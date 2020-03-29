import os
from flask import Flask, render_template, redirect, request, url_for, flash, json
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = "some_secret"

app.config["MONGO_DBNAME"] = "recipe"
app.config["MONGO_URI"] = "mongodb+srv://root:r00tUser@myfirstclouster-fth3h.mongodb.net/recipe?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route("/")
def index():
    """
    THIS FUNCTION RETRIEVE THE RECIPES FROM THE DATABASE TO BE USED IN THE index.html
    """
    return render_template("index.html", recipes=mongo.db.recipes.find(), page_title="All Recipes") 
     
    
@app.route("/recipes/<category>")
def recipes(category):
    """
    THIS FUNCTION SEPARATES VEGANS AND VEGETARIAS
    """
    recipes = mongo.db.recipes.find({"category_name": category})

    return render_template("recipe_category.html",
                  recipes=recipes,
                  page_title=category.capitalize()
                 )

@app.route("/share_recipe")
def share_recipe():
    """
    THIS FUNCTION RETRIEVE THE CATEGORIES FROM THE DATABASE TO BE USED IN THE sharerecipe.html
    """
    return render_template("share_recipe.html", 
                           categories=mongo.db.categories.find(),
                           page_title="Add Recipe")  


@app.route("/insert_recipe", methods=["POST"])
def insert_recipe():
    """
    THIS FUNCTION SEND THE INFORMATION FROM THE sharerecipe.html TO THE DATABASE 
    AND VALIDATED THE NAME, INGREDIENT AND DESCRIPTION
    """
    recipes = mongo.db.recipes
    name = request.form["name"]
    ingredients = request.form["ingredients"]
    description = request.form["description"]
    error_name = ""
    error_ingredients = ""
    error_description = ""
    error_found = False
    
    if len(name) == 0 or len(name) > 30:
        error_found = True
        error_name = "The name should not be empty or longer than 30 characters long."
   
    if len(ingredients) == 0 or len(ingredients) > 450:
        error_found = True    
        error_ingredients = "The ingredient should not be empty or longer than 450 characters long."
    
    if len(description) == 0 or len(description) > 350:
        error_found = True
        error_description = "The description should not be empty or longer than 350 characters long."
    
    if error_found:  
       
        return render_template("sharerecipe.html", error_name=error_name, 
                                error_ingredients=error_ingredients, 
                                error_description=error_description )
    else:
        recipes.insert_one(request.form.to_dict())
        return redirect(url_for("index"))  
    
    
@app.route("/edit_recipe/<recipe_id>")
def edit_recipe(recipe_id):
    """
    THIS FUNCTION RETRIEVE THE INFORMATION THAT WILL BE EDIT IN THE editrecipe.html
    """
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories =  mongo.db.categories.find()
    return render_template("editrecipe.html", recipe=the_recipe,
                           categories=all_categories,
                           page_title="Edit Recipe") 
 


@app.route("/update_recipe/<recipe_id>", methods=["POST"])
def update_recipe(recipe_id):
    """
    THIS FUNCTION SEND THE NEW INFORMATION FROM editrecipe.html TO THE DATABASE
    """
    
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories =  mongo.db.categories.find()
    recipes = mongo.db.recipes
    name = request.form["name"]
    ingredients = request.form["ingredients"]
    description = request.form["description"]
    error_name = ""
    error_ingredients = ""
    error_description = ""
    error_found = False
    
    if len(name) == 0 or len(name) > 30:
        error_found = True
        error_name = "The name should not be empty or longer than 30 characters long."
    
    if len(ingredients) == 0 or len(ingredients) > 450:
        error_found = True    
        error_ingredients = "The ingredient should not be empty or longer than 450 characters long."
    
    if len(description) == 0 or len(description) > 350:
        error_found = True
        error_description = "The description should not be empty or longer than 350 characters long."
    
    if error_found: 
        
        return render_template("edit_recipe.html", recipe=the_recipe, categories=all_categories,
                                error_name=error_name, error_ingredients=error_ingredients, 
                                error_description=error_description)
    else:
        recipes.update( {"_id": ObjectId(recipe_id)},
        {
            "category_name":request.form.get("category_name"),
            "name":request.form.get("name"),
            "image":request.form.get("image"),
            "ingredients": request.form.get("ingredients"),
            "description": request.form.get("description")
        })
        
        return redirect(url_for("index")) 
  

@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """
    THIS FUNCTION DELETE THE RECIPE FROM THE DATABASE
    """
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    return redirect(url_for("index"))
    
    

@app.route("/recipe/<name>")
def recipe(name):
    """
    THIS FUNCTION SHOWS THE SELECTED RECIPE IN recipe_category.html
    """
   
    return render_template("recipe.html", 
                            recipes=mongo.db.recipes.find({"name": name}))


@app.route("/cooking_tools")
def cooking_tools():
    """
    THIS FUNCTION RETRIEVE ALL THE COOKING TOOLS FROM THE cookingtools.json AND SHOWS IN THE cookingtools.html
    """
    data =[]
    with open("data/cooking_tools.json", "r") as json_data:
         data = json.load(json_data)
    return render_template("cooking_tools.html", page_title="Cooking Tools", cookingtools=data)
    
   
@app.route("/recipe/<tool>")
def tool_recipe(tool):
    """
    THIS FUNCTION RECEIVES THE TOOL SELECTED IN recipe.html AND SHOWS IN THE tool.html
    """
    item = {}
    with open("data/cooking_tools.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj ["tool"] == tool:
                item = obj
                
    return render_template("tool.html", item=item)   
  

@app.route("/cooking_tools/<tool>")
def tool_cookingtools(tool):
    """
    THIS FUNCTION RECEIVES THE TOOL SELECTED IN cookingtools.html AND SHOWS IN THE tool.html
    """
    item = {}
    
    with open("data/cooking_tools.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj ["tool"] == tool:
                item = obj
                
    return render_template("tool.html", item=item)      
    


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash ("Thanks {}, we have recived your message!".format(request.form["name"]))
    return render_template("contact.html", page_title="Contact")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
            
            

           