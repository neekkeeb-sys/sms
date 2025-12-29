from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('student/add/', views.add_student, name='add_student'),
    path('attendance/add/', views.add_attendance, name='add_attendance'),
    path('marks/add/', views.add_marks, name='add_marks'),
    path('notice/add/', views.add_notice, name='add_notice'),

    # optional edit/delete examples
    path('student/edit/<int:pk>/', views.edit_student, name='edit_student'),
    path('student/delete/<int:pk>/', views.delete_student, name='delete_student'),
]
