from rest_framework import generics, permissions
from core.savedcourse.models import SavedCourse
from core.savedcourse.serializers import SavedCourseSerializer


class SavedCourseList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = SavedCourse.objects.all()
    serializer_class = SavedCourseSerializer


class SavedCourseDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,) 
    queryset = SavedCourse.objects.all()
    serializer_class = SavedCourseSerializer
