from rest_framework import generics

from rest_framework.permissions import AllowAny, IsAdminUser 

from .models import Course
from .serializers import CourseSerializer


#Making request for courses

class CreateCourseViews(generics.CreateAPIView):
    #This endpoint allows for creation of a course
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminUser]

class GetCourseListViews(generics.ListAPIView):
     #This endpoint list all of the courses of all institutions
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]

class UpdateCourseViews(generics.UpdateAPIView):
    #This endpoint allows for updating a specific course
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminUser]
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'

class DeleteCourseViews(generics.DestroyAPIView):
    #This endpoint allows for deletion of a specific course
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminUser]
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'

class ViewCourseViews(generics.RetrieveAPIView):
    #This endpoint view the details of a specific course
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'

