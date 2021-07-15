from rest_framework import serializers

from .models import Requirements


class RequirementSerializer(serializers.ModelSerializer):
    school = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Requirements
        fields = [
            'title',
            'slug',
            'school',
            'program',
            'description',
        ]
   