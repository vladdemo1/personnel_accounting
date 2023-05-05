from django.db import models

# Create your models here.


class Unit(models.Model):
    """
    Model about worker and manager
    """

    manager = models.BooleanField(default=False, verbose_name="Менеджер")
    worker = models.BooleanField(default=True, verbose_name="Рабочий")

    first_name = models.CharField(max_length=255, verbose_name="Имя")
    middle_name = models.CharField(max_length=255, verbose_name="Отчество")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия")
    login = models.CharField(max_length=255, verbose_name="Логин")
    password = models.CharField(max_length=255, verbose_name="Пароль")
    personnel_number = models.PositiveIntegerField(default=1)
    payroll_number = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return str(self.id)
    

    class Meta:
        verbose_name_plural = 'Сотрудник'
