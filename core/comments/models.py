from django.db import models
from django.contrib.auth.models import User 

from core.articles.models import Article


"""COMMENT MODEL"""
class Comment(models.Model): # Create new course model

    articlename = models.ForeignKey(Article, related_name="article", on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return '%s - %s' % (self.articlename, self.commenter)