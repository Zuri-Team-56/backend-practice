from django.db import models
from core.schools.models import School
from core.student.models import StudentAccount
from django.utils.text import slugify


class SavedSchool(models.Model):
    student = models.ForeignKey(StudentAccount, on_delete=models.CASCADE, related_name='savedschool')
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.student, self.school)