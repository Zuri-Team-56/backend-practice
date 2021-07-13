from rest_framework import serializers

from .models import School

from core.courses.serializers import CourseSerializer
from core.programs.serializers import ProgramSerializer
from core.faculty.serializers import FacultySerializer
from core.requirement.serializers import RequirementSerializer
from core.news.serializers import NewsSerializer

class SchoolSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    programs = ProgramSerializer(many=True, read_only=True)
    faculty = FacultySerializer(many=True, read_only=True)
    requirement = RequirementSerializer(many=True, read_only=True)
    news = NewsSerializer(many=True, read_only=True)


    class Meta:
        model = School
        fields = [
            'pk',
            'name',
            'slug',
            'overview',
            'image',
            'program',
            'programs',     #ForeignKeyRelatedName
            'requirement',  #ForeignKeyRelatedName
            'faculty',      #ForeignKeyRelatedName
            'world_ranking',
            'number_of_students',
            'tuition', 
            'courses',       #ForeignKeyRelatedName        
            'financial_aid',
            'hostel',
            'has_hostel',
            'location',
            'news',         #ForeignKeyRelatedName
            #'saved_school'
            'website',
            'reviews',
            
      
        ]
        extra_kwargs = {
            'image': {'required': False}
        }

