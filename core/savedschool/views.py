from rest_framework import generics, permissions
from core.savedschool.models import SavedSchool
from core.savedschool.serializers import SavedSchoolSerializer
from .permissions import IsAuthor


class SavedSchoolList(generics.ListCreateAPIView):
    permission_classes = [IsAuthor]
    permission_classes = (permissions.IsAdminUser,)
    queryset = SavedSchool.objects.all()
    serializer_class = SavedSchoolSerializer


class SavedSchoolDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthor]
    permission_classes = (permissions.IsAdminUser,)
    queryset = SavedSchool.objects.all()
    serializer_class = SavedSchoolSerializer
