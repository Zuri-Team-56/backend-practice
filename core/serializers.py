from rest_framework import serializers
from .models import SavedSchool, StudentAccount
from .models import CareerQuestion
from .models import CareerQuestionAnswer
from .models import SavedSchool


class StudentAccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentAccount
        fields = ('__all__')

class CareerQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CareerQuestion
        fields = ('__all__')

class CareerQuestionAnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CareerQuestionAnswer
        fields = ('__all__')

class SavedSchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SavedSchool
        fields = ('__all__')