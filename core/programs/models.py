from core.schools.models import School

from django.db import models
from autoslug import AutoSlugField


"""PROGRAM MODEL""" 
class Program(models.Model):

    OPTIONS_TITLE = [
        ("nil", "....."),
        ("BSc", "BSc"),
        ("MSc", "MSc"),
        ("PhD", "PhD"),
    ]
    OPTIONS = [
        ("nil", "....."),
        ("Undergraduate", "Undergraduate"),
        ("Postgraduate", "Postgraduate"),
        ("Doctorate", "Doctorate"),
    ]
    
    name = models.CharField(max_length=200, help_text='Enter Name of Program', blank=False, unique=True )
    title = models.CharField(max_length=100, choices=OPTIONS_TITLE, help_text='Enter Title of Program', null=True, blank=False, unique=False)
    type = models.CharField(max_length=150, choices=OPTIONS, help_text='Enter Name of Program', blank=False, unique=False)
    slug = AutoSlugField(populate_from='name', unique=True, blank=True, editable=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True, related_name="programs")
    information = models.TextField()
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return "{}".format(self.name)
