from django.urls import path
from . import views

urlpatterns = [
    path('<int:recipe_id>/', views.detail, name='detail-page'),
    path('', views.Recipes, name = 'home-page'), #added the views function into the url
    
]