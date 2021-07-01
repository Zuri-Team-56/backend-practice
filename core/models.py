from django.db import models
from django.contrib.auth.models import User  # import the superuser
from phonenumber_field.modelfields import PhoneNumberField
from autoslug import AutoSlugField


# Create your models here.

class Article(models.Model): # Create new post model

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=False, unique=True)
    slug = AutoSlugField(populate_from='title', blank=True, editable=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    body = models.TextField()
    date = models.DateField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return "{}".format(self.title)
