# from django.urls import path, include
# from .views import DetailCareerQuestion, ListStudentAccount, DetailStudentAccount, ListCareerQuestion, DetailCareerQuestion

# urlpatterns = [
#     path('<int:pk>/', DetailStudentAccount.as_view()),
#     path('', ListStudentAccount.as_view()),
#     path('careerquestion/', ListCareerQuestion.as_view()),
#     path('detailcareerquestion/', DetailCareerQuestion.as_view())
# ]

from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'studentaccounts', views.StudentAccountViewSet)
router.register(r'careerquestions', views.CareerQuestionViewSet)
router.register(r'careerquestionanswers', views.CareerQuestionAnswerViewSet)
router.register(r'savedschools', views.SavedSchoolViewSet)
router.register(r'users', views.UserViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
GET_OPTIONS = {'get': 'list'}
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('careerquestions/', views.CareerQuestionViewSet.as_view(GET_OPTIONS), name='careerquestions')
]