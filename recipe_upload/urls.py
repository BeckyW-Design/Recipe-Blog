from . import views
from django.urls import path

urlpatterns = [
    path('', views.recipe_upload, name='recipe_upload'),
]