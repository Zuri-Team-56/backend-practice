from django.shortcuts import render
from django.http import Http404
from core.permissions import UserAdmin
from rest_framework.permissions import AllowAny

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import Article
from .serializers import ArticleSerializer


class ArticleList(ListCreateAPIView):
    
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [AllowAny]
        else:
            permission_classes = [UserAdmin]
        return [permission() for permission in permission_classes]


class ArticleDetail(RetrieveUpdateDestroyAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [AllowAny]
        else:
            permission_classes = [UserAdmin]
        return [permission() for permission in permission_classes]
    
