from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'studentaccounts', views.StudentAccountViewSet)
router.register(r'careerquestions', views.CareerQuestionViewSet)
router.register(r'careerquestionanswers', views.CareerQuestionAnswerViewSet)
router.register(r'savedschools', views.SavedSchoolViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'savedcourses', views.SavedCourseViewSet)
router.register(r'savedscholarships', views.SavedScholarshipViewSet)
router.register(r'careerquestionoptions', views.CareerQuestionOptionViewSet)


GET_OPTIONS = {'get': 'list'}
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]