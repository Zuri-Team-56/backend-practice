from rest_framework import generics, permissions
from core.careerquestionoption.models import CareerQuestionOption
from core.careerquestionoption.serializers import CareerQuestionOptionSerializer


class CareerQuestionOptionList(generics.ListCreateAPIView):
    queryset = CareerQuestionOption.objects.all()
    serializer_class = CareerQuestionOptionSerializer
    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


class CareerQuestionOptionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,) 
    # permission_classes = (IsAuthorOrReadOnly,) 
    queryset = CareerQuestionOption.objects.all()
    serializer_class = CareerQuestionOptionSerializer
