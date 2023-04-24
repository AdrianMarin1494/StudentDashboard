from rest_framework import serializers
from .models import Teacher, Classroom, Subject, Student, ClassAssignment, Timetable, Grade

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
    student_classroom = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'class_id', 'student_classroom']

    def get_student_classroom(self, obj):
        return f"{obj.class_id.YearChoices(obj.class_id.year).label}-{obj.class_id.letter}"


class ClassAssignmentSerializer(serializers.ModelSerializer):
    classroom = serializers.SerializerMethodField()
    subject = serializers.SerializerMethodField()
    teacher = serializers.SerializerMethodField()    

    class Meta:
        model = ClassAssignment
        fields = ['id', 'class_id', 'classroom', 'subject_id', 'subject', 'teacher_id', 'teacher']

    def get_classroom(self, obj):
        return f"{obj.class_id.YearChoices(obj.class_id.year).label}-{obj.class_id.letter}"
    
    def get_subject(self, obj):
        return f"{obj.subject_id.subject_name}"
    
    def get_teacher(self, obj):
        return f"{obj.teacher_id.first_name} {obj.teacher_id.last_name}"