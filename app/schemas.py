from drf_yasg import openapi

# Farmer registration schema
farmer_registration_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['farmerId', 'fullName', 'phoneNumber', 'password'],
    properties={
        # 'farmerId': openapi.Schema(type=openapi.TYPE_INTEGER),
        'fullName': openapi.Schema(type=openapi.TYPE_STRING),
        'email': openapi.Schema(type=openapi.TYPE_STRING),
        'phoneNumber': openapi.Schema(type=openapi.TYPE_STRING),
        'dateOfBirth': openapi.Schema(type=openapi.TYPE_STRING, format='date'),
        'gender': openapi.Schema(type=openapi.TYPE_STRING),
        'preferredLanguage': openapi.Schema(type=openapi.TYPE_STRING),
        'nationalId': openapi.Schema(type=openapi.TYPE_STRING),
        'country': openapi.Schema(type=openapi.TYPE_STRING),
        'city': openapi.Schema(type=openapi.TYPE_STRING),
        'region': openapi.Schema(type=openapi.TYPE_STRING),
        'password': openapi.Schema(type=openapi.TYPE_STRING),
    }
)

# The schemas for the farm related to the farmer will be added here
farm_registration_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['farmer_id', 'totalFarmArea', 'numberOfBlocks', 'mainCropsGrown', 'farmingMethods', 'soilType', 'irrigationSystem', 'averageAnnualRainfall', 'majorChallengesFaced', 'farmEquipmentOwned', 'farmLatitudeCoordinates', 'farmLongitudeCoordinates'],
    properties={
        'farmer_id': openapi.Schema(type=openapi.TYPE_INTEGER),
        'totalFarmArea' : openapi.Schema(type=openapi.TYPE_NUMBER),
        'numberOfBlocks' : openapi.Schema(type=openapi.TYPE_INTEGER),
        'mainCropsGrown' : openapi.Schema(type=openapi.TYPE_STRING),
        'farmingMethods' : openapi.Schema(type=openapi.TYPE_STRING),
        'soilType' : openapi.Schema(type=openapi.TYPE_STRING),
        'irrigationSystem' : openapi.Schema(type=openapi.TYPE_STRING),
        'averageAnnualRainfall' : openapi.Schema(type=openapi.TYPE_NUMBER),
        'majorChallengesFaced' : openapi.Schema(type=openapi.TYPE_STRING),
        'farmEquipmentOwned' : openapi.Schema(type=openapi.TYPE_STRING),
        'farmLatitudeCoordinates' : openapi.Schema(type=openapi.TYPE_NUMBER),
        'farmLongitudeCoordinates' : openapi.Schema(type=openapi.TYPE_NUMBER),
    
    }
    


)

# Company registration schema
company_registration_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['companyId', 'companyName', 'phoneNumber', 'password'],
    properties={
        # 'companyId': openapi.Schema(type=openapi.TYPE_INTEGER),
        'companyName': openapi.Schema(type=openapi.TYPE_STRING),
        'mailingAddress': openapi.Schema(type=openapi.TYPE_STRING),
        'phoneNumber': openapi.Schema(type=openapi.TYPE_STRING),
        'email': openapi.Schema(type=openapi.TYPE_STRING),
        'yearOfEstablishment': openapi.Schema(type=openapi.TYPE_INTEGER),
        'registrationNumber': openapi.Schema(type=openapi.TYPE_STRING),
        'primaryCommodity': openapi.Schema(type=openapi.TYPE_STRING),
        'preferredLanguage': openapi.Schema(type=openapi.TYPE_STRING),
        'country': openapi.Schema(type=openapi.TYPE_STRING),
        'city': openapi.Schema(type=openapi.TYPE_STRING),
        'region': openapi.Schema(type=openapi.TYPE_STRING),
        'password': openapi.Schema(type=openapi.TYPE_STRING),
    }
)

# OTP request schema
otp_request_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['phoneNumber'],
    properties={
        'phoneNumber': openapi.Schema(type=openapi.TYPE_STRING)
    }
)

# OTP verification schema
otp_verification_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['otp'],
    properties={
        # 'phoneNumber': openapi.Schema(type=openapi.TYPE_STRING),
        'otp': openapi.Schema(type=openapi.TYPE_STRING),
    }
)

# Schema for the Signin API request
signin_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['email_or_phone', 'password'],
    properties={
        'email_or_phone': openapi.Schema(type=openapi.TYPE_STRING, description='Email address or phone number of the user'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password of the user'),
    },
    example={
        'email_or_phone': 'john@example.com',
        'password': 'password123',
    }
)

# Schema for the Signin API response
signin_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'refresh': openapi.Schema(type=openapi.TYPE_STRING, description='JWT Refresh Token'),
        'access': openapi.Schema(type=openapi.TYPE_STRING, description='JWT Access Token'),
        'message': openapi.Schema(type=openapi.TYPE_STRING, description='Success message'),
    },
    example={
        'refresh': 'some-refresh-token',
        'access': 'some-access-token',
        'message': 'Login successful',
    }
)

# Schema for the Signout API request

signout_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['refresh'],
    properties={
        'refresh': openapi.Schema(type=openapi.TYPE_STRING, description='JWT Refresh Token'),
    },
    example={
        'refresh': 'some-refresh-token',
    }
)

# Schema for the Signout API response

# Logout request schema
logout_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['refresh'],
    properties={
        'refresh': openapi.Schema(type=openapi.TYPE_STRING, description='JWT Refresh Token to be invalidated'),
    },
    example={
        'refresh': 'some-refresh-token',
    }
)

# Logout response schema
logout_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'message': openapi.Schema(type=openapi.TYPE_STRING, description='Success message after logout'),
    },
    example={
        'message': 'Logout successful',
    }
)

# Password reset schema
# Password reset request schema
password_reset_request_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['phoneNumber'],
    properties={
        'phoneNumber': openapi.Schema(type=openapi.TYPE_STRING, description='Phone number of the user requesting password reset'),
    },
    example={
        'phoneNumber': '+250799999999',
    }
)

# Password reset schema (Reset Password using new password)
password_reset_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['phoneNumber', 'password', 'confirm_password'],
    properties={
        'phoneNumber': openapi.Schema(type=openapi.TYPE_STRING, description='Phone number associated with the user account'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='New password to set'),
        'confirm_password': openapi.Schema(type=openapi.TYPE_STRING, description='Confirmation of the new password'),
    },
    example={
        'phoneNumber': '+250799999999',
        'password': 'newPassword123',
        'confirm_password': 'newPassword123',
    }
)

# ScoutingRecord schema
scouting_record_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['farm', 'scoutID', 'block', 'cropType', 'cropStatus'],
    properties={
        # 'scouting_id': openapi.Schema(type=openapi.TYPE_STRING, description='UUID of the scouting record'),
        'farm': openapi.Schema(type=openapi.TYPE_STRING, description='ForeignKey relationship to the farm (UUID)'),
        # 'scoutID': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the scout'),
        'block': openapi.Schema(type=openapi.TYPE_STRING, description='Block number'),
        'bed': openapi.Schema(type=openapi.TYPE_STRING, description='Bed number'),
        'cropType': openapi.Schema(type=openapi.TYPE_STRING, description='Type of crop'),
        'cropStatus': openapi.Schema(type=openapi.TYPE_STRING, description='Status of the crop'),
        'symptoms': openapi.Schema(type=openapi.TYPE_STRING, description='Observed symptoms'),
        'damage': openapi.Schema(type=openapi.TYPE_STRING, description='Type of damage'),
        'pestType': openapi.Schema(type=openapi.TYPE_STRING, description='Type of pest'),
        'pesticideUsed': openapi.Schema(type=openapi.TYPE_STRING, description='Pesticide applied'),
        'amount': openapi.Schema(type=openapi.TYPE_NUMBER, description='Amount of pesticide applied in liters'),
        'waterUsed': openapi.Schema(type=openapi.TYPE_INTEGER, description='Water used in liters'),
        'applicationMode': openapi.Schema(type=openapi.TYPE_STRING, description='Application method, e.g., sprayer'),
    }
)

# IrrigationRecord schema
irrigation_record_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['farm', 'pumpDischargeRate', 'block', 'year', 'cropType'],
    properties={
        # 'irrigation_id': openapi.Schema(type=openapi.TYPE_STRING, description='UUID of the irrigation record'),
        'farm': openapi.Schema(type=openapi.TYPE_STRING, description='ForeignKey relationship to the farm (UUID)'),
        'pumpDischargeRate': openapi.Schema(type=openapi.TYPE_NUMBER, description='Pump discharge rate in liters/hour'),
        'block': openapi.Schema(type=openapi.TYPE_STRING, description='Block number'),
        'year': openapi.Schema(type=openapi.TYPE_INTEGER, description='Year of irrigation'),
        'cropType': openapi.Schema(type=openapi.TYPE_STRING, description='Type of crop'),
        'variety': openapi.Schema(type=openapi.TYPE_STRING, description='Crop variety'),
        'pumpStartTime': openapi.Schema(type=openapi.TYPE_STRING, format='time', description='Pump start time'),
        'totalTimeTaken': openapi.Schema(type=openapi.TYPE_STRING, description='Duration the pump was running'),
        'amountOfWaterUsed': openapi.Schema(type=openapi.TYPE_NUMBER, description='Total water used in liters'),
    }
)

# PlantingRecord schema
planting_record_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['farm', 'location', 'block', 'cropType', 'plantingMethod'],
    properties={
        # 'planting_id': openapi.Schema(type=openapi.TYPE_STRING, description='UUID of the planting record'),
        'farm': openapi.Schema(type=openapi.TYPE_STRING, description='ForeignKey relationship to the farm (UUID)'),
        'location': openapi.Schema(type=openapi.TYPE_STRING, description='Location of the farm'),
        'block': openapi.Schema(type=openapi.TYPE_STRING, description='Block number'),
        'bed': openapi.Schema(type=openapi.TYPE_STRING, description='Bed number'),
        'cropType': openapi.Schema(type=openapi.TYPE_STRING, description='Type of crop'),
        'variety': openapi.Schema(type=openapi.TYPE_STRING, description='Crop variety'),
        'plantingMethod': openapi.Schema(type=openapi.TYPE_STRING, description='Planting method (e.g., direct seeding)'),
        'rootStockTreatmentChemical': openapi.Schema(type=openapi.TYPE_STRING, description='Rootstock chemical used (if any)', nullable=True),
        'plantingRate': openapi.Schema(type=openapi.TYPE_STRING, description='Rate at which seeds/plants are used (e.g., 6 seeds/m²)'),
        'quantityPlanted': openapi.Schema(type=openapi.TYPE_INTEGER, description='Number of plants or seeds used'),
        'plantingDate': openapi.Schema(type=openapi.TYPE_STRING, format='date', description='Date of planting'),
        'expectedHarvestDate': openapi.Schema(type=openapi.TYPE_STRING, format='date', description='Estimated harvest date'),
    }
)

# HarvestRecord schema
harvest_record_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['farm', 'harvestNumber', 'plantingDate', 'block', 'variety', 'quantityHarvested'],
    properties={
        # 'harvest_id': openapi.Schema(type=openapi.TYPE_STRING, description='UUID of the harvest record'),
        'farm': openapi.Schema(type=openapi.TYPE_STRING, description='ForeignKey relationship to the farm (UUID)'),
        'harvestNumber': openapi.Schema(type=openapi.TYPE_STRING, description='Harvest number (e.g., HARV1234)'),
        'plantingDate': openapi.Schema(type=openapi.TYPE_STRING, format='date', description='Planting date'),
        'block': openapi.Schema(type=openapi.TYPE_STRING, description='Block where the harvest occurred'),
        'variety': openapi.Schema(type=openapi.TYPE_STRING, description='Crop variety'),
        'quantityHarvested': openapi.Schema(type=openapi.TYPE_NUMBER, description='Quantity harvested in kilograms'),
        'quantityPacked': openapi.Schema(type=openapi.TYPE_NUMBER, description='Quantity packed in kilograms'),
        'quantityRejected': openapi.Schema(type=openapi.TYPE_NUMBER, description='Quantity rejected in kilograms'),
        'loss': openapi.Schema(type=openapi.TYPE_NUMBER, description='Loss percentage'),
    }
)

# ProductionRecord schema
production_record_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['farm', 'productionNumber', 'productionDate', 'block', 'blockArea', 'crop'],
    properties={
        # 'production_id': openapi.Schema(type=openapi.TYPE_STRING, description='UUID of the production record'),
        'farm': openapi.Schema(type=openapi.TYPE_STRING, description='ForeignKey relationship to the farm (UUID)'),
        'productionNumber': openapi.Schema(type=openapi.TYPE_STRING, description='Production number'),
        'productionDate': openapi.Schema(type=openapi.TYPE_STRING, format='date', description='Production date'),
        'block': openapi.Schema(type=openapi.TYPE_STRING, description='Block where production took place'),
        'blockArea': openapi.Schema(type=openapi.TYPE_NUMBER, description='Block area in square meters'),
        'crop': openapi.Schema(type=openapi.TYPE_STRING, description='Crop produced'),
        'variety': openapi.Schema(type=openapi.TYPE_STRING, description='Crop variety'),
        'productionQuantity': openapi.Schema(type=openapi.TYPE_NUMBER, description='Total production quantity in kilograms'),
        'yieldPerSquareMeter': openapi.Schema(type=openapi.TYPE_NUMBER, description='Yield per square meter (kg/m²)'),
    }
)

# Fertilizer Application Schema
fertilizer_record_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['farm', 'fertilID', 'productionNumber', 'dateOfApplication', 'block', 'crop', 'variety', 'NPKComposition', 'ratePerHA', 'quantityApplied', 'modeOfApplication', 'operatorName'],
    properties={
        'farm': openapi.Schema(type=openapi.TYPE_STRING, description='ForeignKey relationship to the farm (UUID)'),
        # 'fertilID': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the fertilizer'),
        'productionNumber': openapi.Schema(type=openapi.TYPE_STRING, description='Production batch number'),
        'dateOfApplication': openapi.Schema(type=openapi.TYPE_STRING, format='date', description='Date of fertilizer application'),
        'block': openapi.Schema(type=openapi.TYPE_STRING, description='Block where the fertilizer was applied'),
        'crop': openapi.Schema(type=openapi.TYPE_STRING, description='Crop being fertilized'),
        'variety': openapi.Schema(type=openapi.TYPE_STRING, description='Crop variety'),
        'NPKComposition': openapi.Schema(type=openapi.TYPE_STRING, description='NPK composition of the fertilizer used'),
        'ratePerHA': openapi.Schema(type=openapi.TYPE_NUMBER, description='Rate of fertilizer per hectare'),
        'quantityApplied': openapi.Schema(type=openapi.TYPE_NUMBER, description='Total amount of fertilizer applied'),
        'modeOfApplication': openapi.Schema(type=openapi.TYPE_STRING, description='Mode of application (e.g., Manual, Machinery)'),
        'machineryUsed': openapi.Schema(type=openapi.TYPE_STRING, description='Type of machinery used, if applicable', nullable=True),
        'operatorName': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the person applying the fertilizer'),
    }
)

# Pesticide Application Schema
pesticide_record_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['farm', 'pestID', 'recordNumber', 'dateOfApplication', 'weather', 'sprayJustification', 'pppUsed', 'quantityUsed', 'waterUsed', 'modeOfApplication', 'cropVariety', 'reEntryDate', 'operatorName', 'approverName'],
    properties={
        'farm': openapi.Schema(type=openapi.TYPE_STRING, description='ForeignKey relationship to the farm (UUID)'),
        # 'pestID': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the pesticide'),
        'recordNumber': openapi.Schema(type=openapi.TYPE_STRING, description='Unique record number for the pesticide application'),
        'dateOfApplication': openapi.Schema(type=openapi.TYPE_STRING, format='date', description='Date of pesticide application'),
        'weather': openapi.Schema(type=openapi.TYPE_STRING, description='Weather conditions during the application'),
        'sprayJustification': openapi.Schema(type=openapi.TYPE_STRING, description='Reason for pesticide application'),
        'pppUsed': openapi.Schema(type=openapi.TYPE_STRING, description='Pesticide product used'),
        'quantityUsed': openapi.Schema(type=openapi.TYPE_NUMBER, description='Amount of pesticide applied in liters'),
        'waterUsed': openapi.Schema(type=openapi.TYPE_NUMBER, description='Amount of water used in liters'),
        'modeOfApplication': openapi.Schema(type=openapi.TYPE_STRING, description='Mode of pesticide application (e.g., Backpack Sprayer)'),
        'cropVariety': openapi.Schema(type=openapi.TYPE_STRING, description='Crop variety being treated'),
        'reEntryDate': openapi.Schema(type=openapi.TYPE_STRING, format='date', description='Safe re-entry date after application'),
        'operatorName': openapi.Schema(type=openapi.TYPE_STRING, description='Operator applying the pesticide'),
        'equipmentReference': openapi.Schema(type=openapi.TYPE_STRING, description='Equipment used, if applicable', nullable=True),
        'approverName': openapi.Schema(type=openapi.TYPE_STRING, description='Person approving the pesticide application'),
    }
)

# Pesticide Product Usage (PPU) Schema
pesticide_product_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['farm', 'pestproID', 'tradeName', 'activeIngredient', 'classification', 'targetPest', 'PHI', 'applicationRate', 'waterVolume'],
    properties={
        'farm': openapi.Schema(type=openapi.TYPE_STRING, description='ForeignKey relationship to the farm (UUID)'),
        # 'pestproID': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the pesticide product'),
        'tradeName': openapi.Schema(type=openapi.TYPE_STRING, description='Trade name of the pesticide product'),
        'activeIngredient': openapi.Schema(type=openapi.TYPE_STRING, description='Active ingredient of the pesticide'),
        'classification': openapi.Schema(type=openapi.TYPE_STRING, description='Classification (e.g., Herbicide, Insecticide)'),
        'targetPest': openapi.Schema(type=openapi.TYPE_STRING, description='Target pests being controlled'),
        'PHI': openapi.Schema(type=openapi.TYPE_INTEGER, description='Pre-harvest interval in days'),
        'applicationRate': openapi.Schema(type=openapi.TYPE_STRING, description='Application rate (e.g., L/ha, mL/ha)'),
        'waterVolume': openapi.Schema(type=openapi.TYPE_INTEGER, description='Water volume used for application'),
        'EUMRL': openapi.Schema(type=openapi.TYPE_NUMBER, description='European Union maximum residue level in mg/kg', nullable=True),
    }
)

# Cold Room Record schema
cold_room_record_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['farm', 'coldRoomId', 'date', 'morningTemp', 'afternoonTemp', 'eveningTemp', 'nightTemp'],
    properties={
        'farm': openapi.Schema(type=openapi.TYPE_STRING, description='ForeignKey relationship to the farm (UUID)'),
        # 'coldRoomId': openapi.Schema(type=openapi.TYPE_STRING, description='Identifier for the cold room (e.g., CRM1)'),
        'date': openapi.Schema(type=openapi.TYPE_STRING, format='date', description='Date of the record'),
        'morningTemp': openapi.Schema(type=openapi.TYPE_NUMBER, description='Morning temperature in °C'),
        'afternoonTemp': openapi.Schema(type=openapi.TYPE_NUMBER, description='Afternoon temperature in °C'),
        'eveningTemp': openapi.Schema(type=openapi.TYPE_NUMBER, description='Evening temperature in °C'),
        'nightTemp': openapi.Schema(type=openapi.TYPE_NUMBER, description='Night temperature in °C'),
        'comments': openapi.Schema(type=openapi.TYPE_STRING, description='Comments about the day’s temperature (optional)', nullable=True),
        'actionTaken': openapi.Schema(type=openapi.TYPE_STRING, description='Actions taken based on temperature readings (optional)', nullable=True),
    }
)

# Employee Management schema
employee_record_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['farm', 'fullName', 'employeeID', 'jobTitle', 'department', 'contact', 'email'],
    properties={
        'farm': openapi.Schema(type=openapi.TYPE_STRING, description='ForeignKey relationship to the farm (UUID)'),
        'fullName': openapi.Schema(type=openapi.TYPE_STRING, description='Full name of the employee'),
        # 'employeeID': openapi.Schema(type=openapi.TYPE_INTEGER, description='Unique employee ID'),
        'jobTitle': openapi.Schema(type=openapi.TYPE_STRING, description='Job title of the employee'),
        'department': openapi.Schema(type=openapi.TYPE_STRING, description='Department of the employee'),
        'contact': openapi.Schema(type=openapi.TYPE_STRING, description='Contact number of the employee'),
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email address of the employee'),
        'location': openapi.Schema(type=openapi.TYPE_STRING, description='Location of the employee (optional)', nullable=True),
        'startDate': openapi.Schema(type=openapi.TYPE_STRING, format='date', description='Start date of employment (optional)', nullable=True),
    }
)

# Harvest Group schema
harvest_group_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['farm', 'groupID', 'groupName', 'farmName', 'harvestDate', 'totalHours', 'totalPay', 'harvestYield', 'netProfit'],
    properties={
        'farm': openapi.Schema(type=openapi.TYPE_STRING, description='ForeignKey relationship to the farm (UUID)'),
        # 'groupID': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the Harvest group'),
        'groupName': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the harvest group'),
        'farmName': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the farm where the harvest took place'),
        'harvestDate': openapi.Schema(type=openapi.TYPE_STRING, format='date', description='Date of the harvest'),
        'totalHours': openapi.Schema(type=openapi.TYPE_INTEGER, description='Total hours worked by the group'),
        'totalPay': openapi.Schema(type=openapi.TYPE_STRING, description='Total pay for the group (e.g., "$3,600")'),
        'harvestYield': openapi.Schema(type=openapi.TYPE_STRING, description='Harvest yield in kilograms or another unit (e.g., "5,000 kg")'),
        'netProfit': openapi.Schema(type=openapi.TYPE_STRING, description='Net profit earned from the harvest (e.g., "$5,000")'),
    }
)

# Surplus Spray Mix Disposal schema
spray_mix_disposal_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['farm', 'SSMID', 'productName', 'dateOfApplication', 'block', 'quantityDisposed', 'operatorName', 'authorizedBy'],
    properties={
        'farm': openapi.Schema(type=openapi.TYPE_STRING, description='ForeignKey relationship to the farm (UUID)'),
        # 'SSMID': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the Surplus Spray Mix'),
        'productName': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the product (e.g., Herbicide X)'),
        'dateOfApplication': openapi.Schema(type=openapi.TYPE_STRING, format='date', description='Date of application'),
        'block': openapi.Schema(type=openapi.TYPE_STRING, description='Block where the product was applied'),
        'quantityDisposed': openapi.Schema(type=openapi.TYPE_NUMBER, description='Amount of surplus spray mix disposed in liters'),
        'operatorName': openapi.Schema(type=openapi.TYPE_STRING, description='Operator applying or disposing of the spray mix'),
        'authorizedBy': openapi.Schema(type=openapi.TYPE_STRING, description='Person authorizing the disposal'),
        'notes': openapi.Schema(type=openapi.TYPE_STRING, description='Additional information or observations (optional)', nullable=True),
    }
)

# Equipment Management schema
equipment_record_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['farm', 'EquiID', 'sprayOperator', 'equipmentSerialNumber', 'equipmentCleaned', 'equipmentCondition', 'PPECondition', 'PPECleaned', 'checkedBy'],
    properties={
        'farm': openapi.Schema(type=openapi.TYPE_STRING, description='ForeignKey relationship to the farm (UUID)'),
        # 'EquiID': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the Equipment Management record'),
        'sprayOperator': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the spray operator'),
        'equipmentSerialNumber': openapi.Schema(type=openapi.TYPE_STRING, description='Serial number of the equipment used'),
        'equipmentCleaned': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Indicates whether the equipment was cleaned'),
        'equipmentCondition': openapi.Schema(type=openapi.TYPE_STRING, description='Condition of the equipment'),
        'PPECondition': openapi.Schema(type=openapi.TYPE_STRING, description='Condition of the PPE'),
        'PPECleaned': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Indicates whether the PPE was cleaned'),
        'checkedBy': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the person who checked the equipment and PPE'),
    }
)

# Environmental Record schema
environmental_record_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['farm', 'envID', 'date', 'environmentalFactor', 'measurement', 'unit', 'location', 'responsiblePerson', 'targetBenchmark', 'complianceStatus'],
    properties={
        'farm': openapi.Schema(type=openapi.TYPE_STRING, description='ForeignKey relationship to the farm (UUID)'),
        'date': openapi.Schema(type=openapi.TYPE_STRING, format='date', description='Date of the environmental record'),
        'environmentalFactor': openapi.Schema(type=openapi.TYPE_STRING, description='Environmental factor (e.g., Energy Use)'),
        'measurement': openapi.Schema(type=openapi.TYPE_STRING, description='Value of the environmental measurement'),
        'unit': openapi.Schema(type=openapi.TYPE_STRING, description='Unit of the measurement (e.g., kg)'),
        'location': openapi.Schema(type=openapi.TYPE_STRING, description='Location or area of the measurement'),
        'responsiblePerson': openapi.Schema(type=openapi.TYPE_STRING, description='Person responsible for the measurement'),
        'targetBenchmark': openapi.Schema(type=openapi.TYPE_STRING, description='Target value or benchmark for compliance'),
        'complianceStatus': openapi.Schema(type=openapi.TYPE_STRING, description='Compliance status (e.g., met, not met)'),
        'notes': openapi.Schema(type=openapi.TYPE_STRING, description='Additional notes (optional)', nullable=True),
        'actionTaken': openapi.Schema(type=openapi.TYPE_STRING, description='Actions taken based on measurement (optional)', nullable=True),
    }
)

# Accident/Incident Record Schema
accident_record_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['farmID', 'safetyID', 'safetyType', 'inspectorName', 'date', 'incidentType', 'status'],
    properties={
        'farmID': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the farm'),
        # 'safetyID': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the safety record'),
        'safetyType': openapi.Schema(type=openapi.TYPE_STRING, description='Type of safety record (e.g., Inspection, Incident, Training)'),
        'inspectorName': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the inspector or auditor'),
        'date': openapi.Schema(type=openapi.TYPE_STRING, format='date', description='Date of the safety event'),
        'incidentType': openapi.Schema(type=openapi.TYPE_STRING, description='Type of incident (e.g., Fire, Injury)'),
        'status': openapi.Schema(type=openapi.TYPE_STRING, description='Status of the record (e.g., Resolved, Pending)'),
        'limit': openapi.Schema(type=openapi.TYPE_INTEGER, description='Limit the number of records returned', nullable=True),
        'page': openapi.Schema(type=openapi.TYPE_INTEGER, description='Pagination support', nullable=True),
    }
)

# Work Planning Task Schema
work_planning_task_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['farmID', 'WPID', 'title', 'department', 'assignedTo', 'start', 'deadline', 'status'],
    properties={
        'farmID': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the farm'),
        # 'WPID': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the work planning task'),
        'title': openapi.Schema(type=openapi.TYPE_STRING, description='Title or description of the task'),
        'department': openapi.Schema(type=openapi.TYPE_STRING, description='Department responsible for the task'),
        'assignedTo': openapi.Schema(type=openapi.TYPE_STRING, description='Person assigned to the task'),
        'start': openapi.Schema(type=openapi.TYPE_STRING, format='date', description='Start date of the task'),
        'deadline': openapi.Schema(type=openapi.TYPE_STRING, format='date', description='Deadline for task completion'),
        'status': openapi.Schema(type=openapi.TYPE_STRING, description='Current status of the task (e.g., Completed, Pending, In Progress)'),
        'notes': openapi.Schema(type=openapi.TYPE_STRING, description='Additional notes for the task', nullable=True),
    }
)

# Training Record Schema
training_record_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['farmID', 'TrainingID', 'trainingTitle', 'trainerName', 'date', 'topic', 'duration', 'attendance'],
    properties={
        'farmID': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the farm'),
        # 'TrainingID': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the training record'),
        'trainingTitle': openapi.Schema(type=openapi.TYPE_STRING, description='Title of the training session'),
        'trainerName': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the trainer'),
        'date': openapi.Schema(type=openapi.TYPE_STRING, format='date', description='Date of the training session'),
        'topic': openapi.Schema(type=openapi.TYPE_STRING, description='Topic covered in the training'),
        'duration': openapi.Schema(type=openapi.TYPE_STRING, description='Duration of the training (e.g., 2 hours)'),
        'attendance': openapi.Schema(type=openapi.TYPE_INTEGER, description='Number of participants who attended'),
        'materialsProvided': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_STRING), description='Materials provided during the training'),
        'trainerNotes': openapi.Schema(type=openapi.TYPE_STRING, description='Additional notes from the trainer', nullable=True),
    }
)

# Report: Spray Mix Disposal Schema
spray_mix_disposal_report_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'dateRange': openapi.Schema(type=openapi.TYPE_STRING, format='date-range', description='Date range for the spray mix disposal records'),
        'block': openapi.Schema(type=openapi.TYPE_STRING, description='Block where the disposal occurred', nullable=True),
    }
)

# Report: Incident Report Schema
incident_report_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'date': openapi.Schema(type=openapi.TYPE_STRING, format='date', description='Date of the incident'),
        'block': openapi.Schema(type=openapi.TYPE_STRING, description='Block where the incident occurred', nullable=True),
    }
)

# Report: Work Plan Schema
work_plan_report_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'department': openapi.Schema(type=openapi.TYPE_STRING, description='Assigned department for the task'),
        'status': openapi.Schema(type=openapi.TYPE_STRING, description='Current status of the task (e.g., Completed, Pending, In Progress)'),
        'date': openapi.Schema(type=openapi.TYPE_STRING, format='date', description='Date of the task', nullable=True),
    }
)

# Report: Inventory by Crop Schema
inventory_by_crop_report_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'cropVariety': openapi.Schema(type=openapi.TYPE_STRING, description='Crop variety for which inventory details are fetched', nullable=True),
    }
)

# Report: Water Usage Schema
water_usage_report_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'block': openapi.Schema(type=openapi.TYPE_STRING, description='Block where the water usage occurred', nullable=True),
    }
)

# Report: Disease Symptom Frequency Schema
disease_symptom_frequency_report_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'crop': openapi.Schema(type=openapi.TYPE_STRING, description='Crop for which the disease symptom frequency is fetched', nullable=True),
    }
)

# Report Summary Schema
report_summary_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        # Add any additional filters or parameters for fetching the report summary
    }
)
