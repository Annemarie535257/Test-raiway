from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
import django.utils.timezone as timezone
import random
import json
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.response import Response
from .models import (Farmer, 
                     Farm, 
                     Company, 
                     OTP, 
                     ScoutingRecord, 
                     IrrigationRecord, 
                     PlantingRecord, 
                     ProductionRecord, 
                     HarvestRecord, 
                     FertilizerApplication, 
                     PesticideApplication, 
                     PesticideProduct, 
                     ColdRoomTemperature, 
                     Employee, 
                     HarvestGroup, 
                     SurplusSprayMixDisposal, 
                     EquipmentManagement, 
                     EnvironmentalRecord,
                     SurplusSprayMixDisposal,
                     WorkPlanningTask,
                     TrainingRecord,
                     AccidentIncidentRecord,
                     IncidentReport,
                     InventoryByCropReport,
                     DiseaseSymptomFrequencyReport,
                     WaterUsageByBlockReport,
                     SummaryReport,
)
from .schemas import (
    farmer_registration_schema, 
    farm_registration_schema,
    company_registration_schema, 
    otp_request_schema, 
    otp_verification_schema, 
    signin_schema, 
    signin_response_schema
)
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404

# Register Farmer
@swagger_auto_schema(
    method='post',
    operation_description="Register a new farmer",
    request_body=farmer_registration_schema,
    responses={201: 'Farmer registered successfully', 400: 'Bad Request'}
)
@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def register_farmer(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Logging incoming data for debugging
            print("Incoming data:", data)

            # Check if the required fields are present in the request
            required_fields = [
                'fullName', 'email', 'phoneNumber', 'dateOfBirth', 'gender', 
                'preferredLanguage', 'nationalId', 'password', 'confirmPassword', 
                'country', 'city', 'region'
            ]
            for field in required_fields:
                if field not in data:
                    return JsonResponse({"error": f"Missing field: {field}"}, status=400)

            # Check if the passwords match
            if data['password'] != data['confirmPassword']:
                return JsonResponse({"error": "Passwords do not match"}, status=400)

            # Check if the username or email already exists
            if User.objects.filter(username=data['fullName']).exists():
                return JsonResponse({"error": "Username already exists. Please choose a different username."}, status=400)
            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({"error": "Email already exists. Please choose a different email."}, status=400)

            # Create User with email
            user = User.objects.create_user(
                username=data['fullName'], 
                password=data['password'],  # Using password from the request
                email=data['email']  # Including email in User creation
            )

            # Create Farmer with the User object
            farmer = Farmer.objects.create(
                fullName=data['fullName'],
                email=data['email'],
                phoneNumber=data['phoneNumber'],
                dateOfBirth=data['dateOfBirth'],
                gender=data['gender'],
                preferredLanguage=data['preferredLanguage'],
                nationalId=data['nationalId'],
                country=data['country'],
                city=data['city'],
                region=data['region'],
                user=user
            )

            return JsonResponse({"message": "Farmer registered successfully"}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
        except KeyError as e:
            return JsonResponse({"error": f"Missing field: {str(e)}"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)

# Register Farm
@swagger_auto_schema(
    method='post',
    operation_description="Register a new farm for an existing farmer",
    request_body=farm_registration_schema,
    responses={201: 'Farm registered successfully', 400: 'Bad Request'}
)
@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def register_farm(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Logging incoming data for debugging
            print("Incoming data:", data)

            # Check if farmer exists
            farmer = get_object_or_404(Farmer, id=data['farmer_id'])

            # Create a new farm linked to the farmer
            farm = Farm.objects.create(
                owner=farmer,  # Linking the farm to the registered farmer
                totalFarmArea=data['totalFarmArea'],
                numberOfBlocks=data['numberOfBlocks'],
                mainCropsGrown=data['mainCropsGrown'],
                farmingMethods=data['farmingMethods'],
                soilType=data['soilType'],
                irrigationSystem=data['irrigationSystem'],
                averageAnnualRainfall=data['averageAnnualRainfall'],
                majorChallengesFaced=data['majorChallengesFaced'],
                farmEquipmentOwned=data['farmEquipmentOwned'],
                farmLatitudeCoordinates=data['farmLatitudeCoordinates'],
                farmLongitudeCoordinates=data['farmLongitudeCoordinates']
            )

            return JsonResponse({"message": "Farm registered successfully"}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
        except KeyError as e:
            return JsonResponse({"error": f"Missing field: {str(e)}"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)
                
# Register Company
@swagger_auto_schema(
    method='post',
    operation_description="Register a new company",
    request_body=company_registration_schema,
    responses={201: 'Company registered successfully', 400: 'Bad Request'}
)
@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def register_company(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Create the associated User object for the company
            user = User.objects.create_user(
                username=data['companyName'], 
                password=data['password'], 
                email=data['email']
            )

            # Create the Company object linked to the User
            company = Company.objects.create(
                companyName=data['companyName'],
                mailingAddress=data['mailingAddress'],
                phoneNumber=data['phoneNumber'],
                email=data['email'],
                yearOfEstablishment=data['yearOfEstablishment'],
                registrationNumber=data['registrationNumber'],
                primaryCommodity=data['primaryCommodity'],
                preferredLanguage=data['preferredLanguage'],
                country=data['country'],
                city=data['city'],
                region=data['region'],
                user=user  # Use the already created user object here
            )
            
            return JsonResponse({"message": "Company registered successfully"}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)


# Request OTP
@swagger_auto_schema(
    method='post',
    operation_description="Request OTP",
    request_body=otp_request_schema,
    responses={200: 'OTP sent', 400: 'Bad Request'}
)
@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def request_otp(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            phone_number = data.get('phoneNumber')
            otp_code = str(random.randint(100000, 999999))
            otp = OTP.objects.create(phoneNumber=phone_number, otp=otp_code)
            return JsonResponse({"message": "OTP sent", "otp": otp_code}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)


# Verify OTP
@swagger_auto_schema(
    method='post',
    operation_description="Verify OTP",
    request_body=otp_verification_schema,
    responses={200: 'OTP verified successfully', 400: 'Invalid or expired OTP'}
)
@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def verify_otp(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # phone_number = data.get('phoneNumber')
            otp_code = data.get('otp')
            otp = OTP.objects.filter(otp=otp_code, is_verified=False).first()
            if otp and timezone.now() < otp.expires_at:
                otp.is_verified = True
                otp.save()
                return JsonResponse({"message": "OTP verified successfully"}, status=200)
            return JsonResponse({"error": "Invalid or expired OTP"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)


# Resend OTP
@swagger_auto_schema(
    method='post',
    operation_description="Resend OTP",
    request_body=otp_request_schema,
    responses={200: 'OTP resent', 400: 'Bad Request'}
)
@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def resend_otp(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            phone_number = data.get('phoneNumber')
            otp_code = str(random.randint(100000, 999999))
            otp = OTP.objects.create(phoneNumber=phone_number, otp=otp_code)
            return JsonResponse({"message": "OTP resent", "otp": otp_code}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)



@swagger_auto_schema(
    method='post',
    request_body=signin_schema,
    responses={200: signin_response_schema, 400: "Bad Request", 401: "Unauthorized", 404: "Not Found"}
)
@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def signin(request):
    try:
        data = request.data
        email_or_phone = data.get('email_or_phone')  # This will hold either email or phone number
        password = data.get('password')

        if not email_or_phone or not password:
            return Response({"error": "Email/Phone number and password are required"}, status=400)

        user = None

        # Check if email is provided
        if '@' in email_or_phone:
            try:
                # Authenticate by email
                user = User.objects.get(email=email_or_phone)
            except User.DoesNotExist:
                return Response({"error": "User with this email does not exist"}, status=404)
        else:
            # Authenticate by phone number
            try:
                farmer = Farmer.objects.get(phoneNumber=email_or_phone)
                user = farmer.user
            except Farmer.DoesNotExist:
                try:
                    company = Company.objects.get(phoneNumber=email_or_phone)
                    user = company.user
                except Company.DoesNotExist:
                    return Response({"error": "User with this phone number does not exist"}, status=404)

        # Authenticate using username (which is linked to email or phone)
        user = authenticate(username=user.username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "message": "Login successful"
            }, status=200)
        else:
            return Response({"error": "Invalid credentials"}, status=401)

    except Exception as e:
        return Response({"error": str(e)}, status=400)
    
# Logout

@swagger_auto_schema(
    method='post',
    responses={
        200: "Logout successful",
        400: "Bad Request",
        401: "Unauthorized"
    }
)
@api_view(['POST'])
def signout(request):
    try:
        data = request.data
        refresh_token = data.get('refresh')  # Correct key for token retrieval
        if not refresh_token:
            return Response({"error": "Refresh token required"}, status=status.HTTP_400_BAD_REQUEST)

        token = RefreshToken(refresh_token)
        token.blacklist()  # Invalidate the token
        return Response({"message": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    

#password reset
@swagger_auto_schema(
    method='post',
    responses={
        200: "Password reset successful",
        400: "Bad Request",
        404: "User with this phone number does not exist"
    }
)
@api_view(['POST'])
def reset_password(request):
    try:
        data = request.data
        phone_number = data.get('phoneNumber')  # Phone number used instead of email
        new_password = data.get('password')
        confirm_password = data.get('confirm_password')

        # Check if passwords match
        if new_password != confirm_password:
            return Response({"error": "Passwords do not match"}, status=status.HTTP_400_BAD_REQUEST)

        # Find user by phone number
        user = User.objects.get(farmer__phoneNumber=phone_number)

        # Set the new password
        user.password = make_password(new_password)
        user.save()

        return Response({"message": "Password reset successful"}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"error": "User with this phone number does not exist"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
# View for adding a new Scouting Record
@swagger_auto_schema(
    method='post',
    operation_description="Add a new scouting record",
    responses={201: 'Scouting record added successfully', 400: 'Bad Request'}
)
@api_view(['POST'])
def add_scouting_record(request):
    try:
        data = request.data
        # Fetch the Farm using the UUID
        farm = Farm.objects.get(farm_id=data['farmID'])  # Assuming farm_id is a UUID field

        scouting_record = ScoutingRecord.objects.create(
            farm=farm,  # Use the farm object here
            block=data['block'],
            bed=data['bed'],
            cropType=data['cropType'],
            cropStatus=data['cropStatus'],
            symptoms=data['symptoms'],
            damage=data['damage'],
            pestType=data['pestType'],
            pesticideUsed=data['pesticideUsed'],
            amount=data['amount'],
            waterUsed=data['waterUsed'],
            applicationMode=data['applicationMode']
        )
        return Response({"message": "Scouting record added successfully"}, status=status.HTTP_201_CREATED)
    except Farm.DoesNotExist:
        return Response({"error": "Farm not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
# View for updating a Scouting Record
@swagger_auto_schema(
    method='put',
    operation_description="Update an existing scouting record",
    responses={200: 'Scouting record updated successfully', 404: 'Record not found'}
)
@api_view(['PUT'])
def update_scouting_record(request, id):
    try:
        scouting_record = ScoutingRecord.objects.get(scouting_id=id)
        data = request.data
        scouting_record.block = data['block']
        scouting_record.bed = data['bed']
        scouting_record.cropType = data['cropType']
        scouting_record.cropStatus = data['cropStatus']
        scouting_record.symptoms = data['symptoms']
        scouting_record.damage = data['damage']
        scouting_record.pestType = data['pestType']
        scouting_record.pesticideUsed = data['pesticideUsed']
        scouting_record.amount = data['amount']
        scouting_record.waterUsed = data['waterUsed']
        scouting_record.applicationMode = data['applicationMode']
        scouting_record.save()
        return Response({"message": "Scouting record updated successfully"}, status=status.HTTP_200_OK)
    except ScoutingRecord.DoesNotExist:
        return Response({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)

# View for deleting a Scouting Record
@swagger_auto_schema(
    method='delete',
    operation_description="Soft delete an existing scouting record",
    responses={204: 'Scouting record marked as deleted', 404: 'Record not found'}
)
@api_view(['DELETE'])
def delete_scouting_record(request, id):
    try:
        scouting_record = ScoutingRecord.objects.get(scouting_id=id, is_deleted=False)  # Only find records that are not deleted
        scouting_record.is_deleted = True  # Mark the record as deleted
        scouting_record.save()
        return Response({"message": "Scouting record marked as deleted"}, status=status.HTTP_204_NO_CONTENT)
    except ScoutingRecord.DoesNotExist:
        return Response({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)


# View for adding a new Irrigation Record
@swagger_auto_schema(
    method='post',
    operation_description="Add a new irrigation record",
    responses={201: 'Irrigation record added successfully', 400: 'Bad Request'}
)
@api_view(['POST'])
def add_irrigation_record(request):
    try:
        data = request.data
         # Fetch the Farm using the UUID
        farm = Farm.objects.get(farm_id=data['farmID'])  # Assuming farm_id is a UUID field


        irrigation_record = IrrigationRecord.objects.create(
            farm=farm,
            pumpDischargeRate=data['pumpDischargeRate'],
            block=data['block'],
            year=data['year'],
            cropType=data['cropType'],
            variety=data['variety'],
            pumpStartTime=data['pumpStartTime'],
            totalTimeTaken=data['totalTimeTaken'],
            amountOfWaterUsed=data['amountOfWaterUsed']
        )
        return Response({"message": "Irrigation record added successfully"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# View for updating an Irrigation Record
@swagger_auto_schema(
    method='put',
    operation_description="Update an existing irrigation record",
    responses={200: 'Irrigation record updated successfully', 404: 'Record not found'}
)
@api_view(['PUT'])
def update_irrigation_record(request, id):
    try:
        irrigation_record = IrrigationRecord.objects.get(irrigation_id=id)
        data = request.data
        irrigation_record.pumpDischargeRate = data['pumpDischargeRate']
        irrigation_record.block = data['block']
        irrigation_record.year = data['year']
        irrigation_record.cropType = data['cropType']
        irrigation_record.variety = data['variety']
        irrigation_record.pumpStartTime = data['pumpStartTime']
        irrigation_record.totalTimeTaken = data['totalTimeTaken']
        irrigation_record.amountOfWaterUsed = data['amountOfWaterUsed']
        irrigation_record.save()
        return Response({"message": "Irrigation record updated successfully"}, status=status.HTTP_200_OK)
    except IrrigationRecord.DoesNotExist:
        return Response({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)

# View for deleting an Irrigation Record
@swagger_auto_schema(
    method='delete',
    operation_description="Soft delete an existing irrigation record",
    responses={204: 'Irrigation record marked as deleted', 404: 'Record not found'}
)
@api_view(['DELETE'])
def delete_irrigation_record(request, id):
    try:
        irrigation_record = IrrigationRecord.objects.get(irrigation_id=id, is_deleted=False)  # Only find records that are not deleted
        irrigation_record.is_deleted = True  # Mark the record as deleted
        irrigation_record.save()
        return Response({"message": "Irrigation record marked as deleted"}, status=status.HTTP_204_NO_CONTENT)
    except IrrigationRecord.DoesNotExist:
        return Response({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)


# View for adding a new Planting Record
@swagger_auto_schema(
    method='post',
    operation_description="Add a new planting record",
    responses={201: 'Planting record added successfully', 400: 'Bad Request'}
)
@api_view(['POST'])
def add_planting_record(request):
    try:
        data = request.data
         # Fetch the Farm using the UUID
        farm = Farm.objects.get(farm_id=data['farmID'])  # Assuming farm_id is a UUID field

        planting_record = PlantingRecord.objects.create(
            farm=farm,
            location=data['location'],
            block=data['block'],
            bed=data['bed'],
            cropType=data['cropType'],
            variety=data['variety'],
            plantingMethod=data['plantingMethod'],
            rootStockTreatmentChemical=data['rootStockTreatmentChemical'],
            plantingRate=data['plantingRate'],
            quantityPlanted=data['quantityPlanted'],
            plantingDate=data['plantingDate'],
            expectedHarvestDate=data['expectedHarvestDate']
        )
        return Response({"message": "Planting record added successfully"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# View for updating a Planting Record
@swagger_auto_schema(
    method='put',
    operation_description="Update an existing planting record",
    responses={200: 'Planting record updated successfully', 404: 'Record not found'}
)
@api_view(['PUT'])
def update_planting_record(request, id):
    try:
        planting_record = PlantingRecord.objects.get(planting_id=id)
        data = request.data
        planting_record.location = data['location']
        planting_record.block = data['block']
        planting_record.bed = data['bed']
        planting_record.cropType = data['cropType']
        planting_record.variety = data['variety']
        planting_record.plantingMethod = data['plantingMethod']
        planting_record.rootStockTreatmentChemical = data['rootStockTreatmentChemical']
        planting_record.plantingRate = data['plantingRate']
        planting_record.quantityPlanted = data['quantityPlanted']
        planting_record.plantingDate = data['plantingDate']
        planting_record.expectedHarvestDate = data['expectedHarvestDate']
        planting_record.save()
        return Response({"message": "Planting record updated successfully"}, status=status.HTTP_200_OK)
    except PlantingRecord.DoesNotExist:
        return Response({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)

# View for deleting a Planting Record
@swagger_auto_schema(
    method='delete',
    operation_description="Soft delete an existing planting record",
    responses={204: 'Planting record marked as deleted', 404: 'Record not found'}
)
@api_view(['DELETE'])
def delete_planting_record(request, id):
    try:
        planting_record = PlantingRecord.objects.get(planting_id=id, is_deleted=False)  # Only find records that are not deleted
        planting_record.is_deleted = True  # Mark the record as deleted
        planting_record.save()
        return Response({"message": "Planting record marked as deleted"}, status=status.HTTP_204_NO_CONTENT)
    except PlantingRecord.DoesNotExist:
        return Response({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)


# View for adding a new Harvest Record
@swagger_auto_schema(
    method='post',
    operation_description="Add a new harvest record",
    responses={201: 'Harvest record added successfully', 400: 'Bad Request'}
)
@api_view(['POST'])
def add_harvest_record(request):
    try:
        data = request.data
         # Fetch the Farm using the UUID
        farm = Farm.objects.get(farm_id=data['farmID'])  # Assuming farm_id is a UUID field
        harvest_record = HarvestRecord.objects.create(
            farm=farm,
            harvestNumber=data['harvestNumber'],
            plantingDate=data['plantingDate'],
            block=data['block'],
            variety=data['variety'],
            quantityHarvested=data['quantityHarvested'],
            quantityPacked=data['quantityPacked'],
            quantityRejected=data['quantityRejected'],
            loss=data['loss']
        )
        return Response({"message": "Harvest record added successfully"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# View for updating a Harvest Record
@swagger_auto_schema(
    method='put',
    operation_description="Update an existing harvest record",
    responses={200: 'Harvest record updated successfully', 404: 'Record not found'}
)
@api_view(['PUT'])
def update_harvest_record(request, id):
    try:
        harvest_record = HarvestRecord.objects.get(harvest_id=id)
        data = request.data
        harvest_record.harvestNumber = data['harvestNumber']
        harvest_record.plantingDate = data['plantingDate']
        harvest_record.block = data['block']
        harvest_record.variety = data['variety']
        harvest_record.quantityHarvested = data['quantityHarvested']
        harvest_record.quantityPacked = data['quantityPacked']
        harvest_record.quantityRejected = data['quantityRejected']
        harvest_record.loss = data['loss']
        harvest_record.save()
        return Response({"message": "Harvest record updated successfully"}, status=status.HTTP_200_OK)
    except HarvestRecord.DoesNotExist:
        return Response({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)

# View for deleting a Harvest Record
@swagger_auto_schema(
    method='delete',
    operation_description="Soft delete an existing harvest record",
    responses={204: 'Harvest record marked as deleted', 404: 'Record not found'}
)
@api_view(['DELETE'])
def delete_harvest_record(request, id):
    try:
        harvest_record = HarvestRecord.objects.get(harvest_id=id, is_deleted=False)  # Only find records that are not deleted
        harvest_record.is_deleted = True  # Mark the record as deleted
        harvest_record.save()
        return Response({"message": "Harvest record marked as deleted"}, status=status.HTTP_204_NO_CONTENT)
    except HarvestRecord.DoesNotExist:
        return Response({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)


# View for adding a new Production Record
@swagger_auto_schema(
    method='post',
    operation_description="Add a new production record",
    responses={201: 'Production record added successfully', 400: 'Bad Request'}
)
@api_view(['POST'])
def add_production_record(request):
    try:
        data = request.data
         # Fetch the Farm using the UUID
        farm = Farm.objects.get(farm_id=data['farmID'])  # Assuming farm_id is a UUID field
        production_record = ProductionRecord.objects.create(
            farm=farm,
            productionNumber=data['productionNumber'],
            productionDate=data['productionDate'],
            block=data['block'],
            blockArea=data['blockArea'],
            crop=data['crop'],
            variety=data['variety'],
            productionQuantity=data['productionQuantity'],
            yieldPerSquareMeter=data['yieldPerSquareMeter']
        )
        return Response({"message": "Production record added successfully"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# View for updating a Production Record
@swagger_auto_schema(
    method='put',
    operation_description="Update an existing production record",
    responses={200: 'Production record updated successfully', 404: 'Record not found'}
)
@api_view(['PUT'])
def update_production_record(request, id):
    try:
        production_record = ProductionRecord.objects.get(production_id=id)
        data = request.data
        production_record.productionNumber = data['productionNumber']
        production_record.productionDate = data['productionDate']
        production_record.block = data['block']
        production_record.blockArea = data['blockArea']
        production_record.crop = data['crop']
        production_record.variety = data['variety']
        production_record.productionQuantity = data['productionQuantity']
        production_record.yieldPerSquareMeter = data['yieldPerSquareMeter']
        production_record.save()
        return Response({"message": "Production record updated successfully"}, status=status.HTTP_200_OK)
    except ProductionRecord.DoesNotExist:
        return Response({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)

# View for deleting a Production Record
@swagger_auto_schema(
    method='delete',
    operation_description="Mark an existing production record as deleted",
    responses={204: 'Production record marked as deleted successfully', 404: 'Record not found'}
)
@api_view(['DELETE'])
def delete_production_record(request, id):
    try:
        production_record = ProductionRecord.objects.get(production_id=id)
        production_record.is_deleted = True  # Mark as deleted
        production_record.save()
        return Response({"message": "Production record marked as deleted"}, status=status.HTTP_204_NO_CONTENT)
    except ProductionRecord.DoesNotExist:
        return Response({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)


# Add a new Fertilizer Application Record
@swagger_auto_schema(
    method='post',
    operation_description="Add a new fertilizer application record",
    responses={201: 'Fertilizer record added successfully', 400: 'Bad Request'}
)
@api_view(['POST'])
def add_fertilizer_record(request):
    try:
        data = request.data
        farm = Farm.objects.get(farm_id=data['farmID'])  # Assuming farmID is a UUID field
        fertilizer_record = FertilizerApplication.objects.create(
            farm=farm,
            productionNumber=data['productionNumber'],
            dateOfApplication=data['dateOfApplication'],
            block=data['block'],
            crop=data['crop'],
            variety=data['variety'],
            NPKComposition=data['NPKComposition'],
            ratePerHA=data['ratePerHA'],
            quantityApplied=data['quantityApplied'],
            modeOfApplication=data['modeOfApplication'],
            machineryUsed=data.get('machineryUsed'),  # Optional
            operatorName=data['operatorName']
        )
        return Response({"message": "Fertilizer record added successfully"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# Update a Fertilizer Application Record
@swagger_auto_schema(
    method='put',
    operation_description="Update an existing fertilizer application record",
    responses={200: 'Fertilizer record updated successfully', 404: 'Record not found'}
)
@api_view(['PUT'])
def update_fertilizer_record(request, id):
    try:
        fertilizer_record = FertilizerApplication.objects.get(fertilizerapp_id=id)
        data = request.data
        fertilizer_record.productionNumber = data['productionNumber']
        fertilizer_record.dateOfApplication = data['dateOfApplication']
        fertilizer_record.block = data['block']
        fertilizer_record.crop = data['crop']
        fertilizer_record.variety = data['variety']
        fertilizer_record.NPKComposition = data['NPKComposition']
        fertilizer_record.ratePerHA = data['ratePerHA']
        fertilizer_record.quantityApplied = data['quantityApplied']
        fertilizer_record.modeOfApplication = data['modeOfApplication']
        fertilizer_record.machineryUsed = data.get('machineryUsed', '')
        fertilizer_record.operatorName = data['operatorName']
        fertilizer_record.save()
        return Response({"message": "Fertilizer record updated successfully"}, status=status.HTTP_200_OK)
    except FertilizerApplication.DoesNotExist:
        return Response({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)


# Delete a Fertilizer Application Record
@swagger_auto_schema(
    method='delete',
    operation_description="Soft delete an existing fertilizer record",
    responses={204: 'Fertilizer record marked as deleted', 404: 'Record not found'}
)
@api_view(['DELETE'])
def delete_fertilizer_record(request, id):
    try:
        fertilizer_record = FertilizerApplication.objects.get(fertilizerapp_id=id)
        fertilizer_record.is_deleted = True  # Soft delete
        fertilizer_record.save()  # Save the change
        return Response({"message": "Fertilizer record marked as deleted"}, status=status.HTTP_204_NO_CONTENT)
    except FertilizerApplication.DoesNotExist:
        return Response({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)


# Add a new Pesticide Application Record
@swagger_auto_schema(
    method='post',
    operation_description="Add a new pesticide application record",
    responses={201: 'Pesticide record added successfully', 400: 'Bad Request'}
)
@api_view(['POST'])
def add_pesticide_record(request):
    try:
        data = request.data
        farm = Farm.objects.get(farm_id=data['farmID'])
        pesticide_record = PesticideApplication.objects.create(
            farm=farm,
            recordNumber=data['recordNumber'],
            dateOfApplication=data['dateOfApplication'],
            weather=data['weather'],
            sprayJustification=data['sprayJustification'],
            pppUsed=data['pppUsed'],
            quantityUsed=data['quantityUsed'],
            waterUsed=data['waterUsed'],
            modeOfApplication=data['modeOfApplication'],
            cropVariety=data['cropVariety'],
            reEntryDate=data['reEntryDate'],
            operatorName=data['operatorName'],
            equipmentReference=data.get('equipmentReference', ''),
            approverName=data['approverName']
        )
        return Response({"message": "Pesticide record added successfully"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# Update a Pesticide Application Record
@swagger_auto_schema(
    method='put',
    operation_description="Update an existing pesticide application record",
    responses={200: 'Pesticide record updated successfully', 404: 'Record not found'}
)
@api_view(['PUT'])
def update_pesticide_record(request, id):
    try:
        pesticide_record = PesticideApplication.objects.get(pesticideapp_id=id)
        data = request.data
        pesticide_record.recordNumber = data['recordNumber']
        pesticide_record.dateOfApplication = data['dateOfApplication']
        pesticide_record.weather = data['weather']
        pesticide_record.sprayJustification = data['sprayJustification']
        pesticide_record.pppUsed = data['pppUsed']
        pesticide_record.quantityUsed = data['quantityUsed']
        pesticide_record.waterUsed = data['waterUsed']
        pesticide_record.modeOfApplication = data['modeOfApplication']
        pesticide_record.cropVariety = data['cropVariety']
        pesticide_record.reEntryDate = data['reEntryDate']
        pesticide_record.operatorName = data['operatorName']
        pesticide_record.equipmentReference = data.get('equipmentReference', '')
        pesticide_record.approverName = data['approverName']
        pesticide_record.save()
        return Response({"message": "Pesticide record updated successfully"}, status=status.HTTP_200_OK)
    except PesticideApplication.DoesNotExist:
        return Response({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)


# Delete a Pesticide Application Record
@swagger_auto_schema(
    method='delete',
    operation_description="Mark an existing pesticide application record as deleted",
    responses={204: 'Pesticide record marked as deleted successfully', 404: 'Record not found'}
)
@api_view(['DELETE'])
def delete_pesticide_record(request, id):
    try:
        pesticide_record = PesticideApplication.objects.get(pesticideapp_id=id)  # Correct field
        pesticide_record.is_deleted = True  # Mark as deleted
        pesticide_record.save()
        return Response({"message": "Pesticide record marked as deleted"}, status=status.HTTP_204_NO_CONTENT)
    except PesticideApplication.DoesNotExist:
        return Response({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)

    

# Add a new Pesticide Product Usage Record
@swagger_auto_schema(
    method='post',
    operation_description="Add a new pesticide product usage record",
    responses={201: 'Pesticide product record added successfully', 400: 'Bad Request'}
)
@api_view(['POST'])
def add_pesticide_product(request):
    try:
        data = request.data
        farm = Farm.objects.get(farm_id=data['farmID'])
        pesticide_product = PesticideProduct.objects.create(
            farm=farm,
            tradeName=data['tradeName'],
            activeIngredient=data['activeIngredient'],
            classification=data['classification'],
            targetPest=data['targetPest'],
            PHI=data['PHI'],
            applicationRate=data['applicationRate'],
            waterVolume=data['waterVolume'],
            EUMRL=data.get('EUMRL', None)
        )
        return Response({"message": "Pesticide product record added successfully"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# Update a Pesticide Product Usage Record
@swagger_auto_schema(
    method='put',
    operation_description="Update an existing pesticide product usage record",
    responses={200: 'Pesticide product record updated successfully', 404: 'Record not found'}
)
@api_view(['PUT'])
def update_pesticide_product(request, id):
    try:
        pesticide_product = PesticideProduct.objects.get(pesticide_id=id)
        data = request.data
        pesticide_product.tradeName = data['tradeName']
        pesticide_product.activeIngredient = data['activeIngredient']
        pesticide_product.classification = data['classification']
        pesticide_product.targetPest = data['targetPest']
        pesticide_product.PHI = data['PHI']
        pesticide_product.applicationRate = data['applicationRate']
        pesticide_product.waterVolume = data['waterVolume']
        pesticide_product.EUMRL = data.get('EUMRL', None)
        pesticide_product.save()
        return Response({"message": "Pesticide product record updated successfully"}, status=status.HTTP_200_OK)
    except PesticideProduct.DoesNotExist:
        return Response({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)


# Delete a Pesticide Product Usage Record
@swagger_auto_schema(
    method='delete',
    operation_description="Mark an existing pesticide product record as deleted",
    responses={204: 'Pesticide product record marked as deleted successfully', 404: 'Record not found'}
)
@api_view(['DELETE'])
def delete_pesticide_product(request, id):
    try:
        pesticide_product = PesticideProduct.objects.get(pesticide_id=id)
        pesticide_product.is_deleted = True  # Mark as deleted
        pesticide_product.save()
        return Response({"message": "Pesticide product record marked as deleted"}, status=status.HTTP_204_NO_CONTENT)
    except PesticideProduct.DoesNotExist:
        return Response({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)

    
# View for adding a new Cold Room Record
@swagger_auto_schema(
    method='post',
    operation_description="Add a new cold room temperature monitoring record",
    responses={201: 'Cold Room record added successfully', 400: 'Bad Request'}
)
@api_view(['POST'])
def add_cold_room_record(request):
    try:
        data = request.data
        farm = Farm.objects.get(farm_id=data['farmID'])  # Assuming farm_id is a UUID field
        cold_room_record = ColdRoomTemperature.objects.create(
            farm=farm,
            date=data['date'],
            morningTemp=data['morningTemp'],
            afternoonTemp=data['afternoonTemp'],
            eveningTemp=data['eveningTemp'],
            nightTemp=data['nightTemp'],
            comments=data.get('comments', ''),
            actionTaken=data.get('actionTaken', '')
        )
        return JsonResponse({"message": "Cold Room record added successfully"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# View for updating a Cold Room Record
@swagger_auto_schema(
    method='put',
    operation_description="Update an existing cold room record",
    responses={200: 'Cold Room record updated successfully', 404: 'Record not found'}
)
@api_view(['PUT'])
def update_cold_room_record(request, id):
    try:
        cold_room_record = ColdRoomTemperature.objects.get(coldroom_id=id)
        data = request.data
        cold_room_record.morningTemp = data['morningTemp']
        cold_room_record.afternoonTemp = data['afternoonTemp']
        cold_room_record.eveningTemp = data['eveningTemp']
        cold_room_record.nightTemp = data['nightTemp']
        cold_room_record.comments = data.get('comments', cold_room_record.comments)
        cold_room_record.actionTaken = data.get('actionTaken', cold_room_record.actionTaken)
        cold_room_record.save()
        return JsonResponse({"message": "Cold Room record updated successfully"}, status=status.HTTP_200_OK)
    except ColdRoomTemperature.DoesNotExist:
        return JsonResponse({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)


# View for deleting a Cold Room Record
@swagger_auto_schema(
    method='delete',
    operation_description="Mark an existing cold room record as deleted",
    responses={204: 'Cold Room record marked as deleted successfully', 404: 'Record not found'}
)
@api_view(['DELETE'])
def delete_cold_room_record(request, id):
    try:
        cold_room_record = ColdRoomTemperature.objects.get(coldroom_id=id)
        cold_room_record.is_deleted = True  # Mark as deleted
        cold_room_record.save()
        return JsonResponse({"message": "Cold Room record marked as deleted"}, status=status.HTTP_204_NO_CONTENT)
    except ColdRoomTemperature.DoesNotExist:
        return JsonResponse({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)

    
# View for adding a new Employee Record
@swagger_auto_schema(
    method='post',
    operation_description="Add a new employee record",
    responses={201: 'Employee record added successfully', 400: 'Bad Request'}
)
@api_view(['POST'])
def add_employee_record(request):
    try:
        data = request.data
        farm = Farm.objects.get(farm_id=data['farmID'])  # Assuming farm_id is a UUID field
        employee_record = Employee.objects.create(
            farm=farm,
            fullName=data['fullName'],
            jobTitle=data['jobTitle'],
            department=data['department'],
            contact=data['contact'],
            email=data['email'],
            location=data.get('location', ''),
            startDate=data.get('startDate', None)
        )
        return JsonResponse({"message": "Employee record added successfully"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# View for updating an Employee Record
@swagger_auto_schema(
    method='put',
    operation_description="Update an existing employee record",
    responses={200: 'Employee record updated successfully', 404: 'Record not found'}
)
@api_view(['PUT'])
def update_employee_record(request, id):
    try:
        employee_record = Employee.objects.get(employee_id=id)
        data = request.data
        employee_record.fullName = data['fullName']
        employee_record.jobTitle = data['jobTitle']
        employee_record.department = data['department']
        employee_record.contact = data['contact']
        employee_record.email = data['email']
        employee_record.location = data.get('location', employee_record.location)
        employee_record.startDate = data.get('startDate', employee_record.startDate)
        employee_record.save()
        return JsonResponse({"message": "Employee record updated successfully"}, status=status.HTTP_200_OK)
    except Employee.DoesNotExist:
        return JsonResponse({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)


# View for deleting an Employee Record
@swagger_auto_schema(
    method='delete',
    operation_description="Mark an existing employee record as deleted",
    responses={204: 'Employee record marked as deleted successfully', 404: 'Record not found'}
)
@api_view(['DELETE'])
def delete_employee_record(request, id):
    try:
        employee_record = Employee.objects.get(employee_id=id)
        employee_record.is_deleted = True  # Mark as deleted
        employee_record.save()
        return JsonResponse({"message": "Employee record marked as deleted"}, status=status.HTTP_204_NO_CONTENT)
    except Employee.DoesNotExist:
        return JsonResponse({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)

    
# View for adding a new Harvest Group Record
@swagger_auto_schema(
    method='post',
    operation_description="Add a new harvest group record",
    responses={201: 'Harvest Group record added successfully', 400: 'Bad Request'}
)
@api_view(['POST'])
def add_harvest_group_record(request):
    try:
        data = request.data
        farm = Farm.objects.get(farm_id=data['farmID'])  # Assuming farm_id is a UUID field
        group = HarvestGroup.objects.create(
            farm=farm,
            groupName=data['groupName'],
            farmName=data['farmName'],
            harvestDate=data['harvestDate'],
            totalHours=data['totalHours'],
            totalPay=data['totalPay'],
            harvestYield=data['harvestYield'],
            netProfit=data['netProfit']
        )
        return JsonResponse({"message": "Harvest Group record added successfully"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# View for updating a Harvest Group Record
@swagger_auto_schema(
    method='put',
    operation_description="Update an existing harvest group record",
    responses={200: 'Harvest Group record updated successfully', 404: 'Record not found'}
)
@api_view(['PUT'])
def update_harvest_group_record(request, id):
    try:
        group = HarvestGroup.objects.get(group_id=id)
        data = request.data
        group.groupName = data['groupName']
        group.farmName = data['farmName']
        group.harvestDate = data['harvestDate']
        group.totalHours = data['totalHours']
        group.totalPay = data['totalPay']
        group.harvestYield = data['harvestYield']
        group.netProfit = data['netProfit']
        group.save()
        return JsonResponse({"message": "Harvest Group record updated successfully"}, status=status.HTTP_200_OK)
    except HarvestGroup.DoesNotExist:
        return JsonResponse({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)


# View for deleting a Harvest Group Record
@swagger_auto_schema(
    method='delete',
    operation_description="Mark an existing harvest group record as deleted",
    responses={204: 'Harvest Group record marked as deleted successfully', 404: 'Record not found'}
)
@api_view(['DELETE'])
def delete_harvest_group_record(request, id):
    try:
        group = HarvestGroup.objects.get(group_id=id)
        group.is_deleted = True  # Mark as deleted
        group.save()
        return JsonResponse({"message": "Harvest Group record marked as deleted"}, status=status.HTTP_204_NO_CONTENT)
    except HarvestGroup.DoesNotExist:
        return JsonResponse({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)

    
# View for adding a new Surplus Spray Mix Disposal Record
@swagger_auto_schema(
    method='post',
    operation_description="Add a new surplus spray mix disposal record",
    responses={201: 'Surplus spray mix disposal record added successfully', 400: 'Bad Request'}
)
@api_view(['POST'])
def add_spray_mix_disposal(request):
    try:
        data = request.data
        farm = Farm.objects.get(farm_id=data['farmID'])  # Assuming farmID is a UUID field
        spray_mix_record = SurplusSprayMixDisposal.objects.create(
            farm=farm,
            productName=data['productName'],
            dateOfApplication=data['dateOfApplication'],
            block=data['block'],
            quantityDisposed=data['quantityDisposed'],
            operatorName=data['operatorName'],
            authorizedBy=data['authorizedBy'],
            notes=data.get('notes', '')
        )
        return JsonResponse({"message": "Surplus spray mix disposal record added successfully"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# View for updating a Surplus Spray Mix Disposal Record
@swagger_auto_schema(
    method='put',
    operation_description="Update an existing surplus spray mix disposal record",
    responses={200: 'Surplus spray mix disposal record updated successfully', 404: 'Record not found'}
)
@api_view(['PUT'])
def update_spray_mix_disposal(request, id):
    try:
        spray_mix_record = SurplusSprayMixDisposal.objects.get(surplusmix_id=id)
        data = request.data
        spray_mix_record.productName = data['productName']
        spray_mix_record.dateOfApplication = data['dateOfApplication']
        spray_mix_record.block = data['block']
        spray_mix_record.quantityDisposed = data['quantityDisposed']
        spray_mix_record.operatorName = data['operatorName']
        spray_mix_record.authorizedBy = data['authorizedBy']
        spray_mix_record.notes = data.get('notes', spray_mix_record.notes)
        spray_mix_record.save()
        return JsonResponse({"message": "Surplus spray mix disposal record updated successfully"}, status=status.HTTP_200_OK)
    except SurplusSprayMixDisposal.DoesNotExist:
        return JsonResponse({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)


# View for deleting a Surplus Spray Mix Disposal Record
@swagger_auto_schema(
    method='delete',
    operation_description="Mark an existing surplus spray mix disposal record as deleted",
    responses={204: 'Surplus spray mix disposal record marked as deleted successfully', 404: 'Record not found'}
)
@api_view(['DELETE'])
def delete_spray_mix_disposal(request, id):
    try:
        spray_mix_record = SurplusSprayMixDisposal.objects.get(surplusmix_id=id)
        spray_mix_record.is_deleted = True  # Mark as deleted
        spray_mix_record.save()
        return JsonResponse({"message": "Surplus spray mix disposal record marked as deleted"}, status=status.HTTP_204_NO_CONTENT)
    except SurplusSprayMixDisposal.DoesNotExist:
        return JsonResponse({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)

    

# View for adding a new Equipment Management Record
@swagger_auto_schema(
    method='post',
    operation_description="Add a new equipment management record",
    responses={201: 'Equipment record added successfully', 400: 'Bad Request'}
)
@api_view(['POST'])
def add_equipment_record(request):
    try:
        data = request.data
        farm = Farm.objects.get(farm_id=data['farmID'])  # Assuming farmID is a UUID field
        equipment_record = EquipmentManagement.objects.create(
            farm=farm,
            sprayOperator=data['sprayOperator'],
            equipmentSerialNumber=data['equipmentSerialNumber'],
            equipmentCleaned=data['equipmentCleaned'],
            equipmentCondition=data['equipmentCondition'],
            PPECondition=data['PPECondition'],
            PPECleaned=data['PPECleaned'],
            checkedBy=data['checkedBy']
        )
        return JsonResponse({"message": "Equipment record added successfully"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# View for updating an Equipment Management Record
@swagger_auto_schema(
    method='put',
    operation_description="Update an existing equipment management record",
    responses={200: 'Equipment record updated successfully', 404: 'Record not found'}
)
@api_view(['PUT'])
def update_equipment_record(request, id):
    try:
        equipment_record = EquipmentManagement.objects.get(equipment_id=id)
        data = request.data
        equipment_record.sprayOperator = data['sprayOperator']
        equipment_record.equipmentSerialNumber = data['equipmentSerialNumber']
        equipment_record.equipmentCleaned = data['equipmentCleaned']
        equipment_record.equipmentCondition = data['equipmentCondition']
        equipment_record.PPECondition = data['PPECondition']
        equipment_record.PPECleaned = data['PPECleaned']
        equipment_record.checkedBy = data['checkedBy']
        equipment_record.save()
        return JsonResponse({"message": "Equipment record updated successfully"}, status=status.HTTP_200_OK)
    except EquipmentManagement.DoesNotExist:
        return JsonResponse({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)


# View for deleting an Equipment Management Record
@swagger_auto_schema(
    method='delete',
    operation_description="Mark an existing equipment management record as deleted",
    responses={204: 'Equipment record marked as deleted successfully', 404: 'Record not found'}
)
@api_view(['DELETE'])
def delete_equipment_record(request, id):
    try:
        equipment_record = EquipmentManagement.objects.get(equipment_id=id)
        equipment_record.is_deleted = True  # Mark as deleted
        equipment_record.save()
        return JsonResponse({"message": "Equipment record marked as deleted"}, status=status.HTTP_204_NO_CONTENT)
    except EquipmentManagement.DoesNotExist:
        return JsonResponse({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)


# View for adding a new Environmental Record
@swagger_auto_schema(
    method='post',
    operation_description="Add a new environmental record",
    responses={201: 'Environmental record added successfully', 400: 'Bad Request'}
)
@api_view(['POST'])
def add_environmental_record(request):
    try:
        data = request.data
        farm = Farm.objects.get(farm_id=data['farmID'])  # Assuming farmID is a UUID field
        environmental_record = EnvironmentalRecord.objects.create(
            farm=farm,
            date=data['date'],
            environmentalFactor=data['environmentalFactor'],
            measurement=data['measurement'],
            unit=data['unit'],
            location=data['location'],
            responsiblePerson=data['responsiblePerson'],
            targetBenchmark=data['targetBenchmark'],
            complianceStatus=data['complianceStatus'],
            notes=data.get('notes', ''),
            actionTaken=data.get('actionTaken', '')
        )
        return JsonResponse({"message": "Environmental record added successfully"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# View for updating an Environmental Record
@swagger_auto_schema(
    method='put',
    operation_description="Update an existing environmental record",
    responses={200: 'Environmental record updated successfully', 404: 'Record not found'}
)
@api_view(['PUT'])
def update_environmental_record(request, id):
    try:
        environmental_record = EnvironmentalRecord.objects.get(environmental_id=id)
        data = request.data
        environmental_record.date = data['date']
        environmental_record.environmentalFactor = data['environmentalFactor']
        environmental_record.measurement = data['measurement']
        environmental_record.unit = data['unit']
        environmental_record.location = data['location']
        environmental_record.responsiblePerson = data['responsiblePerson']
        environmental_record.targetBenchmark = data['targetBenchmark']
        environmental_record.complianceStatus = data['complianceStatus']
        environmental_record.notes = data.get('notes', environmental_record.notes)
        environmental_record.actionTaken = data.get('actionTaken', environmental_record.actionTaken)
        environmental_record.save()
        return JsonResponse({"message": "Environmental record updated successfully"}, status=status.HTTP_200_OK)
    except EnvironmentalRecord.DoesNotExist:
        return JsonResponse({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)


# View for deleting an Environmental Record
@swagger_auto_schema(
    method='delete',
    operation_description="Mark an existing environmental record as deleted",
    responses={204: 'Environmental record marked as deleted successfully', 404: 'Record not found'}
)
@api_view(['DELETE'])
def delete_environmental_record(request, id):
    try:
        environmental_record = EnvironmentalRecord.objects.get(environmental_id=id)
        environmental_record.is_deleted = True  # Mark as deleted
        environmental_record.save()
        return JsonResponse({"message": "Environmental record marked as deleted"}, status=status.HTTP_204_NO_CONTENT)
    except EnvironmentalRecord.DoesNotExist:
        return JsonResponse({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)



# View for adding a new Accident/Incident Record
@swagger_auto_schema(
    method='post',
    operation_description="Add a new accident/incident record",
    responses={201: 'Accident/Incident record added successfully', 400: 'Bad Request'}
)
@api_view(['POST'])
def add_accident_record(request):
    try:
        data = request.data
        farm = Farm.objects.get(farm_id=data['farmID'])  # Assuming farmID is a UUID field
        accident_record = AccidentIncidentRecord.objects.create(
            farm=farm,
            safetyType=data['safetyType'],
            inspectorName=data['inspectorName'],
            date=data['date'],
            incidentType=data['incidentType'],
            status=data['status']
        )
        return JsonResponse({"message": "Accident record added successfully"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# View for updating an Accident/Incident Record
@swagger_auto_schema(
    method='put',
    operation_description="Update an existing accident/incident record",
    responses={200: 'Accident/Incident record updated successfully', 404: 'Record not found'}
)
@api_view(['PUT'])
def update_accident_record(request, id):
    try:
        accident_record = AccidentIncidentRecord.objects.get(safety_id=id)
        data = request.data
        accident_record.safetyType = data['safetyType']
        accident_record.inspectorName = data['inspectorName']
        accident_record.date = data['date']
        accident_record.incidentType = data['incidentType']
        accident_record.status = data['status']
        accident_record.save()
        return JsonResponse({"message": "Accident record updated successfully"}, status=status.HTTP_200_OK)
    except AccidentIncidentRecord.DoesNotExist:
        return JsonResponse({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)

# View for deleting an Accident/Incident Record
@swagger_auto_schema(
    method='delete',
    operation_description="Mark an existing accident/incident record as deleted",
    responses={204: 'Accident/Incident record marked as deleted successfully', 404: 'Record not found'}
)
@api_view(['DELETE'])
def delete_accident_record(request, id):
    try:
        accident_record = AccidentIncidentRecord.objects.get(safety_id=id)
        accident_record.is_deleted = True  # Mark as deleted
        accident_record.save()
        return JsonResponse({"message": "Accident/Incident record marked as deleted"}, status=status.HTTP_204_NO_CONTENT)
    except AccidentIncidentRecord.DoesNotExist:
        return JsonResponse({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)



# View for adding a new Work Planning Task
@swagger_auto_schema(
    method='post',
    operation_description="Add a new work planning task",
    responses={201: 'Work planning task added successfully', 400: 'Bad Request'}
)
@api_view(['POST'])
def add_workplanning_task(request):
    try:
        data = request.data
        farm = Farm.objects.get(farm_id=data['farmID'])  # Assuming farmID is a UUID field
        workplanning_task = WorkPlanningTask.objects.create(
            farm=farm,
            title=data['title'],
            department=data['department'],
            assignedTo=data['assignedTo'],
            start=data['start'],
            deadline=data['deadline'],
            status=data['status'],
            notes=data.get('notes', '')
        )
        return JsonResponse({"message": "Work planning task added successfully"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# View for updating a Work Planning Task
@swagger_auto_schema(
    method='put',
    operation_description="Update an existing work planning task",
    responses={200: 'Work planning task updated successfully', 404: 'Record not found'}
)
@api_view(['PUT'])
def update_workplanning_task(request, id):
    try:
        workplanning_task = WorkPlanningTask.objects.get(wp_id=id)
        data = request.data
        workplanning_task.title = data['title']
        workplanning_task.department = data['department']
        workplanning_task.assignedTo = data['assignedTo']
        workplanning_task.start = data['start']
        workplanning_task.deadline = data['deadline']
        workplanning_task.status = data['status']
        workplanning_task.notes = data.get('notes', workplanning_task.notes)
        workplanning_task.save()
        return JsonResponse({"message": "Work planning task updated successfully"}, status=status.HTTP_200_OK)
    except WorkPlanningTask.DoesNotExist:
        return JsonResponse({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)

# View for deleting a Work Planning Task
@swagger_auto_schema(
    method='delete',
    operation_description="Mark an existing work planning task as deleted",
    responses={204: 'Work planning task marked as deleted successfully', 404: 'Record not found'}
)
@api_view(['DELETE'])
def delete_workplanning_task(request, id):
    try:
        workplanning_task = WorkPlanningTask.objects.get(wp_id=id)
        workplanning_task.is_deleted = True  # Mark as deleted
        workplanning_task.save()
        return JsonResponse({"message": "Work planning task marked as deleted"}, status=status.HTTP_204_NO_CONTENT)
    except WorkPlanningTask.DoesNotExist:
        return JsonResponse({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)



# View for adding a new Training Record
@swagger_auto_schema(
    method='post',
    operation_description="Add a new training record",
    responses={201: 'Training record added successfully', 400: 'Bad Request'}
)
@api_view(['POST'])
def add_training_record(request):
    try:
        data = request.data
        farm = Farm.objects.get(farm_id=data['farmID'])  # Assuming farmID is a UUID field
        training_record = TrainingRecord.objects.create(
            farm=farm,
            trainingTitle=data['trainingTitle'],
            trainerName=data['trainerName'],
            date=data['date'],
            topic=data['topic'],
            duration=data['duration'],
            summary=data['summary'],
            materialsProvided=data['materialsProvided'],
            attendance=data['attendance'],
            trainerNotes=data.get('trainerNotes', '')
        )
        return JsonResponse({"message": "Training record added successfully"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# View for updating a Training Record
@swagger_auto_schema(
    method='put',
    operation_description="Update an existing training record",
    responses={200: 'Training record updated successfully', 404: 'Record not found'}
)
@api_view(['PUT'])
def update_training_record(request, id):
    try:
        training_record = TrainingRecord.objects.get(training_id=id)
        data = request.data
        training_record.trainingTitle = data['trainingTitle']
        training_record.trainerName = data['trainerName']
        training_record.date = data['date']
        training_record.topic = data['topic']
        training_record.duration = data['duration']
        training_record.summary = data['summary']
        training_record.materialsProvided = data['materialsProvided']
        training_record.attendance = data['attendance']
        training_record.trainerNotes = data.get('trainerNotes', training_record.trainerNotes)
        training_record.save()
        return JsonResponse({"message": "Training record updated successfully"}, status=status.HTTP_200_OK)
    except TrainingRecord.DoesNotExist:
        return JsonResponse({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)

# View for deleting a Training Record
@swagger_auto_schema(
    method='delete',
    operation_description="Mark an existing training record as deleted",
    responses={204: 'Training record marked as deleted successfully', 404: 'Record not found'}
)
@api_view(['DELETE'])
def delete_training_record(request, id):
    try:
        training_record = TrainingRecord.objects.get(training_id=id)
        training_record.is_deleted = True  # Mark as deleted
        training_record.save()
        return JsonResponse({"message": "Training record marked as deleted"}, status=status.HTTP_204_NO_CONTENT)
    except TrainingRecord.DoesNotExist:
        return JsonResponse({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)


# View for getting Spray Mix Disposal Report
@swagger_auto_schema(
    method='get',
    operation_description="Fetch details of spray mix disposal for a given date range or block",
    responses={200: 'Spray mix disposal report fetched successfully', 400: 'Bad Request'}
)
@api_view(['GET'])
def get_spray_mix_disposal_report(request):
    try:
        # Fetch filters from request (e.g., dateRange, block)
        date_range = request.GET.get('dateRange', None)
        block = request.GET.get('block', None)
        
        # Querying records based on filters
        spray_mix_disposals = SurplusSprayMixDisposal.objects.all()

        if date_range:
            # Apply date range filter
            pass  # Add date range filtering logic here

        if block:
            spray_mix_disposals = spray_mix_disposals.filter(block=block)

        # Return response
        return JsonResponse({"message": "Spray mix disposal report fetched successfully", "data": list(spray_mix_disposals.values())}, status=status.HTTP_200_OK)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# View for getting Incident Reports
@swagger_auto_schema(
    method='get',
    operation_description="Fetches incident reports based on date and block filters",
    responses={200: 'Incident reports fetched successfully', 400: 'Bad Request'}
)
@api_view(['GET'])
def get_incident_reports(request):
    try:
        date = request.GET.get('date', None)
        block = request.GET.get('block', None)
        
        # Querying records based on filters
        incident_reports = IncidentReport.objects.all()

        if date:
            # Apply date filtering
            pass  # Add date filtering logic here

        if block:
            incident_reports = incident_reports.filter(block=block)

        return JsonResponse({"message": "Incident reports fetched successfully", "data": list(incident_reports.values())}, status=status.HTTP_200_OK)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# View for getting Work Plan Reports
@swagger_auto_schema(
    method='get',
    operation_description="Fetches work plan details based on assigned departments, task status, or date",
    responses={200: 'Work plan reports fetched successfully', 400: 'Bad Request'}
)
@api_view(['GET'])
def get_work_plan_reports(request):
    try:
        department = request.GET.get('department', None)
        status = request.GET.get('status', None)
        date = request.GET.get('date', None)
        
        # Querying records based on filters
        work_plans = WorkPlanningTask.objects.all()

        if department:
            work_plans = work_plans.filter(department=department)
        
        if status:
            work_plans = work_plans.filter(status=status)

        if date:
            # Apply date filtering
            pass  # Add date filtering logic here

        return JsonResponse({"message": "Work plan reports fetched successfully", "data": list(work_plans.values())}, status=status.HTTP_200_OK)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# View for getting Inventory by Crop Report
@swagger_auto_schema(
    method='get',
    operation_description="Fetches inventory details by crop variety, including fertilizers and pesticides used",
    responses={200: 'Inventory by crop report fetched successfully', 400: 'Bad Request'}
)
@api_view(['GET'])
def get_inventory_by_crop_report(request):
    try:
        crop_variety = request.GET.get('cropVariety', None)
        
        # Querying records based on filters
        inventory = InventoryByCropReport.objects.all()

        if crop_variety:
            inventory = inventory.filter(cropVariety=crop_variety)

        return JsonResponse({"message": "Inventory by crop report fetched successfully", "data": list(inventory.values())}, status=status.HTTP_200_OK)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# View for getting Water Usage by Block Report
@swagger_auto_schema(
    method='get',
    operation_description="Fetches water usage data for each block over time",
    responses={200: 'Water usage report fetched successfully', 400: 'Bad Request'}
)
@api_view(['GET'])
def get_water_usage_report(request):
    try:
        block = request.GET.get('block', None)
        
        # Querying records based on filters
        water_usage = WaterUsageByBlockReport.objects.all()

        if block:
            water_usage = water_usage.filter(block=block)

        return JsonResponse({"message": "Water usage report fetched successfully", "data": list(water_usage.values())}, status=status.HTTP_200_OK)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# View for getting Disease Symptom Frequency Report
@swagger_auto_schema(
    method='get',
    operation_description="Fetches the frequency of various disease symptoms across different crops",
    responses={200: 'Disease symptom frequency report fetched successfully', 400: 'Bad Request'}
)
@api_view(['GET'])
def get_disease_symptom_frequency_report(request):
    try:
        crop = request.GET.get('crop', None)
        
        # Querying records based on filters
        disease_symptoms = DiseaseSymptomFrequencyReport.objects.all()

        if crop:
            disease_symptoms = disease_symptoms.filter(crop=crop)

        return JsonResponse({"message": "Disease symptom frequency report fetched successfully", "data": list(disease_symptoms.values())}, status=status.HTTP_200_OK)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# View for getting Report Summary
@swagger_auto_schema(
    method='get',
    operation_description="Fetches summarized data for generating reports",
    responses={200: 'Report summary fetched successfully', 400: 'Bad Request'}
)
@api_view(['GET'])
def get_report_summary(request):
    try:
        # Fetch all the relevant data needed for summary
        report_summary = SummaryReport.objects.all()

        return JsonResponse({"message": "Report summary fetched successfully", "data": list(report_summary.values())}, status=status.HTTP_200_OK)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)





