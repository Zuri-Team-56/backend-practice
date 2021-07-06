from django.db.models.query import QuerySet
from rest_framework import serializers
from .models import SavedSchool
from django.contrib.auth.models import User


class SavedSchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SavedSchool
        fields = ('__all__')
