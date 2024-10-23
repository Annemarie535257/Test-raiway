from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid
import random

# Farmer Model
class Farmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    farmer_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # UUID for Farmer
    email = models.EmailField(default='default@example.com')
    fullName = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=15)
    dateOfBirth = models.DateField()
    gender = models.CharField(max_length=10)
    preferredLanguage = models.CharField(max_length=50)
    nationalId = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)

    def __str__(self):
        return self.fullName

# Company Model
class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # UUID for Company
    companyName = models.CharField(max_length=255)
    mailingAddress = models.TextField()
    phoneNumber = models.CharField(max_length=15)
    email = models.EmailField(default='default@example.com')
    yearOfEstablishment = models.IntegerField()
    registrationNumber = models.CharField(max_length=20)
    primaryCommodity = models.CharField(max_length=255, default='Maize')  # Set default value here
    preferredLanguage = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)

    def __str__(self):
        return self.companyName

# Farm Model
class Farm(models.Model):
    farm_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # UUID for Farm
    owner = models.ForeignKey(Farmer, on_delete=models.CASCADE, null=True, blank=True)
    # company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    totalFarmArea = models.FloatField()
    numberOfBlocks = models.IntegerField()
    mainCropsGrown = models.CharField(max_length=255)
    farmingMethods = models.CharField(max_length=255, default='Traditional')  # Set default value here
    soilType = models.CharField(max_length=255, default='Loamy') 
    irrigationSystem = models.CharField(max_length=255)
    averageAnnualRainfall = models.FloatField()
    majorChallengesFaced = models.TextField()
    farmEquipmentOwned = models.TextField()
    farmLatitudeCoordinates = models.FloatField()
    farmLongitudeCoordinates = models.FloatField()

    def __str__(self):
        return f'Farm owned by {self.owner}'

# Function to calculate OTP expiration time
def get_expiry_time():
    return timezone.now() + timezone.timedelta(minutes=10)

# OTP Model for verification
class OTP(models.Model):
    phoneNumber = models.CharField(max_length=15)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(default=timezone.now)
    is_verified = models.BooleanField(default=False)
    expires_at = models.DateTimeField(default=get_expiry_time)

    def __str__(self):
        return f'OTP for {self.phoneNumber}'

# Scouting Record Model
class ScoutingRecord(models.Model):
    scouting_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # UUID for Scouting Record
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)  # ForeignKey relationship to Farm
    block = models.CharField(max_length=255)
    bed = models.CharField(max_length=255)
    cropType = models.CharField(max_length=255)
    cropStatus = models.CharField(max_length=255)
    symptoms = models.CharField(max_length=255)
    damage = models.CharField(max_length=255)
    pestType = models.CharField(max_length=255)
    pesticideUsed = models.CharField(max_length=255)
    amount = models.FloatField()  # Amount of pesticide in liters
    waterUsed = models.IntegerField()  # Water used in liters
    applicationMode = models.CharField(max_length=255)  # Sprayer, etc.
    is_deleted = models.BooleanField(default=False)  # Field for soft delete


    def __str__(self):
        return f'Scouting record for farm {self.farm}'


# Irrigation Record Model
class IrrigationRecord(models.Model):
    irrigation_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # UUID for Irrigation Record
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)  # ForeignKey relationship to Farm
    pumpDischargeRate = models.FloatField()  # Pump discharge in liters/hour
    block = models.CharField(max_length=255)
    year = models.IntegerField()
    cropType = models.CharField(max_length=255)
    variety = models.CharField(max_length=255)
    pumpStartTime = models.TimeField()
    totalTimeTaken = models.CharField(max_length=255)  # Duration in hours
    amountOfWaterUsed = models.FloatField()  # Water in liters
    is_deleted = models.BooleanField(default=False)  # Field for soft delete


    def __str__(self):
        return f'Irrigation record for farm {self.farm}'


# Planting Record Model
class PlantingRecord(models.Model):
    planting_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # UUID for Planting Record
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)  # ForeignKey relationship to Farm
    location = models.CharField(max_length=255)
    block = models.CharField(max_length=255)
    bed = models.CharField(max_length=255)
    cropType = models.CharField(max_length=255)
    variety = models.CharField(max_length=255)
    plantingMethod = models.CharField(max_length=255)  # Direct seeding, transplanting
    rootStockTreatmentChemical = models.CharField(max_length=255, blank=True, null=True)  # Optional
    plantingRate = models.CharField(max_length=255)  # Rate in seeds per square meter
    quantityPlanted = models.IntegerField()  # Quantity of seeds/plants
    plantingDate = models.DateField()
    expectedHarvestDate = models.DateField()
    is_deleted = models.BooleanField(default=False)  # Field for soft delete


    def __str__(self):
        return f'Planting record for farm {self.farm}'


# Harvest Record Model
class HarvestRecord(models.Model):
    harvest_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # UUID for Harvest Record
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)  # ForeignKey relationship to Farm
    harvestNumber = models.CharField(max_length=255)
    plantingDate = models.DateField()
    block = models.CharField(max_length=255)
    variety = models.CharField(max_length=255)
    quantityHarvested = models.FloatField()  # In kilograms
    quantityPacked = models.FloatField()  # In kilograms
    quantityRejected = models.FloatField()  # In kilograms
    loss = models.FloatField()  # Loss percentage
    is_deleted = models.BooleanField(default=False)  # Field for soft delete

    # history = HistoricalRecords()  # Add this line to track changes


    def __str__(self):
        return f'Harvest record for farm {self.farm}'


# Production Record Model
class ProductionRecord(models.Model):
    production_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # UUID for Production Record
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)  # ForeignKey relationship to Farm
    productionNumber = models.CharField(max_length=255)
    productionDate = models.DateField()
    block = models.CharField(max_length=255)
    blockArea = models.FloatField()  # Area in square meters
    crop = models.CharField(max_length=255)
    variety = models.CharField(max_length=255)
    productionQuantity = models.FloatField()  # Quantity in kilograms
    yieldPerSquareMeter = models.FloatField()  # Yield in kilograms/m²
    is_deleted = models.BooleanField(default=False)  # Field for soft delete

    # history = HistoricalRecords()  # Add this line to track changes


    def __str__(self):
        return f'Production record for farm {self.farm}'
    

# Fertilizer Application Model
class FertilizerApplication(models.Model):
    fertilizerapp_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # UUID for Fertilizer Application
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)  # ForeignKey to Farm
    fertilID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # UUID for Fertilizer
    productionNumber = models.CharField(max_length=255)  # Production number for the batch
    dateOfApplication = models.DateField()  # Date of fertilizer application
    block = models.CharField(max_length=255)  # Block where the fertilizer was applied
    crop = models.CharField(max_length=255)  # Crop being fertilized
    variety = models.CharField(max_length=255)  # Crop variety
    NPKComposition = models.CharField(max_length=255)  # NPK Composition of fertilizer
    ratePerHA = models.FloatField()  # Rate of fertilizer per hectare
    quantityApplied = models.FloatField()  # Total quantity of fertilizer applied
    modeOfApplication = models.CharField(max_length=255)  # Mode of application (e.g., Manual, Machinery)
    machineryUsed = models.CharField(max_length=255, blank=True, null=True)  # Machinery used (optional)
    operatorName = models.CharField(max_length=255)  # Operator applying the fertilizer
    is_deleted = models.BooleanField(default=False)  # Field for soft delete

    # history = HistoricalRecords()  # Tracks changes to the model

    def __str__(self):
        return f'Fertilizer application for farm {self.farm}, block {self.block}'

# Pesticide Application Model
class PesticideApplication(models.Model):
    pesticideapp_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # UUID for Pesticide Application
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)  # ForeignKey to Farm
    pestID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # UUID for Pesticide
    recordNumber = models.CharField(max_length=255)  # Unique record number for pesticide application
    dateOfApplication = models.DateField()  # Date of pesticide application
    weather = models.CharField(max_length=255)  # Weather conditions during application
    sprayJustification = models.TextField()  # Reason for pesticide application
    pppUsed = models.CharField(max_length=255)  # Pesticide product used
    quantityUsed = models.FloatField()  # Quantity of pesticide used (in liters)
    waterUsed = models.FloatField()  # Volume of water used (in liters)
    modeOfApplication = models.CharField(max_length=255)  # Method of application (e.g., Backpack Sprayer)
    cropVariety = models.CharField(max_length=255)  # Crop or variety treated
    reEntryDate = models.DateField()  # Safe re-entry date
    operatorName = models.CharField(max_length=255)  # Operator applying the pesticide
    equipmentReference = models.CharField(max_length=255, blank=True, null=True)  # Reference for equipment used (optional)
    approverName = models.CharField(max_length=255)  # Name of the approver for pesticide application
    is_deleted = models.BooleanField(default=False)  # Field for soft delete

    # history = HistoricalRecords()  # Tracks changes to the model

    def __str__(self):
        return f'Pesticide application for farm {self.farm}, record {self.recordNumber}'
    
# Pesticide Product Usage (PPU) Model
class PesticideProduct(models.Model):
    pesticide_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # UUID for Pesticide Product
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)  # ForeignKey to Farm
    pestproID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # UUID for Pesticide Product
    tradeName = models.CharField(max_length=255)  # Trade name of the pesticide product
    activeIngredient = models.CharField(max_length=255)  # Active ingredient in the pesticide
    classification = models.CharField(max_length=255)  # Classification (e.g., Herbicide, Insecticide)
    targetPest = models.CharField(max_length=255)  # Target pests being controlled
    PHI = models.IntegerField()  # Pre-harvest interval in days
    applicationRate = models.CharField(max_length=255)  # Application rate (e.g., L/ha)
    waterVolume = models.IntegerField()  # Volume of water used in the application
    EUMRL = models.FloatField(blank=True, null=True)  # EU maximum residue level (optional)
    is_deleted = models.BooleanField(default=False)  # Field for soft delete

    # history = HistoricalRecords()  # Tracks changes to the model

    def __str__(self):
        return f'Pesticide product: {self.tradeName}, used on farm {self.farm}'
    
#Cold Room Temperature Model
class ColdRoomTemperature(models.Model):
    coldroom_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # UUID for Cold Room
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)  # ForeignKey relationship to Farm
    coldRoomId = models.CharField(max_length=255)  # Identifier for the cold room
    date = models.DateField()  # Date of the record
    morningTemp = models.FloatField()  # Morning temperature in °C
    afternoonTemp = models.FloatField()  # Afternoon temperature in °C
    eveningTemp = models.FloatField()  # Evening temperature in °C
    nightTemp = models.FloatField()  # Night temperature in °C
    comments = models.TextField(blank=True, null=True)  # Optional comments
    actionTaken = models.TextField(blank=True, null=True)  # Optional actions taken
    is_deleted = models.BooleanField(default=False)  # Field for soft delete

    # history = HistoricalRecords()  # Track changes

    def __str__(self):
        return f'Cold room {self.coldRoomId} record on {self.date}'
    
#Employee Management Model
class Employee(models.Model):
    employee_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # UUID for Employee
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)  # ForeignKey relationship to Farm
    fullName = models.CharField(max_length=255)  # Full name of the employee
    jobTitle = models.CharField(max_length=255)  # Employee's job title
    department = models.CharField(max_length=255)  # Department where the employee works
    contact = models.CharField(max_length=15)  # Contact number
    email = models.EmailField()  # Email address
    location = models.CharField(max_length=255, blank=True, null=True)  # Optional location
    startDate = models.DateField(blank=True, null=True)  # Optional start date of employment
    is_deleted = models.BooleanField(default=False)  # Field for soft delete

    # history = HistoricalRecords()  # Track changes

    def __str__(self):
        return f'Employee {self.fullName}'
    
#Harvest Group Management Model
class HarvestGroup(models.Model):
    group_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # UUID for Harvest Group
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)  # ForeignKey relationship to Farm
    groupName = models.CharField(max_length=255)  # Name of the group
    farmName = models.CharField(max_length=255)  # Farm where the harvest took place
    harvestDate = models.DateField()  # Date of the harvest
    totalHours = models.IntegerField()  # Total hours worked
    totalPay = models.CharField(max_length=255)  # Total pay for the group
    harvestYield = models.CharField(max_length=255)  # Harvest yield in kilograms or another unit
    netProfit = models.CharField(max_length=255)  # Net profit earned
    is_deleted = models.BooleanField(default=False)  # Field for soft delete

    # history = HistoricalRecords()  # Track changes

    def __str__(self):
        return f'Harvest group {self.groupName}'
    
#surplus spray mix disposal model
class SurplusSprayMixDisposal(models.Model):
    surplusmix_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # UUID for Surplus Mix Disposal
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)  # ForeignKey relationship to Farm
    productName = models.CharField(max_length=255)  # Name of the product (e.g., Herbicide X)
    dateOfApplication = models.DateField()  # Date of application
    block = models.CharField(max_length=255)  # Block where the product was applied
    quantityDisposed = models.DecimalField(max_digits=10, decimal_places=2)  # Amount disposed in liters
    operatorName = models.CharField(max_length=255)  # Name of the operator
    authorizedBy = models.CharField(max_length=255)  # Authorized person
    notes = models.TextField(blank=True, null=True)  # Optional notes
    is_deleted = models.BooleanField(default=False)  # Field for soft delete

    # history = HistoricalRecords()  # Track changes

    def __str__(self):
        return f'Surplus spray mix for {self.productName}'
    
#equipment management model
class EquipmentManagement(models.Model):
    equipment_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # UUID for Equipment Management
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)  # ForeignKey relationship to Farm
    sprayOperator = models.CharField(max_length=255)  # Spray operator
    equipmentSerialNumber = models.CharField(max_length=255)  # Equipment serial number
    equipmentCleaned = models.BooleanField(default=False)  # Indicates if the equipment was cleaned
    equipmentCondition = models.CharField(max_length=255)  # Equipment condition
    PPECondition = models.CharField(max_length=255)  # PPE condition
    PPECleaned = models.BooleanField(default=False)  # Indicates if the PPE was cleaned
    checkedBy = models.CharField(max_length=255)  # Person who checked the equipment
    is_deleted = models.BooleanField(default=False)  # Field for soft delete

    # history = HistoricalRecords()  # Track changes

    def __str__(self):
        return f'Equipment record for {self.equipmentSerialNumber}'
    
#environmental record model
class EnvironmentalRecord(models.Model):
    environmental_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # UUID for Environmental Record
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)  # ForeignKey relationship to Farm
    date = models.DateField()  # Date of the record
    environmentalFactor = models.CharField(max_length=255)  # Environmental factor (e.g., Energy Use)
    measurement = models.CharField(max_length=255)  # Value of the measurement
    unit = models.CharField(max_length=50)  # Unit of the measurement
    location = models.CharField(max_length=255)  # Location of measurement
    responsiblePerson = models.CharField(max_length=255)  # Responsible person
    targetBenchmark = models.CharField(max_length=255)  # Target benchmark for compliance
    complianceStatus = models.CharField(max_length=50)  # Whether target was met or not
    notes = models.TextField(blank=True, null=True)  # Optional notes
    actionTaken = models.TextField(blank=True, null=True)  # Optional actions taken
    is_deleted = models.BooleanField(default=False)  # Field for soft delete

    # history = HistoricalRecords()  # Track changes

    def __str__(self):
        return f'Environmental record for {self.environmentalFactor} on {self.date}'
    
#Accident Incident Record Model
class AccidentIncidentRecord(models.Model):
    safety_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # UUID for Safety
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)  # ForeignKey to Farm
    safetyType = models.CharField(max_length=255)  # Safety type (e.g., Inspection, Incident)
    inspectorName = models.CharField(max_length=255)  # Inspector or auditor name
    date = models.DateField()  # Date of safety event
    incidentType = models.CharField(max_length=255)  # Type of safety incident (e.g., Fire, Injury)
    status = models.CharField(max_length=255)  # Status (e.g., Resolved, Pending)
    is_deleted = models.BooleanField(default=False)  # Field for soft delete
    # history = HistoricalRecords()  # Track changes

    def __str__(self):
        return f'{self.safetyType} - {self.incidentType}'
    
#Work Planning Task Model
class WorkPlanningTask(models.Model):
    wp_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # UUID for Work Planning
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)  # ForeignKey to Farm
    title = models.CharField(max_length=255)  # Title or description of the task
    department = models.CharField(max_length=255)  # Department responsible
    assignedTo = models.CharField(max_length=255)  # Person assigned to complete the task
    start = models.DateField()  # Start date of the task
    deadline = models.DateField()  # Deadline for task completion
    status = models.CharField(max_length=255)  # Status (e.g., Completed, Pending)
    notes = models.TextField(blank=True, null=True)  # Optional notes
    is_deleted = models.BooleanField(default=False)  # Field for soft delete
    # history = HistoricalRecords()  # Track changes

    def __str__(self):
        return f'{self.title} - {self.status}'
    
#Training record task model
class TrainingRecord(models.Model):
    training_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # UUID for Training
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)  # ForeignKey to Farm
    trainingTitle = models.CharField(max_length=255)  # Training title
    trainerName = models.CharField(max_length=255)  # Name of the trainer
    date = models.DateField()  # Date of the training session
    farmName = models.CharField(max_length=255)  # Name of the farm or farmer
    topic = models.CharField(max_length=255)  # Topic covered
    duration = models.CharField(max_length=255)  # Duration of the training
    summary = models.TextField()  # Brief description
    materialsProvided = models.JSONField()  # List of training materials (e.g., ["Guide on Pest Control"])
    attendance = models.IntegerField()  # Number of participants
    trainerNotes = models.TextField(blank=True, null=True)  # Optional trainer notes
    is_deleted = models.BooleanField(default=False)  # Field for soft delete
    # history = HistoricalRecords()  # Track changes

    def __str__(self):
        return f'{self.trainingTitle} - {self.trainerName}'
    
# spray mix disposal report model
class SprayMixDisposalReport(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    block = models.CharField(max_length=255)
    dateRangeStart = models.DateField()
    dateRangeEnd = models.DateField()
    details = models.TextField()

    def __str__(self):
        return f'Spray Mix Disposal Report - {self.block}'

# Incident Report Model
class IncidentReport(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    block = models.CharField(max_length=255)
    date = models.DateField()
    incidentType = models.CharField(max_length=255)

    def __str__(self):
        return f'Incident Report - {self.incidentType}'
    
# Work Plan Report Model
class WorkPlanReport(models.Model):
    department = models.CharField(max_length=255)
    taskStatus = models.CharField(max_length=255)
    startDate = models.DateField()
    endDate = models.DateField()

    def __str__(self):
        return f'Work Plan Report - {self.department}'

# Inventory By Crop Report Model
class InventoryByCropReport(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    cropVariety = models.CharField(max_length=255)
    fertilizerUsed = models.CharField(max_length=255)
    pesticideUsed = models.CharField(max_length=255)

    def __str__(self):
        return f'Inventory Report for {self.cropVariety}'

# Water Usage By Block Report Model
class WaterUsageByBlockReport(models.Model):
    block = models.CharField(max_length=255)
    waterUsage = models.FloatField()
    dateRangeStart = models.DateField()
    dateRangeEnd = models.DateField()

    def __str__(self):
        return f'Water Usage Report - {self.block}'

# Disease Symptom Frequency Report Model
class DiseaseSymptomFrequencyReport(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    cropVariety = models.CharField(max_length=255)
    symptom = models.CharField(max_length=255)
    frequency = models.IntegerField()

    def __str__(self):
        return f'Disease Symptom Frequency - {self.cropVariety}'

# Summary Report Model
class SummaryReport(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    summaryDetails = models.TextField()

    def __str__(self):
        return f'Summary Report for {self.farm}'




# Create your models here.

