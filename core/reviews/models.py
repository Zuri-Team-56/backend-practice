from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from core.schools.models import School

User = get_user_model()


#from Iconnel
"""REVIEWS MODEL"""
class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(max_length=5000)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    name_of_school = models.ForeignKey(School, on_delete=models.CASCADE)
    educational_status = models.CharField(max_length=150, blank=False)
    rating = models.IntegerField(default=0, 
        validators=[
            MaxValueValidator(5), 
            MinValueValidator(0)
            ]
        )
    date = models.DateField()

    def __str__(self):
        return self.review

