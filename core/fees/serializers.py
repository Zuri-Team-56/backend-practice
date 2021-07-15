from rest_framework import serializers

from .models import Tuition


class TuitionSerializer(serializers.ModelSerializer):
    course = serializers.SlugRelatedField(read_only=True, slug_field='course_name')

    class Meta:
        model = Tuition
        fields = [
            'pk',
            'title',
            'slug',
            'course',
            'program',
            'description',
            'amount',
            'website',
        ]
   