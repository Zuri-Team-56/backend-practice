
from django.conf import settings
from django.contrib import admin
from django.urls import path, include


GET_OPTIONS = {'get': 'list'}

RETRIEVE_OPTIONS = {'get': 'retrieve'}

POST_OPTIONS = {'post': 'create'}

LIST_OPTIONS = {
    'get': 'list',
    'post': 'create'
}

DETAIL_OPTIONS = {
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}

urlpatterns = []
