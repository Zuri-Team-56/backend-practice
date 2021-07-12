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
    

    title = models.CharField(max_length=100, choices=OPTIONS_TITLE, help_text='Enter Title of Program', null=True, blank=True, unique=True)
    name = models.CharField(max_length=150, choices=OPTIONS, help_text='Enter Name of Program', blank=False, unique=True)
    slug = AutoSlugField(populate_from='name', blank=True, editable=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True, related_name="programs")
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return "{}".format(self.name)
