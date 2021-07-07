from django.db import models
from autoslug import AutoSlugField
from core.schools.models import School



"""SCHOOL NEWS MODEL""" 
class SchoolNews(models.Model): # Create school news articles

    category = models.CharField(max_length=150, help_text='Enter Name of category', blank=False, unique=True)
    title = models.CharField(max_length=150, help_text='Enter title', blank=False, unique=True)
    slug = AutoSlugField(populate_from='title', blank=True, editable=True)
    school_name = models.ForeignKey(School, on_delete=models.CASCADE, related_name="news")
    
    information = models.TextField()
    date = models.DateField()
    
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return "{}".format(self.title)

