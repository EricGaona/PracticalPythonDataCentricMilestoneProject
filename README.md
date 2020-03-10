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

W3C CSS Validation

W3C Markup Validation

Vegetarian and Vegan:

When we click the delete button, we open a confirmation window that asks “Are you sure you want to delete this recipe?” with an OK button to confirm and another button to cancel. If the user confirms they want to delete, all the information on the recipe will be deleted from the database. If the user doesn’t confirm they want to delete they will be returned to the previous page. 
When the edit button is clicked, it opens a form with all the recipe information and it allows the user to edit the files.  
Once the user is happy with their edits they should click the save button at the bottom of the form. 

Share Recipe:

The Share Recipe tab takes the user to a form.  Every section of the form is compulsory to be completed in order to share a recipe. The Name of Recipe box only accepts a maximum of 30 characters.  The image should be a URL.  The ingredients a maximum of 450 characters and the description a maximum of 350 characters. 
At the bottom, there is a submit button to save and share recipe. When the Submit button is clicked it sends the information to the database and then redirects the user to the homepage. 







