from rest_framework import serializers
from django.contrib.auth.models import User

from .models import FacultyName


class FacultySerializer(serializers.ModelSerializer):    
    class Meta:
        model = FacultyName
        fields = [
            'pk',
            'name',
            'slug',
            'name_of_school',
            #'body',
        ]