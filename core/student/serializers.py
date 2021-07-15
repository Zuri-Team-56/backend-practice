from core.savedschool.serializers import SavedSchoolSerializer
from core.savedscholarship.serializers import SavedScholarshipSerializer
from core.savedcourse.serializers import SavedCourseSerializer
from rest_framework import serializers
from core.student.models import StudentAccount

class StudentAccountSerializer(serializers.ModelSerializer):
    savedcourse = SavedCourseSerializer(many=True, read_only=True)
    savedscholarship = SavedScholarshipSerializer(many=True, read_only=True)
    savedschool = SavedSchoolSerializer(many=True, read_only=True)
    
    class Meta:
        model = StudentAccount
        fields = [
            'user',
            'image',
            'first_name',
            'last_name',
            'slug',
            'telephone',
            'mobile',
            'gender',
            'email',
            'educational_level',
            'country',
            'state',
            'savedcourse',
            'savedschool',
            'savedscholarship'
        ]
        extra_kwargs = {
            'image': {'required': False}
        }