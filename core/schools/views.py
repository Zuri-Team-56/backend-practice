from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from .models import School
from .serializers import SchoolSerializer



# Create your views here.


#Making request for schools

class CreateSchoolViews(generics.CreateAPIView):
    #This endpoint allows for creation of an institution
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class GetSchoolListViews(generics.ListAPIView):
    #This endpoint list all of the Institution
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class UpdateSchoolViews(generics.UpdateAPIView):
    #This endpoint allows for updating a specific institution by passing in the id of the insitution
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class DeleteSchoolViews(generics.DestroyAPIView):
    #This endpoint allows for deletion of a specific institution
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class ViewSchoolViews(generics.RetrieveAPIView):
    #This endpoint view the details of a specific institution
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

