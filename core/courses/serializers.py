from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Course


class CourseSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Course
        fields = [
            'pk',
            'course_name',
            'slug',
            'school_name',
            'image',
            'course_requirements',
            'program',
            'name_of_department',
            'school_location',
            'tuition', 
            'tution_price',
            'address',
            'addressState',
            'duration',
            'durationYears',
            'compare',
        ]
        extra_kwargs = {
            'image': {'required': False}
        }
