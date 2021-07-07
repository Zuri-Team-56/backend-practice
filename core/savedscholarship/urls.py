from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'savedscholarships', views.SavedScholarshipViewSet)


GET_OPTIONS = {'get': 'list'}
urlpatterns = [
    path('', include(router.urls))
]