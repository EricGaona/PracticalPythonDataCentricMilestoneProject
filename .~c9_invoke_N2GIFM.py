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
    return render_template("index.html", recipes=mongo.db.recipes.find(), page_title="All Recipes", title="Home Page") 
     
    
@app.route("/recipes/<category>")
def recipes(category):
    """
    THIS FUNCTION SEPARATES VEGANS AND VEGETARIAS
    """
    recipes = mongo.db.recipes.find({"category_name": category})
    print("hola_1")
    print(category)
    print("hola_2")
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
    THIS FUNCTION SEND THE INFORMATION FROM THE share_recipe.html TO THE DATABASE 
    AND VALIDATED THE NAME, INGREDIENT AND DESCRIPTION
    """
    recipes = mongo.db.recipes
    name = request.form["name"]
    ingredients = request.form["ingredients"]
    description = request.form["description"]
    instructions = request.form["instructions"]
    
    error_name = ""
    error_ingredients = ""
    error_description = ""
    error_instructions = ""
    error_found = False
    
    if len(name) == 0 or len(name) > 30 or name.isspace() == True:
        error_found = True
        error_name = "The name should not be empty or longer than 30 characters long."
   
    if len(ingredients) == 0 or len(ingredients) > 1500 or ingredients.isspace() == True:
        error_found = True    
        error_ingredients = "The ingredient should not be empty or longer than 1500 characters long."
    
    if len(description) == 0 or len(description) > 300 or description.isspace() == True:
        error_found = True
        error_description = "The description should not be empty or longer than 300 characters long."
        
    if len(instructions) == 0 or len(instructions) > 2000 or instructions.isspace() == True:
        error_found = True
        error_instructions = "The instructions should not be empty or longer than 2000 characters long."
    
    if error_found:  
        
        return render_template("share_recipe.html", error_name=error_name, 
                                error_ingredients=error_ingredients, 
                                error_description=error_description,
                                error_instructions=error_instructions,
                                categories=mongo.db.categories.find(),
                                page_title="Add Recipe", title="Share Recipe")
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
    return render_template("edit_recipe.html", recipe=the_recipe,
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
    instructions = request.form["instructions"]
    error_name = ""
    error_ingredients = ""
    error_description = ""
    error_instructions = ""
    error_found = False
    
    if len(name) == 0 or len(name) > 30 or name.isspace() == True:
        error_found = True
        error_name = "The name should not be empty or longer than 30 characters long."
    
    if len(ingredients) == 0 or len(ingredients) > 1500 or ingredients.isspace() == True:
        error_found = True    
        error_ingredients = "The ingredient should not be empty or longer than 1500 characters long."
    
    if len(description) == 0 or len(description) > 300 or description.isspace() == True:
        error_found = True
        error_description = "The description should not be empty or longer than 300 characters long."
        
    if len(instructions) == 0 or len(instructions) > 2000 or instructions.isspace() == True:
        error_found = True    
        error_instructions = "The instructions should not be empty or longer than 2000 characters long."
    
    if error_found: 
        
        return render_template("edit_recipe.html", recipe=the_recipe, categories=all_categories,
                                error_name=error_name, error_ingredients=error_ingredients, 
                                error_instructions=error_instructions, 
                                error_description=error_description, page_title="Edit Recipe")
    else:
        recipes.update( {"_id": ObjectId(recipe_id)},
        {
            "category_name":request.form.get("category_name"),
            "name":request.form.get("name"),
            "image":request.form.get("image"),
            "ingredients": request.form.get("ingredients"),
            "description": request.form.get("description"),
            "instructions": request.form.get("instructions")
        })
        
        return redirect(url_for("index")) 
  

@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """
    THIS FUNCTION DELETE THE RECIPE FROM THE DATABASE
    """
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    return redirect(url_for("index"))

@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    """
    THIS FUNCTION SHOWS THE SELECTED RECIPE IN index.html AND recipe_category.html   xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    """
    the_recipe_id =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_recipes=mongo.db.recipes.find()
    the_recipe_id= the_recipe_id
    recipes = mongo.db.recipes.find()
    recipe_title=[]
    for recipe in recipes:
        if '_id' in recipe:
            if the_recipe_id == recipe["_id"]:
                print("entra")
                recipe_title = recipe["name"]
                break
            
    print("the_recipe_id")    
    print("hola_3")        
    print(recipe_title)
    print("hola_4")
    return render_template("recipe.html", the_recipe_id=the_recipe_id, 
                            all_recipes=all_recipes, title=recipe_title) 


@app.route("/cooking_tools")
def cooking_tools():
    """
    THIS FUNCTION RETRIEVE ALL THE COOKING TOOLS FROM THE cookingtools.json AND SHOWS IN THE cookingtools.html
    """
    data =[]
    with open("data/cooking_tools.json", "r") as json_data:
         data = json.load(json_data)
    return render_template("cooking_tools.html", page_title="Cooking Tools", cookingtools=data)
    

@app.route("/cooking_tools/<tool>")
def tool_cookingtools(tool):
    """
    THIS FUNCTION RECEIVES THE TOOL SELECTED IN cookingtools.html AND IN THE recipe.html AND SHOWS IN THE tool.html
    """
    recipes = mongo.db.recipes.find()
    recipes_to_display =[]
    for recipe in recipes:
        if 'tool' in recipe:
            tools = recipe['tool'].split(",")
            if tool in tools:
                recipes_to_display.append(recipe)
 
    item = {}
    
    with open("data/cooking_tools.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            """
            tools = [x for x in obj["tool"].split(",")]
            for x in tools:
                 if x == tool:
                    item = x
            """
            if obj ["tool"] == tool:
                item = obj
                
    return render_template("tool.html", item = item, all_recipes = recipes_to_display)    


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash ("Thanks {}, we have recived your message!".format(request.form["name"]))
    return render_template("contact.html", page_title="Contact")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
            
            

           