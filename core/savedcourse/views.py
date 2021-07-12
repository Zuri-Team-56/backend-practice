from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import SavedCourseSerializer

from .models import SavedCourse

from rest_framework.permissions import IsAuthenticated


class SavedCourseViewSet(viewsets.ModelViewSet):
    queryset = SavedCourse.objects.all().order_by('course')
    serializer_class = SavedCourseSerializer