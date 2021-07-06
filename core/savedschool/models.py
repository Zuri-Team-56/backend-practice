from core.schools.models import School
from core.student.models import StudentAccount
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE

GENDER = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'),
    ('OTHER', 'OTHER')
)


class SavedSchool(models.Model):
    student = models.ForeignKey(StudentAccount, on_delete=models.CASCADE, related_name='saved_schools')
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student} {self.school}"
