from django.urls import path
from core.savedscholarship.views import SavedScholarshipList, SavedScholarshipDetail



urlpatterns = [
    path('<int:pk>/', SavedScholarshipDetail.as_view()),
    path('', SavedScholarshipList.as_view()),
]