from django.contrib import admin
from django.urls import path, include
from home import views
from home.views import book_upload, Explore, Home, register
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.urls import views as auth_views

urlpatterns = [
    path('', views.Home, name='homepage'),
    path('create', views.book_upload, name='create'),
    path('list', views.Explore, name='bookList'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('explore/', views.Explore, name='explore')
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)