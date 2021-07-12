from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core.scholarships import views


app_name = 'scholarships'

urlpatterns = [
    path('', views.ScholarshipList.as_view(), name='list'),
    path('<slug:slug>', views.ScholarshipDetail.as_view(), name='detail'),
    
]
urlpatterns = format_suffix_patterns(urlpatterns)