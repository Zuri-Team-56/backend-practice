from django.urls import path
from core.savedcourse.views import SavedCourseList, SavedCourseDetail



urlpatterns = [
    path('<int:pk>/', SavedCourseDetail.as_view()),
    path('', SavedCourseList.as_view()),
]