from django.db.models.query import QuerySet
from rest_framework import serializers
from .models import StudentAccount
from django.contrib.auth.models import User



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
