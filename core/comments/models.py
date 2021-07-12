from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse

from core.articles.models import Article


"""COMMENT MODEL"""
class Comment(models.Model): # Create new course model

    article = models.ForeignKey(Article, related_name="article", on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    body = models.TextField()
    date = models.DateField()

    class Meta:
        ordering = ['-date']

    def get_absolute_url(self):
        return reverse("comments:detail", kwargs={'pk': self.pk})

    def __str__(self):
        #return '%s - %s' % (self.article, self.commenter)
        return str(self.commenter.username)
        