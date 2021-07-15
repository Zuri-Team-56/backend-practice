from django.urls import path
from core.advisor.views import CareerQuestionList, CareerQuestionDetail#,\
   # CareerQuestionAnswerList, CareerQuestionAnswerDetail,\
        # CareerQuestionOptionList, CareerQuestionOptionDetail



urlpatterns = [
    # path('answers/', CareerQuestionAnswerList.as_view()), # new
    # path('answers/<int:pk>/', CareerQuestionAnswerDetail.as_view()), # ne
    # path('options/', CareerQuestionOptionList.as_view()), # new
    # path('options/<int:pk>/', CareerQuestionOptionDetail.as_view()), # new
    path('<int:pk>/', CareerQuestionDetail.as_view()),
    path('', CareerQuestionList.as_view()),
]

