from core.student.models import StudentAccount
from core.courses.models import Course

from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE


GENDER = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'),
    ('OTHER', 'OTHER')
)



class SavedCourse(models.Model):
    student = models.ForeignKey(StudentAccount, on_delete=models.CASCADE, related_name='saved_courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    @property
    def __str__(self):
        return f"{self.student} {self.course}"

    def __str__(self):
        return self.user.student

