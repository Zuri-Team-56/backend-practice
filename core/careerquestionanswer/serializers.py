from rest_framework import serializers
from core.careerquestionanswer.models import CareerQuestionAnswer



class CareerQuestionAnswerSerializer(serializers.ModelSerializer):
    # student_name = serializers.ReadOnlyField(source='student.username')
    class Meta:
        # fields = ('id', 'question', 'answer', 'student_name')
        fields = ('__all__')
        model = CareerQuestionAnswer