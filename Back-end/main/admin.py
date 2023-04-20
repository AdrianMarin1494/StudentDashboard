from django.contrib import admin
from .models import Teacher, Classroom, Student, Subject, ClassAsignment, Timetable, Grade

# Register your models here.

admin.site.register(Teacher)
admin.site.register(Classroom)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(ClassAsignment)
admin.site.register(Timetable)
admin.site.register(Grade)