from rest_framework import generics, permissions
from core.savedscholarship.models import SavedScholarship
from core.savedscholarship.serializers import SavedScholarshipSerializer


class SavedScholarshipList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = SavedScholarship.objects.all()
    serializer_class = SavedScholarshipSerializer


class SavedScholarshipDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = SavedScholarship.objects.all()
    serializer_class = SavedScholarshipSerializer
