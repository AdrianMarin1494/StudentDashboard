from rest_framework import serializers
from .models import Teacher, Classroom, Subject, Student, ClassAsignment, Timetable, Grade

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        # Model that will be used.
        model = Teacher

        # Database fields
        fields = '__all__'



class ClassroomSerializer(serializers.ModelSerializer):
    # To create a new field you need to name it <given_name>, define a function with "get_<given_name> and add it to fields list."
    # Documentation: https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
    # Tutorial: https://rajansahu713.medium.com/how-to-use-serializer-effectively-in-django-813e00b67b65
    classroom = serializers.SerializerMethodField()
    
    class Meta:
        model = Classroom # Model that will be used.
        fields = ['id', 'year', 'letter', 'classroom'] # Database fields.
    
    # Combines year and letter values.
    def get_classroom(self, obj):
        return f'{obj.year}-{obj.letter}'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'class_id']