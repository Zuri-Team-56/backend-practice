from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core.articles import views

app_name = 'articles'

urlpatterns = [
    path('', views.ArticleList.as_view(), name='list'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)