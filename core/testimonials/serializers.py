from .models import Testimonial
from rest_framework import serializers


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = [
            'pk',
            'image',
            'testimonial',
            'date',
        ]
        extra_kwargs = {
            'image': {'required': False}
        }