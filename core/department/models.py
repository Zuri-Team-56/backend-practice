
from core.faculty.models import Faculty
from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField


"""DEPARTMENT MODEL""" 
class Department(models.Model): # Create new department model

    name = models.CharField(max_length=150, help_text='Enter Department name', blank=False, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True, blank=True, editable=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    faculty = models.ForeignKey(Faculty, related_name="department", on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse("department:detail", kwargs={'slug': self.slug})

    def __str__(self):
        return self.name
