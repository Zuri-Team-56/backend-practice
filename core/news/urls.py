from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core.news import views

app_name = 'news'

urlpatterns = [
    path('', views.NewsList.as_view(), name='list'),
    path('<slug:slug>', views.NewsDetail.as_view(), name='detail'),

    # path('<slug:slug>/news', views.NewsList.as_view(), name='list'),
    # path('<slug:slug>/news/<slug:slug>', views.NewsDetail.as_view(), name='detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)