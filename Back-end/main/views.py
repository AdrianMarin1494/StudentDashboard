from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Teacher
from .serializers import TeacherSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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
        return JsonResponse({"teachers": serializer_object.data})
    
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