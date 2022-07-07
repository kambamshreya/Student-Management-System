from django.db import models

# Create your models here.
class Members(models.Model):
    student_name=models.CharField(max_length=255)
    roll_no=models.CharField(max_length=255)
    branch=models.CharField(max_length=255)