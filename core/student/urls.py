from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'studentaccounts', views.StudentAccountViewSet)
router.register(r'users', views.UserViewSet)


GET_OPTIONS = {'get': 'list'}
urlpatterns = [
    path('', include(router.urls))
]