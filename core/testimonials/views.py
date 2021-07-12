from core.testimonials.serializers import TestimonialSerializer
from .models import Testimonial
from rest_framework.generics import ListAPIView
from rest_framework import permissions


class TestimonialListAPIView(ListAPIView):
    serializer_class = TestimonialSerializer
    queryset = Testimonial.objects.all()
    permission_classes = [permissions.AllowAny]