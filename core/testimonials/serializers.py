from .models import Testimonial
from rest_framework import serializers


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = [
            '__all__',
        ]
        extra_kwargs = {
            'image': {'required': False}
        }