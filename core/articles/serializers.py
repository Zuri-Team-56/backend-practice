from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Article
from core.comments.serializers import CommentSerializer

class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = [
            'pk',
            'author',
            'title',
            'slug',
            'image',
            'body',
            'snippet',
            'date',
            'comments'
        ]
        extra_kwargs = {
            'image': {'required': False}
        }

