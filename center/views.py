from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeForm # Ensure you have a RecipeForm in forms.py

class RecipeList(generic.ListView):
    queryset = Recipe.objects.all().order_by("-updated_at")
    template_name = "center/index.html"
    context_object_name = "recipe_list"
    paginate_by = 6

def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    return render(request, "center/recipe_detail.html", {"recipe": recipe})

@login_required
def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.status = 1
            recipe.save()
            messages.success(request, f'Recipe "{recipe.title}" created!')
            return redirect("recipe_detail", slug=recipe.slug)
    else:
        form = RecipeForm()
    return render(request, "center/add_recipe.html", {"form": form})

@login_required
def edit_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    
    # Defensive Programming: Only author can edit
    if recipe.author != request.user:
        messages.error(request, "You can only edit your own recipes.")
        return redirect("home")

    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, f'"{recipe.title}" updated successfully!')
            return redirect("recipe_detail", slug=recipe.slug)
    else:
        # This pre-fills the form for the Edit page
        form = RecipeForm(instance=recipe)
        
    return render(request, "center/edit_recipe.html", {"recipe": recipe, "form": form})

@login_required
def delete_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    if recipe.author != request.user:
        messages.error(request, "Permission denied.")
        return redirect("home")
    
    if request.method == "POST":
        recipe.delete()
        messages.success(request, "Recipe deleted successfully!")
        return redirect("home")
    return render(request, "center/delete_recipe.html", {"recipe": recipe})

