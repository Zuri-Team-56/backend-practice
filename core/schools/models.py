from django.db import models
from autoslug import AutoSlugField


"""SCHOOL MODEL"""
class School(models.Model):

    OPTIONS = [
        ("nil", "....."),
        ("BSc", "Bachelor's Degree"),
        ("MSc", "Master's Degree"),
        ("PhD", "Doctorate Degree"),
        ("HND", "Higher National Diploma"),
        ("OND", "Ordinary National Diploma"),
        ("ALL", "All"),
    ]
    
 
    name = models.CharField(max_length=200, null=True, blank=True)
    slug = AutoSlugField(populate_from='name', blank=True, editable=True)
    overview = models.TextField()
    program = models.CharField(max_length=200, choices=OPTIONS, default='.....', blank=False)
    image = models.FileField(upload_to=None, null=True, blank=True)
    world_ranking =  models.IntegerField(null=True, blank=True)
    website = models.URLField(max_length=234, null=True, blank=True)
    number_of_students = models.IntegerField(null=True, blank=True)
    financial_aid = models.TextField()    
    hostel = models.TextField()
    has_hostel = models.BooleanField(default=True)
    location = models.CharField(max_length=200, null=True, blank=False)

    
    def __str__(self):
        return self.name