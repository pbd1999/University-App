from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime
from django.shortcuts import render
from django.urls import reverse
from django.conf.urls import include, url
from django.conf import settings
from django.core.files.storage import FileSystemStorage

class Department(models.Model):
    dept_name = models.CharField(max_length=200, primary_key=True)
    building = models.CharField(max_length=200)
    budget = models.CharField(max_length=200)
    def get(self):
        return self.clean()
    def get_absolute_url(self):
        return reverse('Application:department-detail', kwargs={'pk': self.pk})
    
class Course(models.Model):
    course_id = models.CharField(unique=True, max_length=200)
    title = models.CharField(max_length=200)
    dept_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    credits = models.IntegerField()
    def get(self):
        return self.clean()
    def get_absolute_url(self):
        return reverse('Application:course-detail', kwargs={'pk': self.pk})
    
class Student(models.Model):
    ID = models.CharField(max_length=200, primary_key=True)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    dept_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    tot_cred = models.IntegerField()
    stud_img = models.ImageField(upload_to='media/')
    def get(self):
        return self.clean()
    def get_absolute_url(self):
        return reverse('Application:student-detail', kwargs={'pk': self.pk})





