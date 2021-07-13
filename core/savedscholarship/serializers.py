from rest_framework import serializers
from core.savedscholarship.models import SavedScholarship


class SavedScholarshipSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = SavedScholarship