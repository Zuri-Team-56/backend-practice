from django.db import models
from autoslug import AutoSlugField
from core.faculty.models import FacultyName
from core.requirement.models import EntryRequirement
from core.fees.models import Tuition
from core.news.models import SchoolNews


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
    faculty_name = models.ForeignKey(FacultyName,  related_name='faculty', on_delete=models.DO_NOTHING, null=True, blank=True)
    world_ranking =  models.IntegerField(null=True, blank=True)
    website = models.URLField(max_length=234, null=True, blank=True)
    number_of_students = models.IntegerField(null=True, blank=True)
    tuition_information = models.ForeignKey(Tuition,  related_name='tuition', on_delete=models.DO_NOTHING, null=True, blank=True)
    financial_aid = models.TextField()
    entry_requirements = models.ForeignKey(EntryRequirement,  related_name='requirement', on_delete=models.DO_NOTHING, null=True, blank=True)
    hostel = models.TextField()
    has_hostel = models.BooleanField(default=True)
    location = models.CharField(max_length=200, null=True, blank=False)
    school_news = models.ForeignKey(SchoolNews, related_name='school_news', on_delete=models.DO_NOTHING, null=True, blank=True)

    
    def __str__(self):
        return self.name