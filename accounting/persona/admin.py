from django.contrib import admin
from .models import Unit, Attendance

# Register your models here.

admin.site.register(Unit)


class AttendanceAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)


admin.site.register(Attendance,AttendanceAdmin)
