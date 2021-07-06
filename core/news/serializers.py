from rest_framework import serializers

from .models import SchoolNews


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolNews
        fields = [
            'pk',
            'category',
            'title',
            'slug',
            'school_name',
            'information',
            'date',
           
        ]
   
   