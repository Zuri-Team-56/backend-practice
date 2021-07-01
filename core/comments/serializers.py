from rest_framework import serializers

from core.models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'pk',
            'article',
            'commenter',
            'body',
            'date',
        ]

