from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('add/', views.add_recipe, name='recipe_add'),
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'),
]
