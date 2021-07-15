from django.urls import path
from core.savedschool.views import SavedSchoolList, SavedSchoolDetail



urlpatterns = [
    
    path('<slug:slug>/savedschool/<pk>', SavedSchoolDetail.as_view()),
    path('<slug:slug>/savedschool', SavedSchoolList.as_view()),
]