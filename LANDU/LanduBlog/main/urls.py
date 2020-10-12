# -*- coding: utf-8 -*-

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
     path('',views.index),
     path('about',views.about),
     path('image_upload', views.hotel_image_view, name = 'image_upload'), 
     path('success', views.success, name = 'success')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)