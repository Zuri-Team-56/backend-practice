from rest_framework import generics, permissions
from core.careerquestionoption.models import CareerQuestionOption
from core.careerquestionoption.serializers import CareerQuestionOptionSerializer


class CareerQuestionOptionList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = CareerQuestionOption.objects.all()
    serializer_class = CareerQuestionOptionSerializer


class CareerQuestionOptionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,) 
    # permission_classes = (IsAuthorOrReadOnly,) 
    queryset = CareerQuestionOption.objects.all()
    serializer_class = CareerQuestionOptionSerializer
