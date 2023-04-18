from django.contrib import admin
from .models import Teacher, Class, Student, Subject

# Register your models here.

admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Subject)