"""todoList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from home import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('',views.home,name='home'),
    path('tasks',views.tasks,name='tasks'),
    path('imagec',views.imagec,name='imagec'),
    path('text_to_voice',views.text_to_voice,name='text_to_voice'),
    path('gif_to_text',views.gif_to_text,name='gif_to_text'),
    path('gif_text',views.gif_text,name='gif_text'),
    path('translate_to_text',views.translate_to_text,name='translate_to_text'),
    path('imgtrans',views.imgtrans,name='imgtrans'),
    path('imgtospeech',views.imgtospeech,name='imgtospeech'),
    path('feat',views.feature,name='feat')


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
