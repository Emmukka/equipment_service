from datetime import date
from dateutil.relativedelta import relativedelta
from .models import MaintenancePlan

def generate_plan(equipment, norm, months=12):
    """
    Автомат формирование плана ТО / ТР / КР
    на заданное количество месяцев
    """
    start_date = equipment.start_date
    end_date = start_date + relativedelta(months=months)

    current_date = start_date
    while current_date <= end_date:
        # ТО
        if norm.to_period > 0:
            MaintenancePlan.objects.get_or_create(
                equipment=equipment,
                work_type='ТО',
                planned_date=current_date
            )

        # ТР
        if norm.tr_period > 0 and (
            (current_date.month - start_date.month) % norm.tr_period == 0
        ):
            MaintenancePlan.objects.get_or_create(
                equipment=equipment,
                work_type='ТР',
                planned_date=current_date
            )

        # КР
        if norm.kr_period > 0 and (
            (current_date.month - start_date.month) % norm.kr_period == 0
        ):
            MaintenancePlan.objects.get_or_create(
                equipment=equipment,
                work_type='КР',
                planned_date=current_date
            )

        current_date += relativedelta(months=norm.to_period)
