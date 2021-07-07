from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'savedcourses', views.SavedCourseViewSet)


GET_OPTIONS = {'get': 'list'}

urlpatterns = [
    path('', include(router.urls))
]