"""
URL configuration for authentication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include
from django.contrib import admin
from app import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="Agrisense API",
      default_version='v1',
      description="API documentation for Agrisense",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="your-email@example.com"),
      license=openapi.License(name="BSD License"),
   ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Swagger URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.yaml', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    # Registration APIs
    path('register/farmer', views.register_farmer, name='register_farmer'),
    path('register/farm', views.register_farm, name='register_farm'),
    path('register/company', views.register_company, name='register_company'),

    # JWT Token APIs
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # OTP APIs
    path('otp/request', views.request_otp, name='request_otp'),
    path('otp/verify', views.verify_otp, name='verify_otp'),
    path('otp/resend', views.resend_otp, name='resend_otp'),

    # Signin API
    path('api/signin', views.signin, name='signin'),

    # ScoutingRecord URLs
    path('scouting-records', views.add_scouting_record, name='add_scouting_record'),
    path('scouting-records/update/<uuid:id>', views.update_scouting_record, name='update_scouting_record'),
    path('scouting-records/delete/<uuid:id>', views.delete_scouting_record, name='delete_scouting_record'),

    # IrrigationRecord URLs
    path('irrigation-records', views.add_irrigation_record, name='add_irrigation_record'),
    path('irrigation-records/update/<uuid:id>', views.update_irrigation_record, name='update_irrigation_record'),
    path('irrigation-records/delete/<uuid:id>', views.delete_irrigation_record, name='delete_irrigation_record'),

    # PlantingRecord URLs
    path('planting-records', views.add_planting_record, name='add_planting_record'),
    path('planting-records/update/<uuid:id>', views.update_planting_record, name='update_planting_record'),
    path('planting-records/delete/<uuid:id>', views.delete_planting_record, name='delete_planting_record'),

    # HarvestRecord URLs
    path('harvest-records', views.add_harvest_record, name='add_harvest_record'),
    path('harvest-records/update/<uuid:id>', views.update_harvest_record, name='update_harvest_record'),
    path('harvest-records/delete/<uuid:id>', views.delete_harvest_record, name='delete_harvest_record'),

    # ProductionRecord URLs
    path('production-records', views.add_production_record, name='add_production_record'),
    path('production-records/update/<uuid:id>', views.update_production_record, name='update_production_record'),
    path('production-records/delete/<uuid:id>', views.delete_production_record, name='delete_production_record'),

    # Fertilizer Application URLs
    path('fertilizer-records', views.add_fertilizer_record, name='add_fertilizer_record'),
    path('fertilizer-records/update/<uuid:id>', views.update_fertilizer_record, name='update_fertilizer_record'),
    path('fertilizer-records/delete/<uuid:id>', views.delete_fertilizer_record, name='delete_fertilizer_record'),

    # Pesticide Application URLs
    path('pesticide-records', views.add_pesticide_record, name='add_pesticide_record'),
    path('pesticide-records/update/<uuid:id>', views.update_pesticide_record, name='update_pesticide_record'),
    path('pesticide-records/delete/<uuid:id>', views.delete_pesticide_record, name='delete_pesticide_record'),

    # Pesticide Product Usage URLs
    path('pesticides', views.add_pesticide_product, name='add_pesticide_product'),
    path('pesticides/update/<uuid:id>', views.update_pesticide_product, name='update_pesticide_product'),
    path('pesticides/delete/<uuid:id>', views.delete_pesticide_product, name='delete_pesticide_product'),

    # Cold Room URLs
    path('coldroom', views.add_cold_room_record, name='add_cold_room_record'),
    path('coldroom/update/<uuid:id>', views.update_cold_room_record, name='update_cold_room_record'),
    path('coldroom/delete/<uuid:id>', views.delete_cold_room_record, name='delete_cold_room_record'),

    # Employee Management URLs
    path('employees', views.add_employee_record, name='add_employee_record'),
    path('employees/update/<uuid:id>', views.update_employee_record, name='update_employee_record'),
    path('employees/delete/<uuid:id>', views.delete_employee_record, name='delete_employee_record'),

    # Harvest Groups Management URLs
    path('harvest-groups', views.add_harvest_group_record, name='add_harvest_group_record'),
    path('harvest-groups/update/<uuid:id>', views.update_harvest_group_record, name='update_harvest_group_record'),
    path('harvest-groups/delete/<uuid:id>', views.delete_harvest_group_record, name='delete_harvest_group_record'),

    # Surplus Spray Mix Disposal URLs
    path('surplus-spraymix', views.add_spray_mix_disposal, name='add_spray_mix_disposal'),
    path('surplus-spraymix/update/<uuid:id>', views.update_spray_mix_disposal, name='update_spray_mix_disposal'),
    path('surplus-spraymix/delete/<uuid:id>', views.delete_spray_mix_disposal, name='delete_spray_mix_disposal'),

    # Equipment Management URLs
    path('equipment-records', views.add_equipment_record, name='add_equipment_record'),
    path('equipment-records/update/<uuid:id>', views.update_equipment_record, name='update_equipment_record'),
    path('equipment-records/delete/<uuid:id>', views.delete_equipment_record, name='delete_equipment_record'),

    # Environmental Record URLs
    path('environment-records', views.add_environmental_record, name='add_environmental_record'),
    path('environment-records/update/<uuid:id>', views.update_environmental_record, name='update_environmental_record'),
    path('environment-records/delete/<uuid:id>', views.delete_environmental_record, name='delete_environmental_record'),

    # Accident/Incident Record URLs
    path('accidents', views.add_accident_record, name='add_accident_record'),
    path('accidents/update/<uuid:id>', views.update_accident_record, name='update_accident_record'),
    path('accidents/delete/<uuid:id>', views.delete_accident_record, name='delete_accident_record'),

    # Work Planning Task URLs
    path('workplanning', views.add_workplanning_task, name='add_workplanning_task'),
    path('workplanning/update/<uuid:id>', views.update_workplanning_task, name='update_workplanning_task'),
    path('workplanning/delete/<uuid:id>', views.delete_workplanning_task, name='delete_workplanning_task'),

    # Training Record URLs
    path('trainings', views.add_training_record, name='add_training_record'),
    path('trainings/update/<uuid:id>', views.update_training_record, name='update_training_record'),
    path('trainings/delete/<uuid:id>', views.delete_training_record, name='delete_training_record'),

    # Spray Mix Disposal Report URLs
    path('reports/sprayMixDisposal', views.get_spray_mix_disposal_report, name='get_spray_mix_disposal_report'),

    # Incident Reporting Report URLs
    path('reports/incidents', views.get_incident_reports, name='get_incident_reports'),

    # Work Plan Report URLs
    path('reports/workPlans', views.get_work_plan_reports, name='get_work_plan_reports'),

    # Inventory Report URLs
    path('reports/inventoryByCrop', views.get_inventory_by_crop_report, name='get_inventory_by_crop_report'),

    # Water Usage Report URLs
    path('reports/waterUsageByBlock', views.get_water_usage_report, name='get_water_usage_report'),

    # Disease Symptom Frequency Report URLs
    path('reports/diseaseSymptoms', views.get_disease_symptom_frequency_report, name='get_disease_symptom_frequency_report'),

    # General Report Summary URLs
    path('reports/summary', views.get_report_summary, name='get_report_summary'),

    # Include the app's URLs
    path('api/', include('app.urls')),  # Include your app's URLs if there are additional ones

]