from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('edit/<slug:slug>/', views.edit_recipe, name='edit_recipe'),
    path('delete/<slug:slug>/', views.delete_recipe, name='delete_recipe'),
]
