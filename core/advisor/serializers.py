from rest_framework import serializers
from core.advisor.models import CareerQuestion #CareerQuestionAnswer, CareerQuestionOption


class CareerQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = CareerQuestion
        


# class CareerQuestionOptionSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = ('__all__')
#         model = CareerQuestionOption


# class CareerQuestionAnswerSerializer(serializers.ModelSerializer):
#     student_name = serializers.ReadOnlyField(source='student.username')
#     class Meta:
#         fields = ('id', 'question', 'answer', 'student_name')
#         model = CareerQuestionAnswer