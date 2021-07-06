from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Article
        fields = [
            'pk',
            'author',
            'title',
            'slug',
            'image',
            'body',
            'date',
        ]
        extra_kwargs = {
            'image': {'required': False}
        }

