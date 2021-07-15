from django.db import models
from core.student.models import StudentAccount
from core.scholarships.models import Scholarship


class SavedScholarship(models.Model):
    student = models.ForeignKey(StudentAccount, on_delete=models.CASCADE, related_name='savedscholarship')
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE)
    # slug = models.SlugField(max_length=255, unique=True, blank=True, editable=True)


    def __str__(self):
        return '{} {}'.format(self.student, self.scholarship)

    # def __str__(self):
#         return f"{self.student} {self.scholarship}"

