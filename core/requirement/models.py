from core.schools.models import School
from django.db import models
from autoslug import AutoSlugField

class EntryRequirement(models.Model):
    
    title = models.CharField(max_length=200, null=True, blank=True)
    slug = AutoSlugField(populate_from='title', blank=True, editable=True)
    school_name = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True, related_name="requirements")
    entry_requirements = models.TextField(max_length=5000)

    def __str__(self):
        return self.entry_requirements   