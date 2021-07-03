from django.shortcuts import render
from django.http import Http404

from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.response import Response
from rest_framework import status

from .serializers import CommentSerializer
from core.models import Comment
from core.permissions import IsOwnerOrReadOnly


class CommentList(ListCreateAPIView):
    
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class CommentDetail(RetrieveUpdateDestroyAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser, IsOwnerOrReadOnly]
        return [permission() for permission in permission_classes]




