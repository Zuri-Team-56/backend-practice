from django.urls import path
from core.testimonials import views


urlpatterns = [

    path('', views.TestimonialListAPIView.as_view()),
  
]