from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializer import StudentSerializer
from django.http import JsonResponse
# import requests



@api_view(['GET'])
def load_student(request):
    students = Student.objects.all()
    serialized_data = StudentSerializer(students, many = True)
    return JsonResponse(serialized_data.data, safe=False)


@api_view(['POST'])
def add_student(request):
    serialized_data = StudentSerializer(data=request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return JsonResponse({'mesage': 'data is succesfully inserted'})
    else:
        return JsonResponse({'mesage': 'invalid data'})


@api_view(['PUT'])
def update_student(request,s_id):
    student = Student.objects.get(id=s_id)
    serialized_data = StudentSerializer(student,data = request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return JsonResponse({'mesage': 'data is succesfully updated'})
    else:
        return JsonResponse({'mesage': 'invalid data'})

@api_view(['DELETE'])
def delete_student(request, s_id):
    student = Student.objects.get(id=s_id)
    student.delete()
    return JsonResponse({'mesage': 'data is succesfully deleted'})







