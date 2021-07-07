from core.schools.models import School
from django.db import models
from autoslug import AutoSlugField


"""TUITION"""
class Tuition(models.Model):

 
    title = models.CharField(max_length=200, null=True, blank=True)
    slug = AutoSlugField(populate_from='title', blank=True, editable=True)
    school_name = models.ForeignKey(School, on_delete=models.CASCADE, related_name="fees")
    undergraduate_tuition = models.TextField()
    undergraduate_fee = models.DecimalField(verbose_name="Undergraduate fee", help_text="Maximum 999.99", max_digits=5, decimal_places=2)
    postgraduate_tuition = models.TextField()
    postgraduate_fee = models.DecimalField(verbose_name="Postgraduate fee", help_text="Maximum 999.99", max_digits=5, decimal_places=2)
    website = models.URLField(max_length=234, null=True, blank=True)
    
    def __str__(self):
        return self.title