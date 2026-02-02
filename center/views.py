from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe
from django.utils.text import slugify
from django.shortcuts import redirect



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




