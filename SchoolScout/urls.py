"""SchoolScout URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', lambda request: redirect('admin/', permanent=False)),
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),

    path('auth/', include('user_auth.urls')),
    
    path('articles/', include('core.articles.urls')),
    path('advisor/', include('core.advisor.urls')), 
    path('comments/', include('core.comments.urls')),
    path('courses/', include('core.courses.urls')),
    path('department/', include('core.department.urls')),
    path('faculty/', include('core.faculty.urls')),
    path('fees/', include('core.fees.urls')),
    # path('location/', include('core.location.urls')),
    path('news/', include('core.news.urls')),
    path('requirement/', include('core.requirement.urls')),
    path('reviews/', include('core.reviews.urls')),
    path('savedcourse/', include('core.savedcourse.urls')),
    path('savedscholarship/', include('core.savedscholarship.urls')),
    path('savedschool/', include('core.savedschool.urls')),
    path('scholarships/', include('core.scholarships.urls')),  
    path('schools/', include('core.schools.urls')),
    path('student/', include('core.student.urls')),
    path('testimonials/', include('core.testimonials.urls')),
    path('programs/', include('core.programs.urls')),          
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(template_name='swagger-ui.html', url_name='schema'), name='swagger-ui')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if not settings.DEBUG:
    # urlpatterns += static('', (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),)
    # urlpatterns += patterns('', (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),)