from django.db import models

GENDER = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'),
    ('OTHER', 'OTHER')
)


class StudentAccount(models.Model):
    user = models.CharField(max_length=200)
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
