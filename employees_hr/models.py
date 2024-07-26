from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('superadmin', 'Super Admin'),
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('user', 'User'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')


class PerformanceEvaluation(models.Model):
    employee_name = models.CharField(max_length=100)
    evaluation_date = models.DateField()
    score = models.IntegerField()
    comments = models.TextField()

    def __str__(self):
        return f'{self.employee_name} - {self.evaluation_date}'
    
class Feature(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

class Payroll(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_date = models.DateField()

    def __str__(self):
        return f"{self.employee_name} - {self.pay_date}"
    
class Attendance(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.name    
    
class LeaveRequest(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    return_date = models.DateField()
    reason = models.TextField()

    def __str__(self):
        return self.name    
    
  
class Document(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 

class Employee(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, null=True)
    position = models.CharField(max_length=100, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return f"{self.name}"
