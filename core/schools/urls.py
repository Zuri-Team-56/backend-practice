from django.urls import path
from . import views


urlpatterns = [
     #School Related URLS
    path('new/', views.CreateSchoolViews.as_view(), name='new'),
    path('', views.GetSchoolListViews.as_view(), name='list'),
    path('update/<slug:slug>/', views.UpdateSchoolViews.as_view(), name='update'),
    path('delete/<slug:slug>/', views.DeleteSchoolViews.as_view(), name='delete'),
    path('<slug:slug>/', views.ViewSchoolViews.as_view(), name='view'),

]
