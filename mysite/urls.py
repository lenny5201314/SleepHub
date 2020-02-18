"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from music_app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('signup/', views.signup,name='signup'),
    path('signin/', views.signin,name='signin'),
    path('logout/', views.user_logout,name='logout'),
    path('discover/', views.discover,name='discover'),
    path('genres/', views.genres,name='genres'),
    path('music_app/', include('music_app.urls')),
    path('item.detail/<int:pk>/', views.music_detail, name='detail'),
    path('post/log', views.log, name='log'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
