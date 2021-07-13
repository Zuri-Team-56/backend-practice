from django.urls import path
from core.savedschool.views import SavedSchoolList, SavedSchoolDetail



urlpatterns = [
    path('<int:pk>/', SavedSchoolDetail.as_view()),
    path('', SavedSchoolList.as_view()),
]