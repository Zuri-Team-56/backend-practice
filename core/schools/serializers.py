from rest_framework import serializers

from .models import School

from core.courses.serializers import CourseSerializer
from core.programs.serializers import ProgramSerializer



class SchoolSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    programs = ProgramSerializer(many=True, read_only=True)

    class Meta:
        model = School
        fields = [
            'pk',
            'name',
            'slug',
            'overview',
            'image',
            'programs',
            #'entry_requirements',
            #'faculty_name',
            'world_ranking',
            'number_of_students',
            #'tuition_information',
            'financial_aid',
            'hostel',
            'has_hostel',
            'location',
            #'school_news',
            #'saved_school'
            'website',
            #'courses'    #ForeignKeyRelatedName
      
        ]
        extra_kwargs = {
            'image': {'required': False}
        }

