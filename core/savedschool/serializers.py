from django.db.models.query import QuerySet
from rest_framework import serializers
from .models import SavedSchool
from django.contrib.auth.models import User
from core.schools.models import School


class SavedSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedSchool
        fields = ('__all__')


class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = ('__all__')