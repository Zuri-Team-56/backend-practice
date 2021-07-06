from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import SavedScholarshipSerializer

from .models import SavedScholarship

from rest_framework.permissions import IsAuthenticated



class SavedScholarshipViewSet(viewsets.ModelViewSet):
    queryset = SavedScholarship.objects.all().order_by('scholarship')
    serializer_class = SavedScholarshipSerializer