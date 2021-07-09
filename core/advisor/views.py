from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import CareerQuestionSerializer, CareerQuestionAnswerSerializer, CareerQuestionOptionSerializer

from .models import CareerQuestion, CareerQuestionAnswer, CareerQuestionOption

from rest_framework.permissions import IsAuthenticated


class CareerQuestionViewSet(viewsets.ModelViewSet):
    queryset = CareerQuestion.objects.all().order_by('question')
    serializer_class = CareerQuestionSerializer

class CareerQuestionAnswerViewSet(viewsets.ModelViewSet):
    queryset = CareerQuestionAnswer.objects.all().order_by('question')
    serializer_class = CareerQuestionAnswerSerializer

class CareerQuestionOptionViewSet(viewsets.ModelViewSet):
    queryset = CareerQuestionOption.objects.all().order_by('question')
    serializer_class = CareerQuestionOptionSerializer
