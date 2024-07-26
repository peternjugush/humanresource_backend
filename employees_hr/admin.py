from django.contrib import admin
from employees_hr.models import *
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Payroll)