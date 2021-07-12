from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Department


class DepartmentSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Department
        fields = [
            'pk',
            'name',
            'slug',
            'image',
            'faculty',
        ]
        extra_kwargs = {
            'image': {'required': False}
        }