from django.db.models.query import QuerySet
from rest_framework import serializers
from .models import SavedSchool, StudentAccount
from django.contrib.auth.models import User
from .models import CareerQuestion
from .models import CareerQuestionAnswer
from .models import SavedSchool


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('__all__')

# class StudentAccountSerializer(serializers.HyperlinkedModelSerializer):
#     user_obj = User.objects.all()

#     user = serializers.HyperlinkedRelatedField(
#         view_name='user-detail',
#         queryset = user_obj
#     )
#     class Meta:
#         model = StudentAccount
#         fields = ('__all__')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')


class StudentAccountSerializer(serializers.HyperlinkedModelSerializer):
    user_obj = User.objects.all()

    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        queryset = user_obj
    )

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