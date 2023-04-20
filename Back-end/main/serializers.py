from rest_framework import serializers
from .models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        # Model that will be used.
        model = Teacher

        # Database fields
        fields = ['id', 'first_name', 'last_name', 'mail']