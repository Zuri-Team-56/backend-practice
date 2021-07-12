
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser 
from .models import Program
from .serializers import ProgramSerializer


class CreateProgram(generics.CreateAPIView):
    
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [IsAdminUser]

class GetProgramList(generics.ListAPIView):

    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [AllowAny]

class UpdateProgram(generics.UpdateAPIView):
    
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [IsAdminUser]
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'

class DeleteProgram(generics.DestroyAPIView):
    
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [IsAdminUser]
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'

class ViewProgram(generics.RetrieveAPIView):
    
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [AllowAny]
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'