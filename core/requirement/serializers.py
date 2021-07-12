from rest_framework import serializers

from .models import Requirements


class RequirementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Requirements
        fields = [
            'title',
            'slug',
            'school',
            'program',
            'description',
        ]
   