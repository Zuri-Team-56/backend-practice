
from core.faculty.models import FacultyName
from django.db import models
from autoslug import AutoSlugField



"""DEPARTMENT MODEL""" #multiple departments
class DepartmentName(models.Model): # Create new department model

    name = models.CharField(max_length=150, help_text='Enter Name of Department', blank=False, unique=True)
    slug = AutoSlugField(populate_from='name', blank=True, editable=True)
    name_of_faculty = models.ForeignKey(FacultyName, related_name="faculty", on_delete=models.CASCADE)
    #body = models.TextField()
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return "{}".format(self.name)
