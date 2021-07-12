from core.student.models import StudentAccount
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE

GENDER = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'),
    ('OTHER', 'OTHER')
)


class CareerQuestion(models.Model):
    question = models.CharField(max_length=200)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.question

class CareerQuestionOption(models.Model):
    question = models.ForeignKey(CareerQuestion, on_delete=models.CASCADE, related_name='options')
    option = models.CharField(max_length=200)

    def __str__(self):
        return self.option

class CareerQuestionAnswer(models.Model):
    question = models.ForeignKey(CareerQuestion, on_delete=models.CASCADE, related_name='answers')
    student = models.ForeignKey(StudentAccount, on_delete=models.CASCADE, related_name='career_choices')
    answer = models.ForeignKey(CareerQuestionOption, on_delete=models.CASCADE, related_name="answers")
    
    def __str__(self):
        # return self.question
        return str(self.question)