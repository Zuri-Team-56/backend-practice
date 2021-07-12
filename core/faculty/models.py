
from core.schools.models import School
from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField


"""FACULTY MODEL""" 
class Faculty(models.Model): # Create new faculty model

    name = models.CharField(max_length=150, help_text='Enter Name of Faculty', blank=False, unique=True)
    slug = AutoSlugField(populate_from='name', blank=True, editable=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True, related_name="faculties")
    
    class Meta:
        ordering = ['name']
        
    def get_absolute_url(self):
        return reverse("faculty:detail", kwargs={'slug': self.slug})

    def __str__(self):
        return self.name
