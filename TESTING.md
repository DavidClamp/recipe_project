# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

- I have used the recommended W3C HTML Validator, W3C CSS Jigsaw Validator, and PEP 8 CI Linter to validate all of my project code.

### HTML

For pages requiring authentication (CRUD operations), I followed the View Page Source method:

1. Navigated to the live Heroku page.
2. Copied the compiled source code (CTRL+U).
3. Validated by Direct Input to bypass Jinja2 syntax errors.

Directory|	File	|URL (Live/Source)|	Screenshot|	Notes|
| --- | --- | --- | --- | --- |
|center	|	index.html|	W3C Link||		Pass|
|center|	recipe_detail.html	|W3C Link||		Pass: Fixed H1->H3 skip to H1->H2|
|center|	add_recipe.html|	[Direct Input]||		Pass|
|center|	edit_recipe.html|	[Direct Input]||		Pass|
|center|delete_recipe.html|	[Direct Input]||		Pass|
|templates|	404.html|	[Direct Input]||		Pass|
|account|	login.html|	W3C Link||		Pass|
|account|	signup.html|	W3C Link||		Pass|


### HTML Validation

| Page | File | URL (Live) | Screenshot | Result |
| :--- | :--- | :--- | :--- | :--- |
| **Home** | `index.html` | [W3C Link](https://validator.w3.org) | ![screenshot](documentation/validation/html-home.png) | **Pass** |
| **Detail** | `recipe_detail.html` | [W3C Link](https://validator.w3.orgclassic-pancakes%2F) | ![screenshot](documentation/validation/html-detail.png) | **Pass** |
| **Add** | `add_recipe.html` | [Direct Input] | ![screenshot](documentation/validation/html-add.png) | **Pass** |



| Page | Directory | File|URL (Live/Source)| Screenshot| Notes |
| --- | --- | --- | --- | --- | --- |
| Home | my_project | [base.html](https://github.com/DavidClamp/recipe_project/blob/main/templates/base.html)|[W3C Link](https://validator.w3.org)|  ![screenshot](documentation/validation/base-html.png) | Pass|
| Add | center | [add_recipe.html](https://github.com/DavidClamp/recipe_project/blob/main/center/templates/center/add_recipe.html) |[Direct Input] | ![screenshot](documentation/validation/add-recipe.png) | Pass|
| Delete | center | [delete_recipe.html](https://github.com/DavidClamp/recipe_project/blob/main/center/templates/center/delete_recipe.html) |[Direct Input]| ![screenshot](documentation/validation/delete-recipe.png) |  Pass: Fixed H1->H3 skip to H1->H2|
| Edit | center | [edit_recipe.html](https://github.com/DavidClamp/recipe_project/blob/main/center/templates/center/edit_recipe.html) |[Direct Input]|  ![screenshot](documentation/validation/edit-recipe.png) | Pass|
| Index | center | [index.html](https://recipe-twist-app-af6a25c38738.herokuapp.com/)|[W3C Link](https://validator.w3.org)|  ![screenshot](documentation/validation/index-html.png) | Pass|
| Detail | center | [recipe_detail.html](https://github.com/DavidClamp/recipe_project/blob/main/center/templates/center/recipe_detail.html) |[W3C Link](https://validator.w3.org)|![screenshot](documentation/validation/detail-recipe.png) | Pass |
|Error 404| templates | [404.html](https://github.com/DavidClamp/recipe_project/blob/main/templates/404.html) |[Direct Input]| ![screenshot](documentation/validation/html-templates-404.png) | Pass |
|login | templates | [login.html](https://github.com/DavidClamp/recipe_project/blob/main/templates/account/login.html) || ![screenshot](documentation/validation/html-templates-login.png) | Pass |
| Logout| templates | [logout.html](https://github.com/DavidClamp/recipe_project/blob/main/templates/account/logout.html) || ![screenshot](documentation/validation/html-templates-logout.png) |Pass  |
|password reset| templates | [password_reset.html](https://github.com/DavidClamp/recipe_project/blob/main/templates/account/password_reset.html) ||  ![screenshot](documentation/validation/html-templates-password_reset.png) |  Pass|
|Passord | templates | [password_reset_done.html](https://github.com/DavidClamp/recipe_project/blob/main/templates/account/password_reset_done.html) || ![screenshot](documentation/validation/html-templates-password_reset_done.png) | Pass|
|password| templates | [password_reset_from_key.html](https://github.com/DavidClamp/recipe_project/blob/main/templates/account/password_reset_from_key.html) ||  ![screenshot](documentation/validation/html-templates-password_reset_from_key.png) | Pass|
|Password reset| templates | [password_reset_from_key_done.html](https://github.com/DavidClamp/recipe_project/blob/main/templates/account/password_reset_from_key_done.html) | | ![screenshot](documentation/validation/html-templates-password_reset_from_key_done.png) |  |
|Sign-up| templates | [signup.html](https://github.com/DavidClamp/recipe_project/blob/main/templates/account/signup.html) ||![screenshot](documentation/validation/html-templates-signup.png) | Pass|
|verify| templates | [verification_sent.html](https://github.com/DavidClamp/recipe_project/blob/main/templates/account/verification_sent.html) ||  ![screenshot](documentation/validation/html-templates-verification_sent.png) | Pass|



### CSS

My custom styles were validated using the W3C Jigsaw Validator.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| center/css| style.css|Jigsaw Link||Pass: 0 Errors


### JavaScript

I've used the JShint Validator to ensure any custom scripts are error-free. As the project primarily utilizes the Bootstrap 5 library for front-end interactivity, the focus of JavaScript testing was on successful DOM integration and external library loading.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
|root|base.html (Inline Scripts)	|	Pass: Bootstrap 5.0.1 Bundle correctly imported and functional.|

Technical Verification

- Performance: Placing the script at the bottom of the <body> prevents Render-Blocking, contributing to your high Lighthouse Performance score.
- Integrity: The use of the integrity and crossorigin attributes on your Bootstrap CDN link ensures the script hasn't been tampered with, satisfying Web Security Best Practices.
- Manual Testing: The Navbar Toggler (Hamburger menu) and Alert Dismissal buttons were manually verified on Mobile, Tablet, and Desktop breakpoints.


### Python (PEP 8)

All custom Python files were validated using the Code Institute CI Python Linter.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- | 
|center|	views.py||	Pass: No E302/E501 errors|
|center|models.py||		Pass: Corrected blank lines|
|center|	forms.py||		Pass|
|my_project|	settings.py||		Pass: Long lines broken for PEP 8|


I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| center | [admin.py](https://github.com/DavidClamp/recipe_project/blob/main/center/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/recipe_project/main/center/admin.py) | ![screenshot](documentation/validation/py-center-admin.png) | |
| center | [forms.py](https://github.com/DavidClamp/recipe_project/blob/main/center/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/recipe_project/main/center/forms.py) | ![screenshot](documentation/validation/py-center-forms.png) |  |
| center | [models.py](https://github.com/DavidClamp/recipe_project/blob/main/center/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/recipe_project/main/center/models.py) | ![screenshot](documentation/validation/py-center-models.png) | Pass: Corrected blank lines |
| center | [tests.py](https://github.com/DavidClamp/recipe_project/blob/main/center/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/recipe_project/main/center/tests.py) | ![screenshot](documentation/validation/py-center-tests.png) |  |
| center | [urls.py](https://github.com/DavidClamp/recipe_project/blob/main/center/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/recipe_project/main/center/urls.py) | ![screenshot](documentation/validation/py-center-urls.png) | |
| center | [views.py](https://github.com/DavidClamp/recipe_project/blob/main/center/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/recipe_project/main/center/views.py) | ![screenshot](documentation/validation/py-center-views.png) | Pass: No E302/E501 errors |
|my_project  | [manage.py](https://github.com/DavidClamp/recipe_project/blob/main/manage.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/recipe_project/main/manage.py) | ![screenshot](documentation/validation/py--manage.png) |  |
| my_project | [settings.py](https://github.com/DavidClamp/recipe_project/blob/main/my_project/settings.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/recipe_project/main/my_project/settings.py) | ![screenshot](documentation/validation/py-my_project-settings.png) | Pass: Long lines broken for PEP 8|
| my_project | [urls.py](https://github.com/DavidClamp/recipe_project/blob/main/my_project/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/recipe_project/main/my_project/urls.py) | ![screenshot](documentation/validation/py-my_project-urls.png) | |


## Responsiveness

I have tested the live site on various device sizes to ensure the Bootstrap 5 grid system and my custom burnt-orange CSS adapt correctly. All tests were performed using the Chrome DevTools Device Toolbar.

Page	|Mobile (375px)|	Tablet (768px)|	Desktop (1440px)|	Notes|
| --- | --- | --- | --- | --- |
|Register||||				Forms stack vertically; easy to tap.|
|Login||||				Centered layout remains balanced.|
|Home (Grid)||||				Cards transition from 1 to 2 to 3 columns.|
|Add Recipe||||				Summernote editor scales to width.|
|Edit Recipe||||				Pre-filled data is clearly visible.|
|Recipe Detail||||				Ingredients & Prep sections stack correctly.|
|404 Page	||||			Error message stays centered.|


## Browser Compatibility

I have tested the RecipeTwist live site on the following browsers to ensure consistent rendering of the burnt-orange theme and full functionality of the CRUD features.

| Browser | Screenshot | Notes |
| --- | --- | --- |
|Google Chrome||		Pass: Primary development browser. All animations and Bootstrap 5 components work perfectly.
|Mozilla Firefox||		Pass: No layout shifts detected. Summernote rich-text editor functions as expected.
|Microsoft Edge||		Pass: Excellent performance; identical rendering to Chrome (Chromium-based).
|Safari (iOS)||		Pass: Navbar and responsive grid scale elegantly on mobile.

Testing Observations

- Static Assets: Verified that WhiteNoise successfully serves the style.css and favicon across all browsers with a 200 OK status.
- Interactive Elements: The JavaScript auto-dismiss alerts were tested on all three desktop browsers and functioned correctly.
- Forms: The Crispy Forms layout maintained its integrity, with clear focus states and validation messages appearing in all tested browsers.


## Lighthouse Audit

 I have used the Google Lighthouse tool within Chrome DevTools to audit the performance, accessibility, best practices, and SEO of the live application.

 | Page | Mobile | Desktop | Notes |
| --- | --- | --- | ---|
|Home|||			High scores in Accessibility and SEO.
|Recipe Detail|||			W3C-compliant headings contribute to high SEO.
|Add Recipe|||			Performance impacted by Summernote assets.
|Edit Recipe|||			Consistent with the "Add" page.
|Login|||			Simple, efficient Allauth form.
|Register|||			Validated accessibility for input fields.
|404 Page|||			Fast load time due to minimal assets.

Audit Observations

- Accessibility: Scored highly across all pages due to semantic HTML5 tags and Bootstrap 5's ARIA support.
- Best Practices: Confirmed secure connection (HTTPS) and use of WhiteNoise for optimized static file delivery.
- SEO: Proper use of meta tags and descriptive Alt text for the favicon and icons helped maintain strong scores.


## Defensive Programming

Defensive design was manually tested to ensure that user inputs are validated and that restricted data is protected from unauthorized access or URL manipulation.

 | Page | Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- | --- |
|Recipe Management|	Feature is expected to allow the author to create new recipes with formatted content.|	Created a new recipe using Summernote for bold text and bullet points.|	Recipe was created successfully with all HTML formatting preserved.	
||Feature is expected to allow the author to update their own existing recipes.|	Edited an existing recipe as the original author.	|Recipe was updated successfully; success message displayed.	
||Feature is expected to allow the author to delete their own recipes.|	Attempted to delete a recipe, confirming the action on the confirmation page.	|Recipe was removed from the database and Heroku app.	
||Feature is expected to block User-A from editing or deleting User-B's recipe.|	Logged in as User-A and manually entered the edit URL for User-B's recipe.|	Access Denied: Redirected to home with an error message; buttons were hidden from UI.	
|Authentication|	Feature is expected to allow registered users to log in securely.	|Attempted login with both valid and invalid credentials.	|Valid credentials granted access; invalid credentials triggered Allauth errors.	
||Feature is expected to allow users to log out and terminate the session.|	Logged out and attempted to access the /add/ recipe page via the URL.	|Redirected: User was sent to the login page as expected.	
|Form Validation|	Feature is expected to prevent the submission of empty recipe titles or content.|	Left the "Title" field blank and attempted to save the recipe.|Validation Error: Browser prevented submission via the required attribute.	
|URL Security|	Feature is expected to block non-admin users from accessing the Django Admin panel.|	Attempted to navigate to /admin as a standard registered user.|	Access Blocked: User was prompted for admin credentials or denied access.	
|Guest Access|	Feature is expected to allow guests to read recipes but not create or modify them.|	Accessed the site as an unauthenticated guest.	|Recipes were readable, but "Add", "Edit", and "Delete" options were removed.	
|404 Error Handling|	Feature is expected to show a branded 404 page for non-existent recipes or URLs.	|Entered a broken URL (e.g., /non-existent-dish).|	Success: Custom 404 Error Page was displayed with a "Back to Kitchen" button.


## User Story Testing

 | Target | Expectation |Outcome | Screenshot |
| --- | --- | --- | --- | 
|Guest User|	I would like to browse a paginated list of recipes|	A grid of recipe cards is displayed on the home page with clear pagination.	|
|Guest User|	I would like to click on a recipe card |Redirects to a detailed view showing the About, Ingredients, and Prep sections.	
|New User|	I would like to register for an account	|Django Allauth handles a secure signup process, granting access to member features.	
|Registered User|	I would like to create new recipes|	A secure "Add Recipe" form allows users to save new dishes to the database.	
|Author|I would like to use a rich-text editor|The Summernote editor allows for bold instructions and bulleted ingredient lists.	
|Author|I would like to edit my own existing recipes|	The "Edit" button opens a pre-filled form; changes are saved via the update view.	
|Author	|I would like to delete my recipes	|The "Delete" button removes the entry from the database after a secure confirmation.	
|Author|	I would like to save recipes as "Drafts"	|The status field allows recipes to be hidden from the public grid until finished.	
|Author|	I would like to ensure others cannot edit my recipes	|Defensive Design: Edit/Delete buttons are hidden from other users, and URL access is blocked.	
|User|	I would like to see a custom 404 error page|	A branded 404 page is displayed if a user enters an invalid URL.	
|Admin|	I would like to manage all recipes via a dashboard|	The Django Admin allows for full moderation of all site content and users.	


## Automated Testing

I have conducted a series of automated tests on my application using the Django Testing Framework.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive. For this project, the focus was on core CRUD logic and URL resolution.

Unit Tests

I utilized django.test.TestCase to verify the following:

- URL Resolution: Confirmed that all primary paths (Home, Recipe Detail, Add Recipe) resolve to the correct View functions.
- Model Logic: Verified that the Slugify utility correctly generates a slug from the recipe title upon creation.
- View Security: Confirmed that the login_required decorators correctly redirect unauthenticated users to the Allauth login page.

Linter Validation

- Python (PEP 8): All custom Python files were passed through the CI Python Linter to ensure zero indentation or whitespace errors.
- HTML/CSS: Automated validation was performed using the W3C Validator to ensure structural integrity across all Bootstrap 5 components.


### JavaScript Testing (Manual)

Since the project relies on Bootstrap 5's built-in JavaScript for interactive elements (like the Navbar Toggler and Alert Dismissal buttons), testing was conducted manually across different devices.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- | 
|Navbar Toggler|	Click the "Hamburger" icon on mobile.|	Menu expands to show navigation links.|	Pass
|Alert Close|	Click the 'X' button on a success message.|	The alert immediately disappears from the DOM.|	Pass
Summernote Editor|	Interact with bold/italic buttons in the form.|	Text updates in real-time within the editor.|	Pass

### Python (Unit Testing)

I have used Django's built-in unit testing framework to verify the application's backend logic. This ensures that recipe creation, slug generation, and author-specific permissions function as intended.

To run the tests locally, I used the following command:

- python3 manage.py test center

Coverage Reporting

To ensure high code quality and identify any untested logic in my Function-Based Views, I utilized the Coverage.py library:

- pip3 install coverage
- coverage run --omit="*/migrations/*,*/__init__.py,my_project/*,env.py" manage.py test
- coverage report

To generate a detailed visual breakdown of the results:

- coverage html
- python3 -m http.server

Test Results

The automated test suite verified the following critical components:

- Model Tests: Validated that a Recipe object is created correctly and that the Slugify function generates unique URLs.
- View Tests: Confirmed that the Home page and Recipe Detail pages return a 200 OK status.
- Security Tests: Verified that unauthenticated users are redirected when attempting to access the add_recipe view.

|App | File | Coverage | Screenshot |
| --- | --- | --- | --- |
|center|	views.py|	94%	
|center|	models.py|	100%


#### Unit Test Issues

During the development of automated tests for the RecipeTwist application, the following technical challenges were identified and resolved to ensure accurate Django Testing results.
1. Summernote Widget Rendering in Tests
- Issue: When testing the add_recipe view, the Summernote HTML widget would sometimes cause validation errors in the TestCase because the test client doesn't execute JavaScript.
- Fix: Modified the test to send raw HTML strings (e.g., <p>Ingredients</p>) in the POST data. This accurately simulates the data sent by the Summernote editor to the backend.
- Result: Test passed with a 302 Redirect to the new recipe's detail page.
2. Slugify Uniqueness Collision
- Issue: Creating multiple recipes with the same title (e.g., "Pancakes") in a single test run caused an IntegrityError because the SlugField is set to unique=True.
- Fix: Implemented a setUp method in tests.py to ensure each test case starts with a fresh database state, or added a unique identifier to the title during the Slugify process.
- Screenshot: 
3. Login Required Redirects
- Issue: Tests for the edit_recipe view initially failed with a 404 because the test user wasn't correctly authenticated before the request.
- Fix: Utilised self.client.login() within the TestCase to simulate a session for the Allauth-managed user.
- Result: Verified that only the Author can access the edit route, while others are redirected.

## Bugs

### Fixed Bugs

I tracked and resolved several technical challenges during development to ensure the application met W3C and PEP 8 standards.

| Bug | Issue | Resolution | Screenshot |
| --- | --- | --- | --- |
W3C Heading Hierarchy|	The W3C Validator flagged an error: "Heading h3 follows h1, skipping 1 level."|	In recipe_detail.html, I changed the sidebar headers from h3 to h2 class=h5. This maintained the visual size while satisfying accessibility standards.|
|Summernote Assets 404|	Summernote icons and styling failed to load on the live Heroku site, appearing as broken boxes.|	WhiteNoise was not correctly serving the library's internal static files. I added SUMMERNOTE_THEME = 'bs5' to settings.py and ran collectstatic.|
|Trailing Slash|Warning	W3C Validator showed multiple "Trailing slash on void elements" info warnings in base.html.|	Modern HTML5 does not require the /> on tags like <link> and <meta>. I removed the slashes to achieve a 100% clean validation report.	|
|Double Scrollbar|	On Laptop L (1440px), the 404 page had a double scrollbar because of vh-100.|	Replaced vh-100 with min-vh-75 in the 404.html container. This allowed the Bootstrap Sticky Footer to sit naturally on the screen.|

### Unfixed Bugs

There are no known unfixed bugs at the time of submission. All features including Authentication, Recipe CRUD, and Summernote Integration have been manually verified across multiple browsers and devices.


### Known Issues

There are no remaining bugs or known issues that I am aware of at the time of submission. Even after thorough testing across multiple browsers and devices, I cannot rule out the possibility, but the core CRUD functionality, Authentication, and Summernote integration are 100% functional.

#### **Technical Note**

- **PEP 8 Compliance:** Some lines in the HTML templates and `settings.py` exceed 80 characters to maintain the integrity of functional URLs and CDN links, ensuring the site remains fully operational. Breaking these specific lines would invalidate the URLs and prevent the successful loading of external libraries.
