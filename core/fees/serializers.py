from rest_framework import serializers

from .models import Tuition


class TuitionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tuition
        fields = [
            'pk',
            'title',
            'slug',
            'school_name',
            'undergraduate_tuition',
            'undergraduate_fee',
            'postgraduate_tuition',
            'postgraduate_fee',
            'website',
        ]
   