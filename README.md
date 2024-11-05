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

#### 👤 User Stories
1. As a user, I want to easily browse or search for dishes based on cuisine, dietary preferences, or ingredients, so that I can quickly find recipes that suit my tastes or dietary needs.
2. As a user, I want to leave comments on recipes, so that I can ask questions, share tips, or leave feedback for other users.
3. As a user, I want to be able to browse recipes and read instructions without needing to log in, so that I can get a feel for the site before registering.
4. As a user, I want to find recipes that can be made quickly, so that I can prepare meals efficiently within my time constraints.
5. As a user, I want to quickly scan recipes on the list page and see brief descriptions or ratings, so that I can decide which recipe interests me most before clicking through.
6. As a user accessing the site from my phone, I want the interface to be fully responsive, so that I can comfortably browse and read recipes on a smaller screen.
7. As an owner looking to grow the platform, I want analytics on recipe views, user engagement, and popular content, so that I can make data-driven decisions to improve the site.
8. As an admin, I want the ability to moderate user-generated content, so that I can ensure recipes and comments meet quality and community guidelines.
[Back to top](<#table-of-content>)


## Site Structure
The structure of TastyYum app organizes content and functionality for easy navigation and user experience.

### **Home page**
Users can navigate through the page here

<details><summary><b>Home page</b></summary>

![Screenshot of home page](/readme/assets/images/home-page.png)
</details><br>

### **Views recipes and add comments**
 Users can view recipes but they cannot comment on recipes unless they are logged in.
<details><summary><b>View recipe and add comment page</b></b></summary>

![Screenshot of home page](/readme/assets/images/view-recipe%20and%20add-comment.png)
</details><br>

### **Sign Up**
New users can create an account from the Signup page.

<details><summary><b>Sign Up</b></summary>

![Screenshot of Signup page](/readme/assets/images/sign-up.png)
</details><br/>

### **Log in**
Users can login from the Login page.

<details><summary><b>Log in</b></summary>

![Screenshot of Login page](/readme/assets/images/log-in.png)
</details><br/>

### **Admin Area**
This page gives the administrator a view with information about i.e. total number of users, number of comments and number of posts. In this view the administrator also can add new recipes, categories the recipes, add and delete comments.

<details><summary><b>Admin Area</b></summary>

![Screenshot of admin page](/readme/assets/images/admin-nav.png)
</details><br/>

### Features Left to Implement
* Add functionalities to llow users to view and edit their profiles, including changing their passwords and updating personal information.
* Allow users to edit their submitted recipes.
* Implement functionality for users to delete their recipes.
* Add categories or tags to recipes for better organization and filtering
* Implement the ability for users to edit their comments.
* Allow users to delete their comments.
* Enable users to reply to other users’ comments, creating a threaded discussion.
* Prevent users from voting multiple times on the same recipe (i.e., they can only upvote or downvote once).
* Add funtion to allow user search for recipes

## Languages

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



