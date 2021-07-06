from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import StudentAccountSerializer, UserSerializer

from .models import  StudentAccount

from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class StudentAccountViewSet(viewsets.ModelViewSet):
    queryset = StudentAccount.objects.all().order_by('user')
    serializer_class = StudentAccountSerializer
