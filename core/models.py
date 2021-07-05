from django.contrib.auth.models import User
from django.db import models

GENDER = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'),
    ('OTHER', 'OTHER')
)


class StudentAccount(models.Model):
    # user = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    gender = models.CharField(max_length=50, choices=GENDER)

    def __str__(self):
        return self.user

class CareerQuestion(models.Model):
    question = models.CharField(max_length=200)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.question

class CareerQuestionAnswer(models.Model):
    question = models.CharField(max_length=255)
    student = models.CharField(max_length=255)
    answer = models.TextField(max_length=255, null=True)

    def __str__(self):
        return self.question

class SavedSchool(models.Model):
    student = models.CharField(max_length=255)
    school = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.school