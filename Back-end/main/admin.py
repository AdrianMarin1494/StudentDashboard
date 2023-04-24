from django.contrib import admin
from .models import Teacher, Classroom, Student, Subject, ClassAssignment, Timetable, Grade

# Register your models here.

admin.site.register([Teacher, Classroom, Student, Subject, ClassAssignment, Timetable, Grade])
