from core.programs.models import Program
from core.department.models import Department
from django.db import models
from autoslug import AutoSlugField
from core.schools.models import School


"""COURSE MODEL"""
class Course(models.Model):
   
    course_name = models.CharField(max_length=200, null=True, blank=True, default='')
    slug = AutoSlugField(populate_from='course_name', blank=True, editable=True)
    school_name = models.ForeignKey(School, related_name='courses', on_delete=models.CASCADE, null=True, blank=True)
    image = models.FileField(upload_to=None, null=True, blank=True)
    course_requirements = models.TextField()
    program = models.ForeignKey(Program, related_name='courses', on_delete=models.CASCADE, null=True, blank=True)
    name_of_department = models.ForeignKey(Department, related_name="department", on_delete=models.CASCADE)
    school_location = models.CharField(max_length=200, null=True, blank=True, default='')
    bookmarkIcon = models.BooleanField(default=False)
    tuition = models.CharField(max_length=200, null=True, blank=True, default='')
    tution_price = models.CharField(max_length=200, null=True, blank=True, default='')
    address = models.TextField()
    addressState = models.CharField(max_length=200, null=True, blank=True, default='')
    duration = models.CharField(max_length=200, null=True, blank=True, default='')
    durationYears = models.CharField(max_length=200, null=True, blank=True, default='')
    compare = models.CharField(max_length=200, null=True, blank=True, default='')

    
    
    def __str__(self):
        return self.course_name
