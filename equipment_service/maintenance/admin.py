from django.contrib import admin
from .models import Equipment, MaintenanceNorm, MaintenancePlan

admin.site.register(Equipment)
admin.site.register(MaintenanceNorm)
admin.site.register(MaintenancePlan)
