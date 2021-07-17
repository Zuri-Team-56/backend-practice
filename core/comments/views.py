from core.articles.models import Article
from django.shortcuts import render
from django.http import Http404
from core.permissions import UserAdmin, IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.response import Response
from rest_framework import status

from .serializers import CommentSerializer
from .models import Comment


class CommentList(ListCreateAPIView):
    
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated, UserAdmin]
        return [permission() for permission in permission_classes]


class CommentDetail(RetrieveUpdateDestroyAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'

    #Allow only staff or superusers to delete comments, allow commenter to edit comments
    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [AllowAny]
        elif self.request.method == 'DELETE':
            permission_classes = [UserAdmin]
        else:
            permission_classes = [IsOwnerOrReadOnly]
        return [permission() for permission in permission_classes]




