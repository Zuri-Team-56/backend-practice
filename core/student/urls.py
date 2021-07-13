from django.urls import path
from core.student.views import StudentAccountList, StudentAccountDetail, UserList, UserDetail



urlpatterns = [
    path('users/', UserList.as_view()), # new
    path('users/<int:pk>/', UserDetail.as_view()), # new
    path('<int:pk>/', StudentAccountDetail.as_view()),
    path('', StudentAccountList.as_view()),
]
