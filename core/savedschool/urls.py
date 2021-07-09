from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'savedschools', views.SavedSchoolViewSet)

GET_OPTIONS = {'get': 'list'}

urlpatterns = [
    path('', include(router.urls))
]