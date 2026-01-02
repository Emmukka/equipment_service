from django.urls import path
from .views import equipment_list, plan_list, generate_plan_view, dashboard

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('equipment/', equipment_list, name='equipment_list'),
    path('plans/', plan_list, name='plan_list'),
    path('plans/<int:equipment_id>/', plan_list),
    path('generate/<int:equipment_id>/', generate_plan_view, name='generate_plan'),
]