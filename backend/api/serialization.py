from rest_framework import serializers
from .models import Employees,Department,Tasks,Achivment
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model =Employees
        fields = '__all__'    

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Department
        fields = '__all__'    

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model =Tasks
        fields = '__all__'    
        
class AchivmentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Achivment
        fields = '__all__'    
