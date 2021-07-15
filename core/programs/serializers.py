from rest_framework import serializers

from .models import Program


class ProgramSerializer(serializers.ModelSerializer):
    school = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Program
        fields = [
            'pk',
            'name',
            'title',
            'type',
            'slug',
            'school',
            'information',
        ]