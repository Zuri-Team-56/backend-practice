from django.shortcuts import render
from .models import Testimonial, UniversityReview, School
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView
from .serializers import TestimonialSerializer, UniversityReviewSerializer

# Create your views here.

class TestimonialListAPIView(ListAPIView):
    serializer_class = TestimonialSerializer
    queryset = Testimonial.objects.all()
    permission_classes = [permissions.AllowAny]


class UniversityReviewAPIListView(ListCreateAPIView):
    serializer_class = UniversityReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self, **kwargs):
        pk = kwargs.get('pk')
        queryset = UniversityReview.objects.filter()
        return queryset

    def perform_create(self, serializer, **kwargs):
        author = self.request.user
        pk = self.kwargs.get('pk')
        print(pk)
        university = School.objects.get(pk=pk)
        serializer.save(author=author, university=university)
