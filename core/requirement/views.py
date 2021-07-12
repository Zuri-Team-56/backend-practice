from django.shortcuts import render
from django.http import Http404
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser 

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import Requirements
from .serializers import RequirementSerializer


class RequirementList(ListCreateAPIView):
    
    queryset = Requirements.objects.all()
    serializer_class = RequirementSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class RequirementDetail(RetrieveUpdateDestroyAPIView):

    queryset = Requirements.objects.all()
    serializer_class = RequirementSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]