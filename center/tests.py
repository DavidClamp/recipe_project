from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Recipe


class TestAddRecipeView(TestCase):
    """Verify functionality and security of the recipe creation view."""

    def setUp(self):
        self.user = User.objects.create_user(username='chef_david', password='password123')
        self.client.login(username='chef_david', password='password123')
        self.url = reverse('add_recipe')

    def test_get_add_recipe_page(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'center/add_recipe.html')

    def test_successful_recipe_creation(self):
        recipe_data = {
            'title': 'Test Pasta',
            'ingredients': 'Water, Flour',
            'instructions': 'Boil and eat.',
            'status': 1
        }
        response = self.client.post(self.url, recipe_data)
        self.assertEqual(response.status_code, 302) 
        self.assertEqual(Recipe.objects.count(), 1)

    def test_unauthenticated_user_redirect(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)


class TestEditDeleteViews(TestCase):
    """Verify permission-based CRUD operations for recipe authors."""

    def setUp(self):
        self.author = User.objects.create_user(username='chef_david', password='password123')
        self.malicious_user = User.objects.create_user(username='bad_actor', password='password123')
        self.recipe = Recipe.objects.create(
            title='Old Stew', 
            slug='old-stew', 
            author=self.author, 
            ingredients='Beef', 
            instructions='Cook it.'
        )

    def test_author_can_access_edit_page(self):
        self.client.login(username='chef_david', password='password123')
        response = self.client.get(reverse('edit_recipe', args=[self.recipe.slug]))
        self.assertEqual(response.status_code, 200)

    def test_malicious_user_access_denied(self):
        """Confirm a non-author is blocked from accessing the edit route."""
        self.client.login(username='bad_actor', password='password123')
        response = self.client.get(reverse('edit_recipe', args=[self.recipe.slug]))
        self.assertNotEqual(response.status_code, 200)

    def test_successful_recipe_update(self):
        self.client.login(username='chef_david', password='password123')
        updated_data = {
            'title': 'New Stew',
            'description': 'A revised family favorite.',
            'ingredients': 'Beef, Carrots, Potatoes',
            'instructions': 'Simmer for 2 hours.',
            'status': 1
        }
        response = self.client.post(reverse('edit_recipe', args=[self.recipe.slug]), updated_data)
        self.assertEqual(response.status_code, 302)
        self.recipe.refresh_from_db()
        self.assertEqual(self.recipe.title, 'New Stew')

    def test_recipe_deletion(self):
        self.client.login(username='chef_david', password='password123')
        self.client.post(reverse('delete_recipe', args=[self.recipe.slug]))
        self.assertEqual(Recipe.objects.count(), 0)
