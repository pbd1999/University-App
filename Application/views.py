from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import CreateView, View, DetailView, TemplateView
from .models import Department, Student, Course
from django import forms

class StudentCreateView(CreateView):
    model = Student
    fields = ('ID', 'firstName', 'lastName', 'dept_name', 'tot_cred', 'stud_img')

class StudentDetailView(DetailView):
    model = Student
    
def StudentAllView(request):
    students = Student.objects.all()
    return render(request, 'Application/student_all_view.html', {'students': students})
    
class DepartmentCreateView(CreateView):
    model = Department
    fields = ('dept_name', 'building', 'budget')

class DepartmentDetailView(DetailView):
    model = Department

def DepartmentAllView(request):
    departments = Department.objects.all()
    return render(request, 'Application/department_all_view.html', {'departments': departments})

class CourseCreateView(CreateView):
    model = Course
    fields = ('course_id', 'title', 'dept_name', 'credits')

class CourseDetailView(DetailView):
    model = Course

def CourseAllView(request):
    courses = Course.objects.all()
    return render(request, 'Application/course_all_view.html', {'courses': courses})

def allViews(request):
    # students = Student.objects.all()
    return render(request, 'Application/all-views.html', {})

def IndexView(request):
    return render(request, 'static/index.html', {'name': 'ROHIT_CHOUGULE'})
