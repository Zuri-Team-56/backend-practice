from django.contrib.auth import get_user_model 
from rest_framework import serializers
from core.student.models import StudentAccount


class StudentAccountSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = StudentAccount


class UserSerializer(serializers.ModelSerializer): # new
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)