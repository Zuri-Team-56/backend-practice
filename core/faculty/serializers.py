from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Faculty


class FacultySerializer(serializers.ModelSerializer):    
    class Meta:
        model = Faculty
        fields = [
            'pk',
            'name',
            'slug',
            'image',
            'school',
           
        ]
        extra_kwargs = {
            'image': {'required': False}
        }