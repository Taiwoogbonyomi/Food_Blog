# **TastyYum Foodblog**
TastyYum is a web application designed for food enthusiasts to explore, share, and manage delicious recipes from around the world. Users can browse a wide variety of recipes, view details, and engage with the community by commenting and rating recipes.

[View live website here](https://tasty-yum-ba485318f89d.herokuapp.com/)

![TastyYum responsive design](readme/assets/images/responsive-design.png)

# Table of Content

* [**Project**](<#project>)
    * [Objective](<#objective>)
    * [Site Users Goal](<#site-users-goal>)
    * [Site Owners Goal](<#site-owners-goal>)
  
* [**User Experience (UX)**](<#user-experience-ux>)
    * [Wireframes](<#wireframes>)
    * [User Stories](<#user-stories>)
    * [Site Structure](<#site-structure>)
    * [Design Choices](<#design-choices>)

* [**Existing Features**](<#existing-features>)
    * [Home page](<#home-page>)
    * [Sign Up](<#sign-up>)
    * [log In](<#sign-in>)
    * [log Out](<#sign-out>)
    * [Footer](<#footer>)  

* [**Features Left To Implement**](<#features-left-to-implement>)

* [**Technologies Used**](<#technologies-used>)
    * [Languages](<#languages>)
    * [Frameworks & Software](<#frameworks--software>)
    * [Libraries](<#libraries>)

* [**Testing**](<#testing>)
    * [Testing User Stories](<#testing-user-stories>)
    * [Code Validation](<#code-validation>)
    * [Additional Testing](<#additional-testing>)
    * [Known Bugs](<#known-bugs>)
* [Deployment](<#deployment>)
* [Credits](<#credits>)
* [Acknowledgements](<#acknowledgements>)

# **Project**

## Objective
As a food lover, I created this app to provide a community-driven platform where food enthusiasts can explore, share, and interact with recipes from various cuisines around the world. By facilitating a space for users to post recipes, rate dishes, leave comments, and offer feedback.

## Site Users Goal
The goal of the users is to discover a variety of recipes to try at home, ranging from everyday meals to special dishes from around the world.

## Site Owners Goal
The goal of the site owner of TastyYum is to ensure the platform's growth, user satisfaction, and overall success by encouraging active participation through recipe sharing, commenting, and voting.

### Database Schema
The database model used for this project is shown below and it was created using [Lucidchart](https://lucid.app/lucidchart/)
![Database schema](readme/assets/images/ERD.png)
[Back to top](<#table-of-content>)


# **User Experience (UX)**

## Wireframes
The wireframes for the site were created in the software [Balsamiq](https://balsamiq.com). The wireframes have been created for desktop, tablet and mobile devices. The text content wasn't finalized during the wireframe process. It's worth mentioning that there are visual differences compared to the wireframes, the reason being design choices that was made during the creation process.

<details><summary><b>Wireframes</b></summary>

![Wireframes](readme/assets/images/desktop-wireframe.png)
![Wireframes](readme/assets/images/tablet-wireframe.png)
![Wireframes](readme/assets/images/mobile-wireframe.png)
</details><br/>

## 👤 User Stories
Below the user stories for the project are listed to clarify why particular feature matters.

### Site User
|  | | |
|:-------:|:--------|:--------|
| As a Site User | I want to be able to browse recipes and read instructions without needing to log in, so that I can get a feel for the site before registering | &check; |
| As a Site User | I want to create an account, so that I can save my favorite recipes and interact with the community | &check; |
| As a Site User | I want to log in securely, so that I can ask questions, share tips, or leave feedback for other users | &check; |
| As a Site User | I want to log out, so that my account stays secure | &check; |
| As a Site User | I want to browse a list of recipes, so that I can explore different dishes | &check; |
| As a Site User | I want to see the full details of a recipe, so that I can follow the instructions to cook it | &check; |
| As a Site User | I want to submit a new recipe, so that I can share it with others.
| As a Site User | I want to filter recipes by category, so that I can easily find recipes that interest me | &check; |
| As a Site User | I want to leave a comment on a recipe, so that I can share my feedback or ask questions | &check; |
| As a Site User | I want to browse recipes comfortably, so that I can use the website on my phone | &check; |
| As a Site User | I want the interface to be fully responsive, so that I can comfortably browse and read recipes on a smaller screen | &check; |


### Site Admin

|  | | |
|:-------:|:--------|:--------|
| As a Site Admin | I can log out from the site so that I can feel safe that nobody can access my information | &check; |
| As a Site Admin | I want to enforce secure login methods, so that user data remains protected  | &check; |
| As a Site Admin | I want to view a list of all registered users, so that I can manage the community and remove unwanted users if necessary  | &check; |
| As a Site Admin | I want to delete offensive or spam comments, so that the site remains a positive and respectful space  | &check; |
| As a Site Admin | I want to create and organize recipe categories, so that users can easily find relevant recipes  | &check; |
| As a Site Admin | I want the ability to moderate user-generated content, so that I can ensure recipes and comments meet quality and community guidelines.
| As a Site Admin | I want to track site traffic and user activity, so that I can improve engagement and optimize content.
| As a Site Admin | I want analytics on recipe views, user engagement, and popular content, so that I can make data-driven decisions to improve the site


[Back to top](<#table-of-content>)


## Site Structure
The TastyYum website follows a structured layout for easy navigation and user experience. Below is the breakdown of the site's structure:

### **Home page**
- Landing page showcasing featured and latest recipes and Quick links to browse recipes by category.

<details><summary><b>Home page</b></summary>

![Screenshot of home page](./readme/assets/images/home-page.png)
</details><br>

### **Categories**
- Displays all available recipe categories

<details><summary><b>Categories</b></b></summary>

![Screenshot of categories](./readme/assets/images/categories-page.png)
</details><br>

### **Views recipes and add comments**
- Each recipe card includes an image, title, short description, and "View Recipe" button.
- Users can add, edit, or delete their comments.
- Users can view recipes but they cannot comment on recipes unless they are logged in.

<details><summary><b>View recipe and add comment page</b></b></summary>

![Screenshot of home page](./readme/assets/images/view-recipe%20and%20add-comment.png)
</details><br>

## **Authentication**

### **Sign Up**
- New users can create an account from the Signup page using the sign up form.

<details><summary><b>Sign Up</b></summary>

![Screenshot of Signup page](./readme/assets/images/sign-up.png)
</details><br/>

### **Log in**
- User authentication form with "Forgot Password?" link.
- Login with username/email and password.

<details><summary><b>Log in</b></summary>

![Screenshot of Login page](./readme/assets/images/login.png)
</details><br/>

### **Admin Area**
This page gives the administrator a view with information about i.e. total number of users, number of comments and number of posts. In this view the administrator also can add new recipes, categories the recipes, add and delete comments.

<details><summary><b>Admin Area</b></summary>

![Screenshot of admin page](./readme/assets/images/admin-nav.png)
</details><br/>

### Features Left to Implement
* Add functionalities to allow users to view and edit their profiles, including changing their passwords and updating personal information.
* Add a "Save Recipe" button so users can bookmark their favorite recipes.
* Add filters for sorting by category, difficulty, cooking time, or rating.
* Allow users to create their own recipes.
* Allow users to edit their submitted recipes.
* Implement functionality for users to delete their recipes.
* Enable users to reply to other users’ comments, creating a threaded discussion.
* Add funtion to allow user search for recipes

[Back to top](<#table-of-content>)

# Testing

## Testing User Stories
* As a Site User | I want to be able to browse recipes and read instructions without needing to log in, so that I can get a feel for the site before registering.
  * The site has been structured in a way that even without creating account, the user can browse through the recipes but they won't be able to comment, upvote or downvote any recipe.
* As a Site User | I want to create an account, so that I can save my favorite recipes and interact with the community 
  * In the navigation bar the user can click on sign up to create a new account.
* As a Site User | I want to log in securely, so that I can comment, edit or delete my comment, upvote or downvote
  * In the navigation bar the user can click the Login to log into their account. When this is done the user can leave comments, edit or delete comments on recipes, upvote and downvote.
* As a Site User | I want to log out, so that my account stays secure.
  * When the user is logged in it is possible to choose the 'Log Out'-option in the navigation menu.
* As a Site User | I want to see the full details of a recipe, so that I can follow the instructions to cook it.
  * On the home link, the user can click on the view recipe button to view the full details of the recipe.
* As a Site User | I want to filter recipes by category, so that I can easily find recipes that interest me.
  * On the navigation bar, the user can click on the categories link to view filter through the recipes by different categories.
* As a Site User | I want to browse recipes comfortably, so that I can use the website on my phone
  * The site has been created to be responsive on all devices irrespective of their size.
* As a Site Admin | I can log out from the site so that I can feel safe that nobody can access my information
   * When the admin is logged in it is possible to choose the 'Log Out'-option in the navigation menu.
* As a Site Admin | I want to view a list of all registered users, so that I can manage the community and remove unwanted users if necessary 
  * When the admin is logged in, the admin can view the list of all registered users, the admin can add and delete users.
* As a Site Admin | I want to delete offensive or spam comments, so that the site remains a positive and respectful space 
   * When the user is logged in as an administrator / superuser a new item show up in the navigation menu called 'Admin Area'. In this area the user can read, update and delete comments. Creation of comments can be made the same way as any logged in user. 
* As a Site Admin | I want to create and organize recipe categories, so that users can easily find relevant recipes.
  * When the Admin is logged in, there is a category area, where admin can create and organize recipes.

[Back to top](<#table-of-content>)

## Code Validation
The code on the 'TastyYum' site has been tested through W3C Markup Validation Service, W3C CSS Validation Service and JSHint. Errors were at first found on the site in the W3C Markup Validation Service but could quite easily be fixed (see bugs section). One error appeared as well in the W3C CSS Validation but that was connected to Font Awesome and not to the site code itself (see bugs section).

### Markup Validation
After fixing the inital errors that W3C Markup Validation Service reported, no errors were returned.
<details><summary><b>HTML Validation Result</b></summary>

![HTML Result ](readme/assets/images/html-checker.png)
</details><br/>

[Back to top](<#table-of-content>)
## Languages


### CSS Validaton
When validating my own code the W3C CSS Validator reports no errors.

<details><summary><b>CSS Validation Result</b></summary>

![CSS Result](readme/assets/images/css-validator.png)
</details><br/>

[Back to top](<#table-of-content>)

### JavaScript Validation
The JSHint validator results can be seen below:

No errors were returned when passing through JSHint (script.js)

<details><summary><b>JSHint Validation Result</b></summary>

![JSHint Validation](./readme/assets/images/JShint.png)
</details><br/>

[Back to top](<#table-of-content>)

### PEP Validation
PEP8 was used to validate the python codes.

* admin.py - No errors or warnings reported
* forms.py - No errors or warnings reported
* models.py - No errors or warnings reported
* apps.py - No errors or warnings reported
* urls.py - No errors or warnings reported
* views.py - No errors or warnings reported

## Additional Testing

### Manual Testing

In addition to tests stated above I have performed a series of manual tests. Below the list of tests that has been conducted can be found.

| Status | **Main Website - User Logged Out**
|:-------:|:--------|
| &check; | Typing in an incorrect URL on the page loads the 404 error page
| &check; | Pasting page that needs authentication loads a forbidden page
| &check; | Clicking the nav logo loads the home page
| &check; | Clicking the Home button on the nav bar loads the home page and lists all recipes
| &check; | Clicking the Categories button on the nav bar lists all recipe categories
| &check; | Clicking the Log In / Sign Up loads the login and sign up page
| &check; | 6 recipes are rendered for the user on the pages before pagination kicks in
| &check; | Clicking the View Recipe button on the a recipe card loads the recipe detail page
| &check; | In the recipe detail view the user cannot create a comment, upvote or downvote
| &check; | Clicking the Facebook link in the footer area opens Facebook in a new window
| &check; | Clicking the Twitter link in the footer area opens Twitter in a new window
| &check; | Clicking the Instagram link in the footer area opens Instagram in a new window
| &check; | Clicking the Youtube link in the footer area opens Youtube in a new window

| Status | **Main Website - User Logged In**
|:-------:|:--------|
| &check; | Typing in an incorrect URL on the page loads the 404 error page
| &check; | Pasting page that needs authentication loads a forbidden page
| &check; | Clicking the nav logo loads the home page
| &check; | Clicking the Home button on the nav bar loads the home page and lists all recipe
| &check; | Clicking the Categories button on the nav bar lists all the recipe categories 
| &check; | 6 recipes are rendered for the user on all pages before pagination kicks in
| &check; | Clicking the view recipe button on the recipe card loads the recipe detail page
| &check; | In the comment view the logged in user can comment on a recipe
| &check; | In the upvote and downvote views, a logged in user can upvote or downvote a recipe
| &check; | In the recipe view the logged in user can update/delete the comments written by themselves
| &check; | In the logged in user menu the Admin Area is not visible
| &check; | Clicking the Facebook link in the footer area opens Facebook in a new window
| &check; | Clicking the Twitter link in the footer area opens Twitter in a new window
| &check; | Clicking the Instagram link in the footer area opens Instagram in a new window
| &check; | Clicking the Youtube link in the footer area opens Youtube in a new window

| Status | **Main Website - Admin Logged In**
|:-------:|:--------|
| &check; | Clicking the Admin Area button in the logged in user menu loads the Admin Area Page
| &check; | The view button is only visible if a recipe is published
| &cross; | When clicking delete / add recipe the appropiate page loads and shows success page after submit
| &check; | Total Users shows correct number of total users
| &check; | Total Comments shows the correct number of total comments

Status | **Create A New User - User Logged Out**
|:-------:|:--------|
| &check; | Username field is required
| &check; | Username field does not accept empty field
| &check; | Email field does not accept just spaces
| &check; | Email field is optional
| &check; | Password field does not accept empty field


### Responsiveness Test
The responsive design tests were carried out manually with [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) and [Responsive Design Checker](https://www.responsivedesignchecker.com/).

| Desktop    | Display <1280px       | Display >1280px    |
|------------|-----------------------|--------------------|
| Render     | pass                  | pass               |
| Images     | pass                  | pass               |
| Links      | pass                  | pass               |

| Tablet     | Samsung Galaxy Tab 10 | Amazon Kindle Fire | iPad Mini | iPad Pro |
|------------|-----------------------|--------------------|-----------|----------|
| Render     | pass                  | pass               | pass      | pass     |
| Images     | pass                  | pass               | pass      | pass     |
| Links      | pass                  | pass               | pass      | pass     |

| Phone      | Galaxy S5/S6/S7       | iPhone 6/7/8       | iPhone 12pro         |
|------------|-----------------------|--------------------|----------------------|
| Render     | pass                  | pass               | pass      | pass     |
| Images     | pass                  | pass               | pass      | pass     |
| Links      | pass                  | pass               | pass      | pass     |

[Back to top](<#table-of-content>)


### Browser Compatibility
* Google Chrome Version (106.0.5249.119)
* Mozilla Firefox (version 105.0.3)
* Min (version 1.26.0)
* Apple Safari (version 16.0)
* Microsoft Edge (version 106.0.1370.47)

[Back to top](<#table-of-content>)


### Lighthouse
Google Lighthouse in Chrome Developer Tools was used to test the application within the areas of *Performance*, *Accessibility*, *Best Practices* and *SEO*. I tested the *index page*, *review details page*, *the admin area* and *the about page*. The testing showed the following:

* Index Page - Performance: 75, Accessibility: 100, Best Practises: 100, SEO: 92


<details><summary><b>Lighthouse Result</b></summary>

![Lighthouse Index Result](readme/assets/images/lighthouse-check.png)
</details><br/>

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - Provides the functionality for the site.
* [HTML5](https://en.wikipedia.org/wiki/HTML) - Provides the content and structure for the website.
* [CSS3](https://en.wikipedia.org/wiki/CSS) - Provides the styling for the website.
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - Provides interactive elements of the website

## Frameworks & Software
* [Bootstrap](https://getbootstrap.com/) - A CSS framework that helps building solid, responsive, mobile-first sites
* [Django](https://www.djangoproject.com/) - A model-view-template framework used to create the Review | Alliance site
* [Balsamiq](https://balsamiq.com/) - Used to create the wireframe.
* [Microsoft Excel](https://www.microsoft.com/sv-se/microsoft-365/excel) - Used to create testing scenarios.
* [Github](https://github.com/) - Used to host and edit the website.
* [GitBash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) - Terminal in [Gitpod](https://www.gitpod.io) used to push changes to the GitHub repository.
* [Heroku](https://en.wikipedia.org/wiki/Heroku) - A cloud platform that the application is deployed to.
* [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) - Used to test performance of site.
* [Responsive Design Checker](https://ui.dev/amiresponsive) - Used for responsiveness check.
* [Favicon](https://favicon.io/) - Used to create the favicon.
* [Gitpod](https://gitpod.io/)- Used to create and edit this website.
* [Cloudinary](https://cloudinary.com/) - A service that hosts all static files in the project.
* [HTML Validation](https://validator.w3.org/) - Used to validate HTML code
* [CSS Validation](https://jigsaw.w3.org/css-validator/) - Used to validate CSS code
* [PEP8 Validation](http://pep8online.com/) - 
* [JSHint Validation](https://jshint.com/) - Used to validate JavaScript code
* [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) - Used to debug and test responsiveness.

[Back to top](<#table-of-content>)


#### 📦 Local Deployment  
1. Clone the repository from GitHub by clicking the "Code" button and copying the URL.
2. Open your preferred IDE and open a terminal session in the directory you want to clone the repository to.
3. Type `git clone` followed by the URL you copied in step 1 and press enter.
4. Install the required dependencies by typing `pip install -r requirements.txt` in the terminal.
5. Note: The project is setup to use environment variables. You will need to set these up in your local environment. See [Environment Variables](#environment-variables) for more information.
6. Connect your database of choice and run the migrations by typing `python manage.py migrate` in the terminal.
7. Create a superuser by typing `python manage.py createsuperuser` in the terminal and following the prompts.
8. Optional: Fixtures for Flight, Airport and Aircraft models are included in the project in the `fixtures` directory. To add pre-populated data to the database, run `python manage.py loaddata fixtures/[fixture_name].json`.
9. Run the app by typing `python manage.py runserver` in the terminal and opening the URL in your browser.

#### 💜 Heroku Deployment
1. Login to the Heroku dashboard and create a new app.
2. Connect your GitHub repository to your Heroku app.
3. In the Settings tab, ensure that the Python Buildpack is added.
4. Set environment variables in the Config Vars section of the Settings tab.
5. In the Deploy tab, enable automatic deploys from your GitHub repository.
6. Click the "Deploy Branch" button to deploy the app.
7. Once the app has been deployed, click the "Open App" button to view the app.
8. If using S3, you will need to set up an S3 bucket and add the environment variables to your Heroku app (see tutorial [here](https://testdriven.io/blog/storing-django-static-and-media-files-on-amazon-s3/) for reference.)

[Back to top](<#table-of-content>)

#### 📐 Environment Variables
- For local deployment, you will need to create a `.env` file in the root directory of the project and set the environment variables in this file.
- For Heroku deployment, you will need to set the environment variables through the Heroku CLI or through the Heroku dashboard under 'Config Vars'.
- You need to define the following variables:
  - If using a Postgres database:
    - `DATABASE_URL` - the URL for your Postgres database.
    - `NAME` - the name of your database.
    - `USER` - the username for your database.
    - `PASSWORD` - the password for your database.
    - `HOST` - the host for your database.
    - `PORT` - the port for your database.
  - Django settings:
    - `SECRET_KEY` - the secret key for your Django project.
    - `DEBUG` - set to `True` for development, `False` for production.
  </details>
  
<br>
<br>
<br>

---

# 👋 Credits

<details>
[Favicon.io](https://favicon.io/) - used to create favicon.
[pexels.com](https://www.pexels.com/)- used to generate all the images

</details>

[Back to top](<#table-of-content>)