from rest_framework import serializers
from core.savedcourse.models import SavedCourse


class SavedCourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = SavedCourse