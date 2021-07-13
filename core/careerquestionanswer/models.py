from core.careerquestionoption.models import CareerQuestionOption
from django.db import models
from core.student.models import StudentAccount
from core.advisor.models import CareerQuestion
from core.careerquestionoption.models import CareerQuestionOption


class CareerQuestionAnswer(models.Model):
    question = models.ForeignKey(CareerQuestion, on_delete=models.CASCADE, related_name='answers')
    student = models.ForeignKey(StudentAccount, on_delete=models.CASCADE, related_name='career_choices')
    answer = models.ForeignKey(CareerQuestionOption, on_delete=models.CASCADE, related_name="answers")
    
    def __str__(self):
        return self.question