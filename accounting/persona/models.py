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

    salary_index = models.FloatField(verbose_name="Индекс зарплаты", default=1.0)

    def __str__(self) -> str:
        return str(self.id)
    

    class Meta:
        verbose_name_plural = 'Сотрудник'


class Attendance(models.Model):
    """
    Model about attendance personal
    """

    STATUS_ARRIVED_TO_WORK = "arrived"
    STATUS_BACK_FROM_WORK = "gone"

    STATUS_VACATION = "vacation"
    STATUS_BACK_FROM_VACATION = "back"

    STATUS_CHOISES = (
        (STATUS_ARRIVED_TO_WORK, "Пришел на работу"),
        (STATUS_BACK_FROM_WORK, "Ушел с работы"),
        (STATUS_VACATION, "В отпуске"),
        (STATUS_BACK_FROM_VACATION, "Вернулся с отпуска"),
    )

    user = models.ForeignKey(Unit, verbose_name="Работник", on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now=True, verbose_name="Дата создания", null=True, blank=True)

    status = models.CharField(max_length=100, verbose_name="Статус работника", choices=STATUS_CHOISES, default=STATUS_ARRIVED_TO_WORK)


    def __str__(self) -> str:
        return str(self.id)
    

    class Meta:
        verbose_name_plural = 'Статус сотрудника'
