from django.urls import path
from . import views

urlpatterns = [
    path('teachers/', views.teachers, name='teachers'),
    path('teachers/<int:id>', views.teacher_info, name='teacher_info'),
    path('classrooms/', views.classrooms, name='classrooms'),
    path('classrooms/<int:id>', views.classroom_info, name="classroom_info"),
    path('subjects/', views.subject, name='subjects'),
    path('subjects/<int:id>', views.subject_info, name='subject_info'),
    path('students/', views.student, name='subjects'),
    path('students/<int:id>', views.student_info, name='subject_info'),
    path('class-assignment/', views.class_assignment, name='class-assignment'),
    path('class-assignment/<int:id>', views.class_assignment_info, name='class-assignment_info'),
    path('timetable/', views.timetable, name='timetable'),
    path('timetable/<int:id>', views.timetable_info, name='timetable_info'),
    path('grades/', views.grade, name='grades'),
    path('grades/<int:id>', views.grade_info, name='grades_info'),
]