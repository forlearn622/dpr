from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_name=models.CharField(max_length=30)
    emp_age=models.IntegerField()
    salary=models.IntegerField()
    city=models.CharField(max_length=30)
    emp_gender=models.CharField(max_length=10)
