from rest_framework import serializers

from .models import Tuition


class TuitionSerializer(serializers.ModelSerializer):

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
   