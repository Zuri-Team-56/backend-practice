from rest_framework import serializers
from core.savedschool.models import SavedSchool


class SavedSchoolSerializer(serializers.ModelSerializer):
    student = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    school = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = SavedSchool
        fields = ('__all__')
        
