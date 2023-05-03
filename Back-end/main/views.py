from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Teacher, Classroom, Subject, Student, ClassAssignment, Timetable, Grade
from .serializers import TeacherSerializer, ClassroomSerializer, SubjectSerializer, StudentSerializer, ClassAssignmentSerializer, TimetableSerializer, GradeSerializer
from rest_framework import generics



# Create your views here.


# Define the API Methods supported.
class TeachersList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()    # Get all teachers
    serializer_class = TeacherSerializer    # Serialize them

class TeacherDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class ClassroomsList(generics.ListCreateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

class ClassroomDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer


class SubjectsList(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class StudentsList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ClassAssignmentsList(generics.ListCreateAPIView):
    queryset = ClassAssignment.objects.all()
    serializer_class = ClassAssignmentSerializer

class ClassAssignmentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClassAssignment.objects.all()
    serializer_class = ClassAssignmentSerializer


class TimetablesList(generics.ListCreateAPIView):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer

class TimetableDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer


class GradesList(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

class GradeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer