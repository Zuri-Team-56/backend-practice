
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CareerQuestion, CareerQuestionOption
from .models import CareerQuestionAnswer


class CareerQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CareerQuestion
        fields = ('__all__')

class CareerQuestionAnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CareerQuestionAnswer
        fields = ('__all__')

class CareerQuestionOptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CareerQuestionOption
        fields = ('__all__')