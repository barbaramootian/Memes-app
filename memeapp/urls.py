from django.urls import path  
from django.contrib import admin  
from . import views  
from django.conf import settings
from django.conf.urls import static
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name='index'),
    path('myimages',views.my_images,name="my_images"),
    path('upload/', views.uploadPicture, name='profile'),
    path('comments/<int:pk>/', views.comment, name='comment'),
    path('like/<int:id>/', views.like_picture, name='like'),
    path('each/<int:id>/', views.each_image, name='eachimage'),
    path('search/', views.search, name='search'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)