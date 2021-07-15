from django.urls import path
from core.careerquestionanswer.views import CareerQuestionAnswerList, CareerQuestionAnswerDetail




urlpatterns = [
    path('<int:pk>/', CareerQuestionAnswerDetail.as_view()),
    path('', CareerQuestionAnswerList.as_view()),
]