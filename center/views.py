from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Recipe
from django.utils.text import slugify
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required



# Create your views here.
class RecipeList(generic.ListView):
    queryset = Recipe.objects.all()
    template_name = "center/index.html"
    context_object_name = "recipe_list"
    paginate_by = 6


def recipe_detail(request, slug):
    """
    Display an individual :model:`center.Recipe`.

    **Context**

    ``recipe``
        An instance of :model:`center.Recipe`.

    **Template:**

    :template:`center/recipe_detail.html`
    """

    queryset = Recipe.objects.all()
    recipe = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "center/recipe_detail.html",
        {"recipe": recipe},
    )
# add a recipe

@login_required
def add_recipe(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        ingredients = request.POST.get("ingredients")
        instructions = request.POST.get("instructions")
      

        # Create the recipe and generate a slug manually
        recipe = Recipe.objects.create(
            title=title,
            slug=slugify(title),  # Converts "My Recipe" to "my-recipe"
            author=request.user,
            description=description,
            ingredients=ingredients,
            instructions=instructions,
            status=1,
        )
        # Use redirect instead of render to prevent form resubmission on refresh
        return redirect("recipe_detail", slug=recipe.slug)

    return render(request, "center/add_recipe.html")

# edit a recipe 

@login_required
def edit_recipe(request, slug):
    #Fetch the existing recipe
    recipe = get_object_or_404(Recipe, slug=slug)

    if request.method == "POST":
        # Update the object fields
        recipe.title = request.POST.get("title")
        recipe.description = request.POST.get("description")
        recipe.ingredients = request.POST.get("ingredients")
        recipe.instructions = request.POST.get("instructions")
        
        # Save to database
        recipe.save() 
        
        messages.success(request, f'Recipe "{recipe.title}" updated successfully!')
        return redirect("recipe_detail", slug=recipe.slug)

    # 6. Render the form pre-filled with existing recipe data
    return render(request, "center/edit_recipe.html", {"recipe": recipe})

@login_required
def delete_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    
    # Check if the user owns the recipe
    if recipe.author != request.user:
        messages.error(request, "You can't delete someone else's recipe.")
        return redirect('recipe_detail', slug=slug)

    if request.method == "POST":
        recipe.delete()
        messages.success(request, "Recipe deleted successfully!")
        return redirect("home")

    # Render a simple confirmation page for GET requests
    return render(request, "center/delete_confirm.html", {"recipe": recipe})




