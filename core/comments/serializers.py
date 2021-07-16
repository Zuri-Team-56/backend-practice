from rest_framework import serializers

from .models import Comment
# from core.articles.serializers import ArticleSerializer
# from core.student.serializers import StudentAccountSerializer

class CommentSerializer(serializers.ModelSerializer):
    article = serializers.SlugRelatedField(read_only=True, slug_field='title')
    # article = ArticleSerializer(many=True, read_only=True)
    # commenter = StudentAccountSerializer(many=True, read_only=True)
    commenter = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    class Meta:
        model = Comment
        fields = [
            'pk',
            'article',
            'commenter',
            'image',
            'body',
            'date',
        ]

