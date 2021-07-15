from django.urls import path
from core.savedcourse.views import SavedCourseList, SavedCourseDetail



urlpatterns = [

    path('<slug:slug>/savedcourse', SavedCourseList.as_view()),
    path('<slug:slug>/savedcourse/<pk>', SavedCourseDetail.as_view()),
]