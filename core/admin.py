from django.contrib import admin
from .models import SavedSchool, StudentAccount
from .models import CareerQuestion
from .models import CareerQuestionAnswer
from .models import SavedSchool

class StudentAccountAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'telephone', 'mobile', 'gender']

admin.site.register(StudentAccount,StudentAccountAdmin)
admin.site.register(CareerQuestion)
admin.site.register(CareerQuestionAnswer)
admin.site.register(SavedSchool)