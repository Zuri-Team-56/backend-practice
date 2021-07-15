from rest_framework import serializers
from core.careerquestionoption.models import CareerQuestionOption



class CareerQuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = CareerQuestionOption