from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core.department import views

app_name = 'department'

urlpatterns = [
    path('', views.DepartmentList.as_view(), name='list'),
    path('<slug:slug>', views.DepartmentDetail.as_view(), name='detail'),

    # path('<slug:slug>/department', views.DepartmentList.as_view(), name='list'),
    # path('<slug:slug>/department/<slug:slug>', views.DepartmentDetail.as_view(), name='detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)