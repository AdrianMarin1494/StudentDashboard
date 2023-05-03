from django.urls import path
from . import views

urlpatterns = [
    path('teachers/', views.TeachersList.as_view(), name='teachers'),
    path('teachers/<int:pk>', views.TeacherDetails.as_view(), name='teacher_info'),
    path('classrooms/', views.ClassroomsList.as_view(), name='classrooms'),
    path('classrooms/<int:pk>', views.ClassroomDetails.as_view(), name="classroom_info"),
    path('subjects/', views.SubjectsList.as_view(), name='subjects'),
    path('subjects/<int:pk>', views.SubjectDetails.as_view(), name='subject_info'),
    path('students/', views.StudentsList.as_view(), name='subjects'),
    path('students/<int:pk>', views.StudentDetails.as_view(), name='subject_info'),
    path('class-assignment/', views.ClassAssignmentsList.as_view(), name='class-assignment'),
    path('class-assignment/<int:pk>', views.ClassAssignmentDetails.as_view(), name='class-assignment_info'),
    path('timetable/', views.TimetablesList.as_view(), name='timetable'),
    path('timetable/<int:pk>', views.TimetableDetails.as_view(), name='timetable_info'),
    path('grades/', views.GradesList.as_view(), name='grades'),
    path('grades/<int:pk>', views.GradeDetails.as_view(), name='grades_info'),
]