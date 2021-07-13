from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core.requirement import views

app_name = 'requirement'

urlpatterns = [
    path('', views.RequirementList.as_view(), name='list'),
    path('<slug:slug>', views.RequirementDetail.as_view(), name='detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)