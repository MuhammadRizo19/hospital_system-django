from django.urls import path
from .views import (
	CreateRecipeView,
	RecipeDetailView,
	RecipeListView,
	UpdateRecipeView,
	DeleteRecipeView,
	SearchRecipeView,
	PrintRecipeView
	)

urlpatterns = [
    path('new/', CreateRecipeView.as_view(), name='create_recipe'),
    path('<uuid:pk>/detail', RecipeDetailView.as_view(),name='recipe_detail'),
    path('recipe_list/', RecipeListView.as_view(), name='recipe_list'),
    path('<uuid:pk>/update', UpdateRecipeView.as_view(),name='update_recipe'),
    path('search_recipe/', SearchRecipeView.as_view(), name='search_recipe'),
    path('<uuid:pk>/delete', DeleteRecipeView.as_view(), name='delete_recipe'),
    path('<uuid:pk>/print_recipe/', PrintRecipeView.as_view(), name='print_recipe'),
]
