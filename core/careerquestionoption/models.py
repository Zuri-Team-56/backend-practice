from django.db import models
from core.student.models import StudentAccount
from core.advisor.models import CareerQuestion

class CareerQuestionOption(models.Model):
    question = models.ForeignKey(CareerQuestion, on_delete=models.CASCADE, related_name='options')
    option = models.CharField(max_length=200)

    def __str__(self):
        return self.option