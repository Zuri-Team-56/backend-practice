from django.urls import path
from core.student.views import StudentAccountList, StudentAccountDetail#, UserList, UserDetail


urlpatterns = [
   
    path('<slug:slug>/', StudentAccountDetail.as_view()),
    path('', StudentAccountList.as_view()),
]
