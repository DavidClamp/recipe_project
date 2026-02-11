from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from .models import Recipe

class RecipeList(generic.ListView):
    """Displays a list of recipes."""
    queryset = Recipe.objects.all()
    template_name = "center/index.html"
    context_object_name = "recipe_list"
    paginate_by = 6

def recipe_detail(request, slug):
    """Displays an individual recipe."""
    recipe = get_object_or_404(Recipe, slug=slug)
    return render(request, "center/recipe_detail.html", {"recipe": recipe})

@login_required
def add_recipe(request):
    """Creates a new recipe manually from POST data."""
    if request.method == "POST":
        title = request.POST.get("title")
        recipe = Recipe.objects.create(
            title=title,
            slug=slugify(title),
            author=request.user,
            description=request.POST.get("description"),
            ingredients=request.POST.get("ingredients"),
            instructions=request.POST.get("instructions"),
            status=1,
        )
        messages.success(request, f'Recipe "{title}" created successfully!')
        return redirect("recipe_detail", slug=recipe.slug)
    return render(request, "center/add_recipe.html")

@login_required
def edit_recipe(request, slug):
    """Updates an existing recipe."""
    recipe = get_object_or_404(Recipe, slug=slug)
    
    # Security: Only allow the author to edit
    if recipe.author != request.user:
        messages.error(request, "Permission denied.")
        return redirect("home")

    if request.method == "POST":
        recipe.title = request.POST.get("title")
        recipe.slug = slugify(recipe.title)  # Keep slug in sync with title
        recipe.description = request.POST.get("description")
        recipe.ingredients = request.POST.get("ingredients")
        recipe.instructions = request.POST.get("instructions")
        recipe.save()
        
        messages.success(request, f'Recipe "{recipe.title}" updated!')
        return redirect("recipe_detail", slug=recipe.slug)
    return render(request, "center/edit_recipe.html", {"recipe": recipe})

@login_required
def delete_recipe(request, slug):
    """Deletes a recipe via POST confirmation."""
    recipe = get_object_or_404(Recipe, slug=slug)
    
    if recipe.author != request.user:
        messages.error(request, "Permission denied.")
        return redirect("home")

    if request.method == "POST":
        recipe.delete()
        messages.success(request, "Recipe deleted successfully!")
        return redirect("home")
    return render(request, "center/delete_recipe.html", {"recipe": recipe})
