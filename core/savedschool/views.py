from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import SavedSchoolSerializer

from .models import SavedSchool

from rest_framework.permissions import IsAuthenticated


class SavedSchoolViewSet(viewsets.ModelViewSet):
    queryset = SavedSchool.objects.all().order_by('school')
    serializer_class = SavedSchoolSerializer


