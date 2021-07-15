from rest_framework import serializers
from core.savedcourse.models import SavedCourse


class SavedCourseSerializer(serializers.ModelSerializer):
    student = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    course = serializers.SlugRelatedField(read_only=True, slug_field='course_name')

    class Meta:
        model = SavedCourse
        fields = ('__all__')

