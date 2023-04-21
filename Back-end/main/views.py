from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Teacher, Classroom, Subject
from .serializers import TeacherSerializer, ClassroomSerializer, SubjectSerializer


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
    pass