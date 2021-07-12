# from django.db.models.query import QuerySet
from core.courses.models import Course
from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import SavedCourse


class SavedCourseSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = SavedCourse
        fields = ('__all__')

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('__all__')