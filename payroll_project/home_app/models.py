from django.db import models


class admin_tb(models.Model) :
    username = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)

class employee_tb(models.Model) :
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=100)
    emp_job = models.CharField(max_length=100)
    emp_role = models.CharField(max_length=100)
    emp_salary = models.IntegerField()
