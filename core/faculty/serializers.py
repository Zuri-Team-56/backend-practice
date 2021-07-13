from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Faculty
from core.department.serializers import DepartmentSerializer

class FacultySerializer(serializers.ModelSerializer):  
    department = DepartmentSerializer(many=True, read_only=True)

    class Meta:
        model = Faculty
        fields = [
            'pk',
            'name',
            'slug',
            'image',
            'school',
            'department'
           
        ]
        extra_kwargs = {
            'image': {'required': False}
        }