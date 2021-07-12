from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core.faculty import views

app_name = 'faculty'

urlpatterns = [
    path('', views.FacultyList.as_view(), name='list'),
    path('<slug:slug>/', views.FacultyDetail.as_view(), name='detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)