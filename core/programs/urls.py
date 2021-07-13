from django.urls import path
from . import views


urlpatterns = [
    #School Related URLS
    path('new/', views.CreateProgram.as_view(), name='new'),
    path('', views.GetProgramList.as_view(), name='list'),
    path('update/<slug:slug>/', views.UpdateProgram.as_view(), name='update'),
    path('delete/<slug:slug>/', views.DeleteProgram.as_view(), name='delete'),
    path('view/<slug:slug>/', views.ViewProgram.as_view(), name='view'),

]
