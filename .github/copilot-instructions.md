# Copilot Instructions for Recipe Twist Project

## Project Overview
This project is a Django-based web application for managing and sharing recipes. It includes features for user authentication, recipe creation, and management, utilizing Django's built-in functionalities and third-party packages.

## Architecture
- **Core Components**: The main components include the `center` app, which handles recipe-related functionalities, and the `my_project` directory, which contains the project settings and configurations.
- **Data Flow**: Recipes are created and managed through forms in the `center` app, with data stored in a SQLite database. The `Recipe` model defines the structure of recipe data.
- **Service Boundaries**: The `center` app is responsible for all recipe-related views, models, and templates, while the `my_project` directory manages overall project settings and URL routing.

## Developer Workflows
- **Running the Application**: Use the command `python manage.py runserver` to start the development server.
- **Database Migrations**: Run `python manage.py makemigrations` and `python manage.py migrate` to apply database changes.
- **Testing**: Use `python manage.py test` to run tests defined in the `center/tests.py` file.

## Project-Specific Conventions
- **Model Structure**: Recipes are defined in `models.py` with fields for title, slug, author, description, ingredients, and instructions. The `status` field indicates whether a recipe is a draft or published.
- **Template Usage**: Templates are organized under `templates/center/`, with `index.html` and `recipe_detail.html` serving as the main views for listing and displaying recipes, respectively.
- **Static Files**: CSS and JavaScript files are stored in the `static/` directory, with Bootstrap used for styling.

## Integration Points
- **External Dependencies**: The project uses `django-allauth` for user authentication and `django-summernote` for rich text editing in recipe descriptions.
- **Cross-Component Communication**: The `urls.py` files in both the `my_project` and `center` directories define how different views are accessed and linked together.

## Key Files
- **`manage.py`**: The command-line utility for administrative tasks.
- **`settings.py`**: Contains project settings, including installed apps and middleware.
- **`urls.py`**: Defines URL routing for the application.
- **`models.py`**: Contains the `Recipe` model definition.
- **`views.py`**: Implements the logic for displaying recipes.

## Conclusion
This document serves as a guide for AI coding agents to understand the structure and workflows of the Recipe Twist project, enabling them to assist effectively in development tasks.