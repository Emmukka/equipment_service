from django.db import models

class Equipment(models.Model):
    name = models.CharField("Название оборудования", max_length=100)
    equipment_type = models.CharField("Тип оборудования", max_length=100)
    manufacturer = models.CharField("Производитель", max_length=100)
    start_date = models.DateField("Дата ввода в эксплуатацию")

    def __str__(self):
        return self.name


class MaintenanceNorm(models.Model):
    equipment = models.OneToOneField(
        Equipment,
        on_delete=models.CASCADE,
        verbose_name="Оборудования"
    )
    to_period = models.IntegerField("ТО (мес.)")
    tr_period = models.IntegerField("ТР (мес.)")
    kr_period = models.IntegerField("КР (мес.)")

    def __str__(self):
        return f"Нормативы для {self.equipment}"


class MaintenancePlan(models.Model):
    WORK_TYPES = [
        ('ТО', 'Технический осмотр'),
        ('ТР', 'Технический ремонт'),
        ('КР', 'Капитальный ремонт'),
    ]

    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    work_type = models.CharField(max_length=2, choices=WORK_TYPES)
    planned_date = models.DateField("Плановая дата")
    status = models.CharField("Статус", max_length=20, default="Запланировано")

    def __str__(self):
        return f"{self.work_type} - {self.equipment}"

