from rest_framework import generics

from rest_framework.permissions import IsAdminUser, AllowAny

from .models import School
from .serializers import SchoolSerializer



# Create your views here.


#Making request for schools

class CreateSchoolViews(generics.CreateAPIView):
    #This endpoint allows for creation of an institution
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsAdminUser]
    

class GetSchoolListViews(generics.ListAPIView):
    #This endpoint list all of the Institution
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [AllowAny]


class UpdateSchoolViews(generics.UpdateAPIView):
    #This endpoint allows for updating a specific institution by passing in the id of the insitution
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsAdminUser]
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'

class DeleteSchoolViews(generics.DestroyAPIView):
    #This endpoint allows for deletion of a specific institution
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsAdminUser]
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'

class ViewSchoolViews(generics.RetrieveAPIView):
    #This endpoint view the details of a specific institution
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [AllowAny]
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'

