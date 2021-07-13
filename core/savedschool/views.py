from rest_framework import generics, permissions
from core.savedschool.models import SavedSchool
from core.savedschool.serializers import SavedSchoolSerializer


class SavedSchoolList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = SavedSchool.objects.all()
    serializer_class = SavedSchoolSerializer


class SavedSchoolDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = SavedSchool.objects.all()
    serializer_class = SavedSchoolSerializer
