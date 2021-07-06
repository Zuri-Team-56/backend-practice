from rest_framework import serializers
from django.contrib.auth.models import User

from .models import DepartmentName


class DepartmentSerializer(serializers.ModelSerializer):    
    class Meta:
        model = DepartmentName
        fields = [
            'pk',
            'name',
            'slug',
            'name_of_faculty',
            #'body',
        ]