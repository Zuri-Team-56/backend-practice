from django.db import models
from autoslug import AutoSlugField



"""SCHOOL MODEL"""
class School(models.Model): 
    name = models.CharField(max_length=200, unique=True, null=True, blank=True)
    slug = AutoSlugField(populate_from='name', unique=True, blank=True, editable=True)
    overview = models.TextField()
    image = models.FileField(upload_to=None, null=True, blank=True)
    program = models.TextField()
    world_ranking =  models.IntegerField(null=True, blank=True)
    website = models.URLField(max_length=234, null=True, blank=True)
    number_of_students = models.IntegerField(null=True, blank=True)
    tuition = models.TextField()
    financial_aid = models.TextField()
    hostel = models.TextField()
    has_hostel = models.BooleanField(default=True)
    location = models.CharField(max_length=200, null=True, blank=False)

    def __str__(self):
        return self.name

    