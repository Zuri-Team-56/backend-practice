
from core.schools.models import School
from django.db import models
from autoslug import AutoSlugField


"""FACULTY MODEL""" 
class FacultyName(models.Model): # Create new faculty model

    name = models.CharField(max_length=150, help_text='Enter Name of Faculty', blank=False, unique=True)
    slug = AutoSlugField(populate_from='name', blank=True, editable=True)
    name_of_school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True, related_name="faculties")
    #body = models.TextField()
    
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return "{}".format(self.name)
