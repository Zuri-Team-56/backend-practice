from django.urls import path
from core.reviews import views


urlpatterns = [
    path('schools/<int:pk>/reviews/', views.ReviewAPIListView.as_view()),
]