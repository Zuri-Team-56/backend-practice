from django.urls import path
from core.reviews import views


urlpatterns = [
    # path('<int:pk>/reviews/', views.ReviewAPIListView.as_view()),
    path('', views.ReviewAPIListView.as_view()),
    
]