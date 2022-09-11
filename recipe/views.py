from django.shortcuts import render
from django.views import generic
from .models import Recipe
from .forms import RecipeForm
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class CreateRecipeView(LoginRequiredMixin, generic.CreateView):
	model = Recipe
	template_name = 'recipe/create_recipe.html'
	form_class = RecipeForm
	context_object_name = 'recipe'
	login_url = 'account_login'

class RecipeDetailView(LoginRequiredMixin, generic.DeleteView):
	model = Recipe
	template_name = 'recipe/recipe_detail.html'
	context_object_name = 'recipe'
	login_url = 'account_login'

class RecipeListView(LoginRequiredMixin, generic.ListView):
	model = Recipe
	template_name = 'recipe/recipe_list.html'
	context_object_name = 'recipe_list'
	paginate_by = 5
	login_url = 'account_login'

class UpdateRecipeView(LoginRequiredMixin, generic.UpdateView):
	model = Recipe
	template_name = 'recipe/update_recipe.html'
	form_class = RecipeForm
	login_url = 'account_login'

class DeleteRecipeView(LoginRequiredMixin, generic.DeleteView):
	model = Recipe
	template_name = 'recipe/delete_recipe.html'
	success_url = reverse_lazy('recipe_list')
	login_url = 'account_login'

class PrintRecipeView(LoginRequiredMixin, generic.DetailView):
	model = Recipe
	template_name = 'recipe/print_recipe.html'
	contextual_object_name = 'recipe'
	login_url = 'account_login'

class SearchRecipeView(LoginRequiredMixin, generic.ListView):
	model = Recipe
	context_object_name = 'recipe_list'
	template_name = 'recipe/search_recipe.html'
	login_url = 'account_login'

	def get_queryset(self): 
		query = self.request.GET.get('recipe')
		return Recipe.objects.filter(Q(bemor__icontains=query) | Q(diagnoz__icontains=query)
		)