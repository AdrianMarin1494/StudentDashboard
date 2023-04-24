from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Teacher, Classroom, Subject, Student, ClassAssignment
from .serializers import TeacherSerializer, ClassroomSerializer, SubjectSerializer, StudentSerializer, ClassAssignmentSerializer


# Create your views here.


# Define the API Methods supported.
@api_view(['GET', 'POST'])
def teachers(request):
    if request.method == "GET":
        # Get all teachers
        teachers_list = Teacher.objects.all()
        
        # Serialize them
        serializer_object = TeacherSerializer(teachers_list, many=True)

        # Return Json Response
        return Response(serializer_object.data)
    
    elif request.method == "POST":
        # Receive request data and save it.
        serializer_object = TeacherSerializer(data=request.data)

        if serializer_object.is_valid():
            serializer_object.save()
            return Response(serializer_object.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def teacher_info(request, id):

    try:
        # Get specific teacher info based on primary key id.
        teacher_info = Teacher.objects.get(pk=id)
    except Teacher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        # Serialize the object and return the data.
        serializer_object = TeacherSerializer(teacher_info)
        return Response(serializer_object.data)

    elif request.method == "PUT":
        serializer_object = TeacherSerializer(teacher_info, data=request.data)
        if serializer_object.is_valid():
            serializer_object.save()
            return Response(serializer_object.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer_object.errors, status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == "DELETE":
        teacher_info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
def classrooms(request):
    if request.method == "GET":
        classroom_list = Classroom.objects.all()
        serializer_object = ClassroomSerializer(classroom_list, many=True)
        return Response(serializer_object.data)
    
    elif request.method == "POST":
        serializer_object = ClassroomSerializer(data=request.data)
        if serializer_object.is_valid():
            serializer_object.save()
            return Response(serializer_object.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def classroom_info(request, id):
    try:
        classroom_info = Classroom.objects.get(pk=id)
    except Classroom.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer_object = ClassroomSerializer(classroom_info)
        return Response(serializer_object.data)
    
    elif request.method == "PUT":
        serializer_object = ClassroomSerializer(classroom_info, data=request.data)
        if serializer_object.is_valid():
            serializer_object.save()
            return Response(serializer_object.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer_object.data, status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == "DELETE":
        classroom_info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(["GET", "POST"])
def subject(request):
    if request.method == "GET":
        subject_list = Subject.objects.all()
        serializer_object = SubjectSerializer(subject_list, many=True)
        return Response(serializer_object.data)
    
    elif request.method == "POST":
        serializer_object = SubjectSerializer(data=request.data)
        if serializer_object.is_valid():
            serializer_object.save()
            return Response(serializer_object.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def subject_info(request, id):
    try:
        subject_info = Subject.objects.get(pk=id)
    except Subject.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer_object = SubjectSerializer(subject_info)
        return Response(serializer_object.data)
    
    elif request.method == "PUT":
        serializer_object = SubjectSerializer(subject_info, data=request.data)
        if serializer_object.is_valid():
            serializer_object.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == "DELETE":
        subject_info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
def student(request):
    if request.method == "GET":
        student_list = Student.objects.all()
        serializer_object = StudentSerializer(student_list, many=True)
        return Response(serializer_object.data)
    
    elif request.method == "POST":
        serializer_object = StudentSerializer(data=request.data)
        if serializer_object.is_valid():
            serializer_object.save()
            return Response(serializer_object.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def student_info(request, id):
    try:
        student_info = Student.objects.get(pk=id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer_object = StudentSerializer(student_info)
        return Response(serializer_object.data)
    
    elif request.method == "PUT":
        serializer_object = StudentSerializer(student_info, data=request.data)
        if serializer_object.is_valid():
            serializer_object.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == "DELETE":
        student_info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
def class_assignment(request):
    if request.method == "GET":
        class_assignment_list = ClassAssignment.objects.all()
        serializer_object = ClassAssignmentSerializer(class_assignment_list, many=True)
        return Response(serializer_object.data)
    
    elif request.method == "POST":
        serializer_object = ClassAssignmentSerializer(data=request.data)
        if serializer_object.is_valid():
            serializer_object.save()
            return Response(serializer_object.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def class_assignment_info(request, id):
    try:
        class_assignment_info = ClassAssignment.objects.get(pk=id)
    except ClassAssignment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer_object = ClassAssignmentSerializer(class_assignment_info)
        return Response(serializer_object.data)
    
    elif request.method == "PUT":
        serializer_object = ClassAssignmentSerializer(class_assignment_info, data=request.data)
        if serializer_object.is_valid():
            serializer_object.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == "DELETE":
        class_assignment_info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)