from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Department
from core.courses.serializers import CourseSerializer

class DepartmentSerializer(serializers.ModelSerializer):   
    courses = CourseSerializer(many=True, read_only=True)
    faculty = serializers.SlugRelatedField(read_only=True, slug_field='name') 
      
    class Meta:
        model = Department
        fields = [
            'pk',
            'name',
            'slug',
            'image',
            'faculty',
            'courses'
        ]
        extra_kwargs = {
            'image': {'required': False}
        }