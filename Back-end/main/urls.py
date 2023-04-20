from django.urls import path
from . import views

urlpatterns = [
    path('teachers/', views.teachers, name='teachers'),
    path('teachers/<int:id>', views.teacher_info, name='teacher_info'),
    path('classrooms/', views.classrooms, name='classrooms')
]