from rest_framework import generics, permissions
from core.student.models import StudentAccount
from core.student.serializers import StudentAccountSerializer
from .permissions import IsAuthor


class StudentAccountList(generics.ListCreateAPIView):

    permission_classes = (permissions.IsAdminUser,)
    queryset = StudentAccount.objects.all()
    serializer_class = StudentAccountSerializer


class StudentAccountDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthor]
    permission_classes = (permissions.IsAdminUser,)
    queryset = StudentAccount.objects.all()
    serializer_class = StudentAccountSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
