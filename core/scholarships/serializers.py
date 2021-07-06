from rest_framework import serializers

from .models import Scholarship


class ScholarshipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scholarship
        fields = [
            'pk',
            'name',
            'slug',
            'description',
            'image',
            'requirements',
            'institution',
            'website',
            'date',
        ]
        extra_kwargs = {
            'image': {'required': False}
        }


