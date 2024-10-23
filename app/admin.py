from django.contrib import admin
from .models import (Farmer, Company, Farm, OTP, ScoutingRecord, PlantingRecord, IrrigationRecord, ProductionRecord, 
                     HarvestRecord, FertilizerApplication, PesticideApplication, PesticideProduct, ColdRoomTemperature, 
                     Employee, HarvestGroup, SurplusSprayMixDisposal, EquipmentManagement, EnvironmentalRecord, 
                     AccidentIncidentRecord, WorkPlanningTask, TrainingRecord, SprayMixDisposalReport, IncidentReport, 
                     WorkPlanReport, InventoryByCropReport, WaterUsageByBlockReport, DiseaseSymptomFrequencyReport, 
                     SummaryReport)


# admin.site.register(Farmer)
# admin.site.register(Company)
# admin.site.register(Farm)

@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('fullName', 'farmer_id', 'email', 'phoneNumber', 'country')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('companyName', 'company_id', 'email', 'phoneNumber', 'country')

@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = ('owner', 'totalFarmArea', 'numberOfBlocks', 'mainCropsGrown', 'farmingMethods', 'soilType', 'irrigationSystem', 'averageAnnualRainfall', 'majorChallengesFaced', 'farmEquipmentOwned', 'farmLatitudeCoordinates', 'farmLongitudeCoordinates')
# Register your models here.

# Scouting Record Admin
@admin.register(ScoutingRecord)
class ScoutingRecordAdmin(admin.ModelAdmin):
    list_display = ('scouting_id', 'farm', 'block', 'cropType', 'pesticideUsed')

# Planting Record Admin
@admin.register(PlantingRecord)
class PlantingRecordAdmin(admin.ModelAdmin):
    list_display = ('planting_id', 'farm', 'block', 'cropType', 'variety', 'plantingDate')

# Irrigation Record Admin
@admin.register(IrrigationRecord)
class IrrigationRecordAdmin(admin.ModelAdmin):
    list_display = ('irrigation_id', 'farm', 'pumpDischargeRate', 'block', 'amountOfWaterUsed')

# Production Record Admin
@admin.register(ProductionRecord)
class ProductionRecordAdmin(admin.ModelAdmin):
    list_display = ('production_id', 'farm', 'productionNumber', 'productionDate', 'crop', 'yieldPerSquareMeter')

# Harvest Record Admin
@admin.register(HarvestRecord)
class HarvestRecordAdmin(admin.ModelAdmin):
    list_display = ('harvest_id', 'farm', 'harvestNumber', 'block', 'quantityHarvested', 'loss')

# Fertilizer Application Admin
@admin.register(FertilizerApplication)
class FertilizerApplicationAdmin(admin.ModelAdmin):
    list_display = ('fertilizerapp_id', 'farm', 'productionNumber', 'dateOfApplication', 'NPKComposition', 'quantityApplied')

# Pesticide Application Admin
@admin.register(PesticideApplication)
class PesticideApplicationAdmin(admin.ModelAdmin):
    list_display = ('pesticideapp_id', 'farm', 'recordNumber', 'dateOfApplication', 'pppUsed', 'quantityUsed')

# Pesticide Product Admin
@admin.register(PesticideProduct)
class PesticideProductAdmin(admin.ModelAdmin):
    list_display = ('pesticide_id', 'farm', 'tradeName', 'activeIngredient', 'classification', 'targetPest')

# Cold Room Temperature Admin
@admin.register(ColdRoomTemperature)
class ColdRoomTemperatureAdmin(admin.ModelAdmin):
    list_display = ('coldroom_id', 'farm', 'coldRoomId', 'date', 'morningTemp', 'eveningTemp')

# Employee Admin
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'farm', 'fullName', 'jobTitle', 'department')

# Harvest Group Admin
@admin.register(HarvestGroup)
class HarvestGroupAdmin(admin.ModelAdmin):
    list_display = ('group_id', 'farm', 'groupName', 'harvestDate', 'totalHours')

# Surplus Spray Mix Disposal Admin
@admin.register(SurplusSprayMixDisposal)
class SurplusSprayMixDisposalAdmin(admin.ModelAdmin):
    list_display = ('surplusmix_id', 'farm', 'productName', 'quantityDisposed')

# Equipment Management Admin
@admin.register(EquipmentManagement)
class EquipmentManagementAdmin(admin.ModelAdmin):
    list_display = ('equipment_id', 'farm', 'equipmentSerialNumber', 'sprayOperator', 'equipmentCleaned')

# Environmental Record Admin
@admin.register(EnvironmentalRecord)
class EnvironmentalRecordAdmin(admin.ModelAdmin):
    list_display = ('environmental_id', 'farm', 'date', 'environmentalFactor', 'measurement')

# Accident/Incident Record Admin
@admin.register(AccidentIncidentRecord)
class AccidentIncidentRecordAdmin(admin.ModelAdmin):
    list_display = ('safety_id', 'farm', 'safetyType', 'incidentType', 'status')

# Work Planning Task Admin
@admin.register(WorkPlanningTask)
class WorkPlanningTaskAdmin(admin.ModelAdmin):
    list_display = ('wp_id', 'farm', 'title', 'department', 'status', 'deadline')

# Training Record Admin
@admin.register(TrainingRecord)
class TrainingRecordAdmin(admin.ModelAdmin):
    list_display = ('training_id', 'farm', 'trainingTitle', 'trainerName', 'date', 'attendance')

# Spray Mix Disposal Report Admin
@admin.register(SprayMixDisposalReport)
class SprayMixDisposalReportAdmin(admin.ModelAdmin):
    list_display = ('farm', 'block', 'dateRangeStart', 'dateRangeEnd')

# Incident Report Admin
@admin.register(IncidentReport)
class IncidentReportAdmin(admin.ModelAdmin):
    list_display = ('farm', 'block', 'date', 'incidentType')

# Work Plan Report Admin
@admin.register(WorkPlanReport)
class WorkPlanReportAdmin(admin.ModelAdmin):
    list_display = ('department', 'taskStatus', 'startDate', 'endDate')

# Inventory By Crop Report Admin
@admin.register(InventoryByCropReport)
class InventoryByCropReportAdmin(admin.ModelAdmin):
    list_display = ('farm', 'cropVariety', 'fertilizerUsed', 'pesticideUsed')

# Water Usage By Block Report Admin
@admin.register(WaterUsageByBlockReport)
class WaterUsageByBlockReportAdmin(admin.ModelAdmin):
    list_display = ('block', 'waterUsage', 'dateRangeStart', 'dateRangeEnd')

# Disease Symptom Frequency Report Admin
@admin.register(DiseaseSymptomFrequencyReport)
class DiseaseSymptomFrequencyReportAdmin(admin.ModelAdmin):
    list_display = ('farm', 'cropVariety', 'symptom', 'frequency')

# Summary Report Admin
@admin.register(SummaryReport)
class SummaryReportAdmin(admin.ModelAdmin):
    list_display = ('farm', 'summaryDetails')

