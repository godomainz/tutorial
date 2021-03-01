from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views


urlpatterns = [
    path('', views.snippet_list),
    path('<int:pk>/', views.snippet_detail),
]