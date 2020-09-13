from django.urls import path 
from . import views

app_name = 'productapp'
urlpatterns = [
    path('home/', views.home , name = 'home'),
]