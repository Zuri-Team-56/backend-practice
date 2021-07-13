from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core.comments import views

app_name = 'comments'

urlpatterns = [
    # path('', views.CommentList.as_view(), name='list'),
    # path('<pk>/', views.CommentDetail.as_view(), name='detail'),

    path('<slug:slug>/comments', views.CommentList.as_view(), name='list'),
    path('<slug:slug>/comments/<pk>', views.CommentDetail.as_view(), name='detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)