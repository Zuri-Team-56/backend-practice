
from django.urls import path
from . import views


urlpatterns = [
    # Course Relate URLS
    path('create-course/', views.CreateCourseViews.as_view(), name='create-course'),
    path('get-course-list/', views.GetCourseListViews.as_view(), name='get-course-list'),
    path('update-course/<int:pk>/', views.UpdateCourseViews.as_view(), name='update-course'),
    path('delete-course/<int:pk>/', views.DeleteCourseViews.as_view(), name='delete-course'),
    path('view-course/<int:pk>/', views.ViewCourseViews.as_view(), name='view-course'),
]