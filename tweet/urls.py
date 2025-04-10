from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.tweetList, name='tweetList'),
    path('create/', views.tweetCreate, name='tweetCreate'),
    path('<int:tweetID>/edit/', views.tweetEdit, name='tweetEdit'),
    path('<int:tweetID>/delete/', views.tweetDelete, name='tweetDelete'),
    path('register/', views.register, name='register'),
    path('abouts/', views.abouts, name='abouts'),
]