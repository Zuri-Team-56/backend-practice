from django.contrib.auth.models import User
from django.db import models

GENDER = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'),
    ('OTHER', 'OTHER')
)


class StudentAccount(models.Model):
    # user = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_accounts')
    telephone = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    gender = models.CharField(max_length=50, choices=GENDER)

    @property
    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        return self.user.first_name

class CareerQuestion(models.Model):
    question = models.CharField(max_length=200)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.question

class CareerQuestionAnswer(models.Model):
    question = models.CharField(max_length=255)
    student = models.CharField(max_length=255)
    answer = models.TextField(max_length=255, null=True)  # This needs to be a foreignkey

    def __str__(self):
        return self.question

class SavedSchool(models.Model):
    student = models.CharField(max_length=255)
    school = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.school