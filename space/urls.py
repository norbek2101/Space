from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),

    path('projects/', projects, name='projects'),
    path('project_detail/<int:pk>/', project_detail, name='project_detail'),
    path('blog/', blog, name='blog'),
    path('blog_detail/<int:pk>/', blog_detail, name='blog_detail'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)