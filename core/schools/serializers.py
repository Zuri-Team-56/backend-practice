from rest_framework import serializers

from .models import School


class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = [
            'pk',
            'name',
            'slug',
            'overview',
            'image',
            'program',
            'entry_requirements',
            'faculty_name',
            'world_ranking',
            'number_of_students',
            'tuition_information',
            'financial_aid',
            'hostel',
            'has_hostel',
            'location',
            'school_news',
            #'saved_school'
            'website',
      
        ]
        extra_kwargs = {
            'image': {'required': False}
        }

