from django.urls import path
from core.savedscholarship.views import SavedScholarshipList, SavedScholarshipDetail


urlpatterns = [
   
    path('<slug:slug>/savedscholarship', SavedScholarshipList.as_view()),
    path('<slug:slug>/savedscholarship/<pk>', SavedScholarshipDetail.as_view()),


]