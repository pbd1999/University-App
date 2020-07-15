from django.urls import path, include
from . import views
app_name = 'Application'

urlpatterns = [

    path('', views.allViews, name = 'all-views'),
    path('department/add/', views.DepartmentCreateView.as_view(), name = 'department-add'),
    path('department/<str:pk>/', views.DepartmentDetailView.as_view(), name = 'department-detail'),
    path('department/', views.DepartmentAllView, name = 'department'),
    path('student/add/', views.StudentCreateView.as_view(), name = 'student-add'),
    path('student/<str:pk>/', views.StudentDetailView.as_view(), name = 'student-detail'),
    path('student/',views.StudentAllView, name = 'student'),
    path('accounts/', include('django.contrib.auth.urls'), name = 'accounts'),
    path('course/add/', views.CourseCreateView.as_view(), name='course-add'),
    path('course/<str:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('course/', views.CourseAllView, name='course'),

]