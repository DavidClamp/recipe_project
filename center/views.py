from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import RecipeForm


# Create your views here.
class RecipeList(generic.ListView):
    queryset = Recipe.objects.all()
    template_name = "center/index.html"
    # context_object_name = "recipes"
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
