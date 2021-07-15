from rest_framework import generics, permissions
from core.savedcourse.models import SavedCourse
from core.savedcourse.serializers import SavedCourseSerializer
from .permissions import IsAuthor


class SavedCourseList(generics.ListCreateAPIView):
    permission_classes = [IsAuthor]
    permission_classes = (permissions.IsAdminUser,)
    queryset = SavedCourse.objects.all()
    serializer_class = SavedCourseSerializer


class SavedCourseDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthor]
    permission_classes = (permissions.IsAdminUser,)
    queryset = SavedCourse.objects.all()
    serializer_class = SavedCourseSerializer
