from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe

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
# comment_count = post.comments.filter(approved=True).count()
  
# if request.method == "POST":
#     comment_form = CommentForm(data=request.POST)
#     if comment_form.is_valid():
#         comment = comment_form.save(commit=False)
#         comment.author = request.user
#         comment.post = post
#         comment.save()

# comment_form = CommentForm()

# return render(
