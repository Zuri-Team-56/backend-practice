
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from autoslug import AutoSlugField
from django.urls import reverse


"""ARTICLE MODEL"""
class Article(models.Model): # Create new post model

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=False, unique=True)
    slug = AutoSlugField(populate_from='title', unique=True, blank=True, editable=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    body = models.TextField()
    snippet = models.CharField(max_length=350)
    date = models.DateField()

    class Meta:
        ordering = ['-date']

    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("detail", kwargs={'slug': self.slug})

    