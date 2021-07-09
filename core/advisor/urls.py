from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'careerquestions', views.CareerQuestionViewSet)
router.register(r'careerquestionanswers', views.CareerQuestionAnswerViewSet)
router.register(r'careerquestionoptions', views.CareerQuestionOptionViewSet)


GET_OPTIONS = {'get': 'list'}
urlpatterns = [
    path('', include(router.urls))
]