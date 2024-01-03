from rest_framework import generics
from .models import Employees,Department,Tasks
from .serialization import EmployeeSerializer,DepartmentSerializer,TaskSerializer,AchivmentSerializer

class EmployeeGetCreate(generics.ListCreateAPIView):
    queryset =Employees.objects.all()
    serializer_class =EmployeeSerializer

class EmployeeUpdateDelte(generics.RetrieveUpdateDestroyAPIView):
    queryset =Employees.objects.all()
    serializer_class =EmployeeSerializer


class DepartmentGetCreate(generics.ListCreateAPIView):
    queryset =Department.objects.all()
    serializer_class =DepartmentSerializer

class DepartmentUpdateDelte(generics.RetrieveUpdateDestroyAPIView):
    queryset =Department.objects.all()
    serializer_class =DepartmentSerializer



class TasksGetCreate(generics.ListCreateAPIView):
    queryset =Tasks.objects.all()
    serializer_class =TaskSerializer

class TasksUpdateDelte(generics.RetrieveUpdateDestroyAPIView):
    queryset =Tasks.objects.all()
    serializer_class =TaskSerializer



class AchivmentGetCreate(generics.ListCreateAPIView):
    queryset =Tasks.objects.all()
    serializer_class =AchivmentSerializer

class AchivmentUpdateDelte(generics.RetrieveUpdateDestroyAPIView):
    queryset =Tasks.objects.all()
    serializer_class =AchivmentSerializer
