from django.urls import path
from core.careerquestionoption.views import CareerQuestionOptionList, CareerQuestionOptionDetail




urlpatterns = [
    path('<int:pk>/', CareerQuestionOptionDetail.as_view()),
    path('', CareerQuestionOptionList.as_view()),
]