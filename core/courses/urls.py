
from django.urls import path
from . import views


urlpatterns = [
    # Course Relate URLS
    path('new/', views.CreateCourseViews.as_view(), name='new'),
    path('', views.GetCourseListViews.as_view(), name='list'),
    path('update/<slug:slug>/', views.UpdateCourseViews.as_view(), name='update'),
    path('delete/<slug:slug>/', views.DeleteCourseViews.as_view(), name='delete'),
    path('<slug:slug>/', views.ViewCourseViews.as_view(), name='view'),
]