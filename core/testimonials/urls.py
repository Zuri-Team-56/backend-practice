from django.urls import path
from core.testimonials import views


urlpatterns = [

    path('testimonials/', views.TestimonialListAPIView.as_view()),
  
]