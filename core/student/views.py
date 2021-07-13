from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from core.student.models import StudentAccount
from core.student.serializers import StudentAccountSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly 


class StudentAccountList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = StudentAccount.objects.all()
    serializer_class = StudentAccountSerializer


class StudentAccountDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (IsAuthorOrReadOnly,) 
    queryset = StudentAccount.objects.all()
    serializer_class = StudentAccountSerializer


class UserList(generics.ListCreateAPIView): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer