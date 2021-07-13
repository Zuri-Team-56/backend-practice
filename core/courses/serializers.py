from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Course
from core.fees.serializers import TuitionSerializer

class CourseSerializer(serializers.ModelSerializer):
    fees = TuitionSerializer(many=True, read_only=True)

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
            'fees',
            'address',
            'addressState',
            'duration',
            'durationYears',
            'compare',
        ]
        extra_kwargs = {
            'image': {'required': False}
        }