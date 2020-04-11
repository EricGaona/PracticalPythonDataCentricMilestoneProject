# Cookbook

This is a website of vegetarian and vegan recipes. The features of the website are: 

sharing of new recipes, edit and delete existing recipes, promotion of a brand of cook tools and a contact page. 

The primary goal of this website is, that the users will become engaged by and learn from the variety of available recipes on-site to be inspired to cook more vegan and vegetarian food using promoted cooking tools which in turn can lead to increased sales of said cooking tools brand. 


## UX

The ideal cents for this website are:

* English speaking.
* vegetarians or vegans.
* chefs and home cooks.
* Those interested in healthy foods or sustainable living. 


Visitors to this website are searching for:

* Find or share vegetarian or vegan recipes.
* How to use new cooking tools.
* Inspiration for daily meals. 


This project is the best way to:

* Expand one’s knowledge of vegetarian and vegan (V&V) cuisine.
* Share new and exciting recipes with the V&V community.
* Encourage more people to try food that is more sustainable.
* Become familiar with which tools are best suited to use when cook which dishes. 


Client stories

1. As a new user of this website, I want to find what I need quickly and easily.
2. As a new visitor to this website, I was to browse a list of new and exciting recipes to inspire me to try new foods that cater to my vegan diet.
3. As a new visitor to this website, I want to share my own V&V recipes with likeminded people.
4. As a new visitor to this website I want to learn more about the types of cooking tools, I should use to get the best results from each of the recipes I will cook.  


## Features

Each page features a responsive navigation bar and a conventional placing of the logo on the top left-hand side of the page, each page also has a footer with copyright information.  Every page has a header image with text across. 

Vegan and Vegetarian tabs

These pages show the recipes vegan and vegetarian respectively.  It shows the name of the recipe, and images, the ingredients, a small description, the cooking tools, a button to delete the recipes and a button to edit the recipe. 

Share Recipe

This page contains a form where the user who wants to share a recipe must specify if it’s vegetarian or vegan, the name of the recipe, ingredients, the link to an image and a short description. 

Cooking Tools

On this page, we present a group of cooking tools that are used in the preparation of the recipes. Alongside the name of the tool, an image and its description.

Contact

The Contact Page features a contact form, which requests the name of the person, email, phone number and message.  The button of the form contains a send button. 


### Features to implement in future

* Create a database where users can create their own login account and then, only people who own an account can carry out the actions of Delete, Share and Edit.  The public can still read all recipes but only account holder can make changes and upload new recipes. 
* Configure the database so users can upload photos of recipes as currently the only way to have a photo is by storing an image link. 
* Create an interface for when a user shares a recipe the interface sends a message to the admin to confirm the recipe. 
* Option to choose the language of the website as the admin’s first language is Spanish, this would allow Spanish speaking users to view in their native language.
* Create a pagination for the recipes


## Technologies Used

This project uses: 

* HTML - is for the structure of the project
* CSS - is for the styles of the website 
* Bootstrap theme - is the template that is used for the project
* JavaScript - for the confirmation of the delete option
* Flask - as a framework of Python
* Python - programming all the functions that make the website work
* Mongo DB - to store the database
* Cloud 9 - for their IDE while building the website
* Heroku - to store and deploy the project


## Testing

* [W3C CSS Validation](https://jigsaw.w3.org/css-validator/)

* [W3C Markup Validation](https://validator.w3.org/)

### Manual (logical) testing of all elements and functionality on every page

#### Home Page:

1. Navigation bar:

i. Go to the "Home" page from a desktop.
ii. Change the screen size from desktop to tablet to verify that the navigation bar is responsive and switches from in line menu to burger icon dropdown menu at the appropriate place.
iii. Click on the logo in the navigation bar and verify that it links to the home page.
vi. Click on each navigation menu item and verify that it links to the correct page.

2. All Recipes section 

i. Show the name, description and image of all the recipes in the database.
ii. Click on the name or the image and verify that it links to the recipe page.


#### Vegetarian Page:

1. Navigation bar:

i. Repeat verification steps done for navbar on Home page.
ii. Confirm that navbar code is identical on all html pages.

2. Vegetarian Recipes

i. Show the name, description and image of all the Vegetarian recipes in the database.
ii. Click on the name or the image and verify that it links to the recipe page.


#### Vegan Page:

1. Navigation bar:

i. Repeat verification steps done for navbar on Home page.
ii. Confirm that navbar code is identical on all html pages.

2. Vegan Recipes

i. Show the name, description and image of all the Vegan recipes in the database.
ii. Click on the name or the image and verify that it links to the recipe page.


#### Share Recipe Page:

1. Navigation bar:

i. Repeat verification steps done for navbar on Home page.
ii. Confirm that navbar code is identical on all html pages.

2. Add Recipe Section

i. Try to submit the name empty or with mare than 30 characters and verify that an error message about the required fields appears
ii. Try to submit the form with an invalid image link and verify that a relevant error message appears
iii. Try to submit the ingredients empty or with mare than 1500 characters and verify that an error message about the required fields appears
iv. Try to submit the description empty or with mare than 300 characters and verify that an error message about the required fields appears
v. Try to submit the instructions empty or with mare than 2000 characters and verify that an error message about the required fields appears
vi. Try to submit the form with all inputs valid and verify that the recipe is added to the website.
vii. Reduce and expand width of window to verify that the form display behaves and centres the way expected, and that it looks good on all device widths.


#### recipe Page:

1. Navigation bar:

i. Repeat verification steps done for navbar on Home page.
ii. Confirm that navbar code is identical on all html pages.

2. Recipe Section

i. Show the name, description, image, ingredients, cooking tools and instructions of the recipe that was clicked in the Home Pega or in the Vegan or Vegetarian Page.
ii. Click on the delete bottom and verify that it opens a small window to cancel or confirm the deleted.
iii. Click on the the edit bottom and verify that it links to the edit page.


#### Edit Page:

1. Navigation bar:

i. Repeat verification steps done for navbar on Home page.
ii. Confirm that navbar code is identical on all html pages.

2. Add Recipe Section

i. Try to submit the name empty or with mare than 30 characters and verify that an error message about the required fields appears
ii. Try to submit the form with an invalid image link and verify that a relevant error message appears
iii. Try to submit the ingredients empty or with mare than 1500 characters and verify that an error message about the required fields appears
iv. Try to submit the description empty or with mare than 300 characters and verify that an error message about the required fields appears
v. Try to submit the instructions empty or with mare than 2000 characters and verify that an error message about the required fields appears
vi. Try to submit the form with all inputs valid and verify that the recipe is edited.
vii. Reduce and expand width of window to verify that the form display behaves and centres the way expected, and that it looks good on all device widths.


#### Cooking Tools Page:

1. Navigation bar:

i. Repeat verification steps done for navbar on Home page.
ii. Confirm that navbar code is identical on all html pages.

2. All Cooking Tools section 

i. Show the name, description and image of all the Cooking Tools in the cooking_tools.json file.
ii. Click on the name or the image and verify that it links to the Tool page.


#### Tool Page:

1. Navigation bar:

i. Repeat verification steps done for navbar on Home page.
ii. Confirm that navbar code is identical on all html pages.

2. Cooking Tools section 

i. Show the name, description and image of the Cooking Tool that is selected in the Cooking Tools Page or in the Recipe page.
ii. Show the name and image of the recipes that use that Cooking Tool.


#### Review all functionality and responsiveness:

This website was tested across multiple browsers including Chrome, Opera, Internet Explorer, Firefox and on multiple movie devices including iPhone 4, 5, and 7.  Also on Samsung and Xaomi to ensure compatibility and responsiveness.


## Deployment

This project was developed using the Cloud9 IDE, committed to git, pushed to GitHub and Heroku using the built in function within cloud9.
The database is hosted in mongoDB.

### How to run this project in Heroku

Follow this link [cookbook](https://cookbookproject.herokuapp.com/)


#### Credits

### Content

* The texts, recipes and ingredients for the website were copied from [bbcgoodfood.com](https://www.bbcgoodfood.com/)
* The texts for the cooking tools were copied from [/www.argos.co.uk]( https://www.argos.co.uk/)  

### Media

* All the images of recipes for the website were copied from [bbcgoodfood.com](https://www.bbcgoodfood.com/)
* All the images of recipes for the cooking tools were copied from [/www.argos.co.uk]( https://www.argos.co.uk/)


#### Acknowledgements

* I took the idea for this Project from the module list of recommend ideas for project.
* My mentor Brian Macharia guided me towards whole the process of design and creation of the website.
* All the team of tutors who helped throughout the realization of this project.