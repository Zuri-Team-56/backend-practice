from core.schools.models import School
from django.db import models
from autoslug import AutoSlugField


PROGRAM_TYPES = (
    ("Undergrad", "Undergraduate Degree"),
    ("Postgrad", "Post graduate Degree"),
    ("Doctorate", "Doctorate Degree"),
)


"""TUITION"""
class Tuition(models.Model):
 
    title = models.CharField(max_length=200, null=True, blank=True)
    slug = AutoSlugField(populate_from='title', blank=True, editable=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="fees")
    program = models.CharField(max_length=200, choices=PROGRAM_TYPES)
    description = models.TextField()
    amount = models.DecimalField(verbose_name="Tuition Amount", help_text="Maximum 99999999.99", max_digits=9, decimal_places=2)
    website = models.URLField(max_length=234, null=True, blank=True)
    
    def __str__(self):
        return self.title
