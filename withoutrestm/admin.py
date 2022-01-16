from django.contrib import admin

# Register your models here.
from withoutrestm.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email_address', 'country']


admin.site.register(Employee, EmployeeAdmin)
