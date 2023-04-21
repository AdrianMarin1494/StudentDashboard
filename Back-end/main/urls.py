from django.urls import path
from . import views

urlpatterns = [
    path('teachers/', views.teachers, name='teachers'),
    path('teachers/<int:id>', views.teacher_info, name='teacher_info'),
    path('classrooms/', views.classrooms, name='classrooms'),
    path('classrooms/<int:id>', views.classroom_info, name="classroom_info"),
    path('subjects/', views.subject, name='subjects'),
    path('subjects/<int:id>', views.subject_info, name='subject_info'),
]