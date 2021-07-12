from rest_framework import serializers

from .models import News


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = [
            'pk',
            'title',
            'slug',
            'category',
            'school',
            'image',
            'info',
            'snippet',
            'date',
           
        ]
   
   