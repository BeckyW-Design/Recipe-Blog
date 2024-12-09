from django.urls import path
from . import views


urlpatterns = [
    path('about/', views.recipe_upload, name='about'),
]