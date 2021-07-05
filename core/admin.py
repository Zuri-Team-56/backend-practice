from django.contrib import admin
from .models import SavedSchool, StudentAccount
from .models import CareerQuestion
from .models import CareerQuestionAnswer
from .models import SavedSchool

admin.site.register(StudentAccount)
admin.site.register(CareerQuestion)
admin.site.register(CareerQuestionAnswer)
admin.site.register(SavedSchool)