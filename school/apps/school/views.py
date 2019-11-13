from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Student
import json

# Create your views here.
class StudentView(APIView):
    def get(self, request):
        id = request.GET.get('id', None)
        name = request.GET.get('name', None)
        if id != None:
            students = Student.objects.all().filter(id=id)
            if len(students) > 0:
                array_student = []
                for a in students:
                    dict = {'id': a.id, 'name': a.name}
                    array_student.append(dict)
                return Response(array_student, status=status.HTTP_200_OK)
            else:
                return Response(students, status=status.HTTP_204_NO_CONTENT)
        elif name != None:
            students = Student.objects.all().filter(name=name)
            if len(students) > 0:
                array_student = []
                for a in students:
                    dict = {'id': a.id, 'name': a.name}
                    array_student.append(dict)
                return Response(array_student, status=status.HTTP_200_OK)
            else:
                return Response(students, status=status.HTTP_204_NO_CONTENT)
        else:
            students = Student.objects.all()
            if len(students) > 0:
                array_student = []
                for a in students:
                    dict = {'id': a.id, 'name': a.name}
                    array_student.append(dict)
                return Response(array_student, status=status.HTTP_200_OK)
            else:
                return Response(students, status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        name = request.POST.get('name', None)
        if name:
            students = Student(name=name)
            students.save()
            return Response({}, status=status.HTTP_201_CREATED)
        else:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        id = request.POST.get('id', None)
        name = request.POST.get('name', None)
        print(id)
        print(name)
        if id != None and name != None:
            students = Student.objects.all().filter(id=id)
            if len(students) > 0:
                for a in students:
                    student = a
                    student.name = name
                    student.save()
                return Response({}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(students, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        id = request.POST.get('id', None)
        if id != None:
            student = Student.objects.all().filter(id=id)
            if len(student) > 0:
                for a in student:
                    student = a
                    student.delete()
                return Response({}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)