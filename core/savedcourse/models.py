from django.db import models
from core.student.models import StudentAccount
from core.courses.models import Course


class SavedCourse(models.Model):
    student = models.ForeignKey(StudentAccount, on_delete=models.CASCADE, related_name='savedcourse')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    @property
    def __str__(self):
        return f"{self.student} {self.course}"

    def __str__(self):
        return '{} {}'.format(self.student, self.course)
    