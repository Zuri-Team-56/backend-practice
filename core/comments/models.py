from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse

from core.articles.models import Article
from core.student.models import StudentAccount


"""COMMENT MODEL"""
class Comment(models.Model): # Create new course model

    article = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE)
    commenter = models.ForeignKey(StudentAccount, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    body = models.TextField()
    date = models.DateField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        # return str(self.commenter.username)
        return f"{self.commenter} {self.article}"
        # return '%s %s' % (self.article, self.commenter)
        
    # Comment.objects.filter(article = article_title)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.commenter +'-'+ self.article)
    #     super(Comment, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("comments:detail", kwargs={'pk': self.pk})