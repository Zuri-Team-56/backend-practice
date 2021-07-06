from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE

GENDER = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'),
    ('OTHER', 'OTHER')
)


class StudentAccount(models.Model):
    # user = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_accounts')
    telephone = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    gender = models.CharField(max_length=50, choices=GENDER)

    @property
    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        return self.user.first_name

class School(models.Model):
    pass

class Course(models.Model):
    pass

class Scholarship(models.Model):
    pass

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
        return self.question

class SavedSchool(models.Model):
    student = models.ForeignKey(StudentAccount, on_delete=models.CASCADE, related_name='saved_schools')
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student} {self.school}"

class SavedCourse(models.Model):
    student = models.ForeignKey(StudentAccount, on_delete=models.CASCADE, related_name='saved_courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student} {self.course}"

class SavedScholarship(models.Model):
    student = models.ForeignKey(StudentAccount, on_delete=models.CASCADE, related_name='saved_scholarships')
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student} {self.scholarship}"