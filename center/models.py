from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Finished"))

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="recipe_posts")
    description = models.TextField(blank=True)
    ingredients = models.TextField()
    instructions = models.TextField()

    # state if recipe is still in draft of finished(published)

    status = models.IntegerField(choices=STATUS, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# order recipes with updates first then second created

    class Meta:
        ordering = ["-updated_at","-created_at"]

    # show title as a readable string 

    def __str__(self):
        return f"The title of this recipe is {self.title}"
