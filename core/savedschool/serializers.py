from rest_framework import serializers
from core.savedschool.models import SavedSchool


class SavedSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = SavedSchool
