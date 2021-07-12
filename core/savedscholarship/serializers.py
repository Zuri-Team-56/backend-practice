from django.db.models.query import QuerySet
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import SavedScholarship
from core.scholarships.models import Scholarship


class SavedScholarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedScholarship
        fields = ('__all__')

class ScholarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scholarship
        fields = ('__all__')