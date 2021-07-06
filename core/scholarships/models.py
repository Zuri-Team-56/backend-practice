from django.db import models
from autoslug import AutoSlugField
from core.schools.models import School


"""SCHOLARSHIP MODEL"""
#options for scholarship class
class Scholarship(models.Model): # Create new scholarship model


    name = models.CharField(max_length=250, help_text='Enter Name of Scholarship', blank=False, unique=True)
    description = models.TextField()
    slug = AutoSlugField(populate_from='name', blank=True, editable=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    requirements = models.TextField(verbose_name=('Application requirements'))
    institutition = models.ForeignKey(School, related_name='school', on_delete=models.CASCADE, null=True, blank=True) 
    website = models.URLField(max_length=350, help_text='Enter scholarship application website link', blank=True, unique=True)
    website = models.URLField(max_length=350, help_text='Enter scholarship Whatsapp link', blank=True, unique=True)
    website = models.URLField(max_length=350, help_text='Enter scholarship Instagram link', blank=True, unique=True)
    website = models.URLField(max_length=350, help_text='Enter scholarship Faceook link', blank=True, unique=True)
    website = models.URLField(max_length=350, help_text='Enter scholarship Twitter link', blank=True, unique=True)
    date = models.DateField()


    class Meta:
        ordering = ['-date']

    def __str__(self):
        return "{}".format(self.name)
