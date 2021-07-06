from django.contrib import admin
from .models import SavedSchool, StudentAccount
from .models import CareerQuestion
from .models import CareerQuestionAnswer
from .models import SavedCourse, SavedScholarship, CareerQuestionOption

class StudentAccountAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'telephone', 'mobile', 'gender']

admin.site.register(StudentAccount,StudentAccountAdmin)
admin.site.register(CareerQuestion)
admin.site.register(CareerQuestionAnswer)
admin.site.register(SavedSchool)
admin.site.register(SavedScholarship)
admin.site.register(SavedCourse)
admin.site.register(CareerQuestionOption)