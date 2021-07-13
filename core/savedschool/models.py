from django.db import models
from core.schools.models import School
from core.student.models import StudentAccount
from core.schools.models import School
from core.courses.models import Course


class SavedSchool(models.Model):
    student = models.ForeignKey(StudentAccount, on_delete=models.CASCADE, related_name='saved_schools')
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student} {self.school}"