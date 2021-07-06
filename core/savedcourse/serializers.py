from django.db.models.query import QuerySet
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import SavedCourse


class SavedCourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SavedCourse
        fields = ('__all__')
