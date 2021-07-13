from django.db import models
from core.student.models import StudentAccount

class CareerQuestion(models.Model):
    question = models.CharField(max_length=200)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.question

# class CareerQuestionOption(models.Model):
#     question = models.ForeignKey(CareerQuestion, on_delete=models.CASCADE, related_name='options')
#     option = models.CharField(max_length=200)

#     def __str__(self):
#         return self.option

# class CareerQuestionAnswer(models.Model):
#     question = models.ForeignKey(CareerQuestion, on_delete=models.CASCADE, related_name='answers')
#     student = models.ForeignKey(StudentAccount, on_delete=models.CASCADE, related_name='career_choices')
#     answer = models.ForeignKey(CareerQuestionOption, on_delete=models.CASCADE, related_name="answers")
    
#     def __str__(self):
#         return self.question