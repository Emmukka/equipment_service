from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipment, MaintenancePlan, MaintenanceNorm
from .utils import generate_plan
from collections import defaultdict
from calendar import month_name

def equipment_list(request):
    equipments = Equipment.objects.all()
    return render(request, 'maintenance/equipment_list.html', {'equipments': equipments})

def plan_list(request, equipment_id=None):
    if equipment_id:
        plans = MaintenancePlan.objects.filter(equipment__id=equipment_id).order_by('planned_date')
    else:
        plans = MaintenancePlan.objects.order_by('planned_date')
    
    calendar = defaultdict(list)
    for p in plans:
        month_year = f"{month_name[p.planned_date.month]} {p.planned_date.year}"
        calendar[month_year].append(p)
    
    return render(
        request,
        'maintenance/plan_list.html',
        {'calendar': dict(calendar)}
    )

def generate_plan_view(request, equipment_id):
    equipment = get_object_or_404(Equipment, id=equipment_id)
    norm = get_object_or_404(MaintenanceNorm, equipment=equipment)

    generate_plan(equipment, norm, months=12)

    return redirect(f'/plans/{equipment.id}/')

def dashboard(request):
    equipments = Equipment.objects.all()
    plans = MaintenancePlan.objects.order_by('planned_date')[:15]

    return render(
        request,
        'maintenance/dashboard.html',
        {
            'equipments': equipments,
            'plans': plans
        }
    )

