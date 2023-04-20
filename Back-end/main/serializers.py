from rest_framework import serializers
from .models import Teacher, Classroom

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        # Model that will be used.
        model = Teacher

        # Database fields
        fields = ['id', 'first_name', 'last_name', 'mail']


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom # Model that will be used.
        fields = ['year', 'letter'] # Database fields.