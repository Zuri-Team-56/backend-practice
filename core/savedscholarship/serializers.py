from django.db.models.query import QuerySet
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import SavedScholarship


class SavedScholarshipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SavedScholarship
        fields = ('__all__')