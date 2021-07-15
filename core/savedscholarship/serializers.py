from rest_framework import serializers
from core.savedscholarship.models import SavedScholarship


class SavedScholarshipSerializer(serializers.ModelSerializer):
    student = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    scholarship = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = SavedScholarship
        fields = ('__all__')
        