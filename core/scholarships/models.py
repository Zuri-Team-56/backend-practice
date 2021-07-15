from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from core.schools.models import School


"""SCHOLARSHIP MODEL"""
#options for scholarship class
class Scholarship(models.Model): # Create new scholarship model

    name = models.CharField(max_length=150, help_text='Enter Name of Scholarship', blank=False, unique=True)
    description = models.TextField()
    slug = AutoSlugField(populate_from='name', unique=True, blank=True, editable=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    requirements = models.TextField(verbose_name=('Application requirements'))
    snippets = models.CharField(max_length=350)
    school = models.ForeignKey(School, related_name='scholarships', on_delete=models.CASCADE, null=True, blank=True) 
    website = models.URLField(max_length=350, help_text='Enter scholarship application website link', blank=True, unique=True)
    whatsapp = models.URLField(max_length=350, help_text='Enter scholarship Whatsapp link', blank=True, unique=True)
    instagram = models.URLField(max_length=350, help_text='Enter scholarship Instagram link', blank=True, unique=True)
    facebook = models.URLField(max_length=350, help_text='Enter scholarship Faceook link', blank=True, unique=True)
    twitter = models.URLField(max_length=350, help_text='Enter scholarship Twitter link', blank=True, unique=True)
    date = models.DateField()
    saved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-date']
    
    def get_absolute_url(self):
        return reverse("scholarships:detail", kwargs={'slug': self.slug})

    def __str__(self):
        return self.name
