from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Define a página inicial do chat
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('policies/', views.policies, name='policies'),


]