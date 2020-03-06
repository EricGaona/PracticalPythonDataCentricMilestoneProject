import os
from flask import Flask, render_template, redirect, request, url_for, flash, json
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipe'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstclouster-fth3h.mongodb.net/recipe?retryWrites=true&w=majority'

mongo = PyMongo(app)

# THIS FUNCTION RETRIEVE THE RECIPES FROM THE DATABASE TO BE USED IN THE index.html
@app.route('/')
def index():
     return render_template("index.html", recipes=mongo.db.recipes.find(), page_title="Home Page") 
     
    
# THIS FUNCTION SEPARATES VEGANS AND VEGETARIAS    
@app.route('/recipes/<category>')
def recipes(category):
    recipes = mongo.db.recipes.find({'category_name': category})

    return render_template('recipe_category.html',
                  recipes=recipes,
                  page_title=category.capitalize()
                 )

# THIS FUNCTION RETRIEVE THE CATEGORIES FROM THE DATABASE TO BE USED IN THE sharerecipe.html    
@app.route('/sharerecipe')
def sharerecipe():
    return render_template("sharerecipe.html", 
                           categories=mongo.db.categories.find(),
                           page_title="Share Recipe")  

# THIS FUNCTION SEND THE INFORMATION FROM THE sharerecipe.html TO THE DATABASE    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('index'))  
    
# THIS FUNCTION RETRIEVE THE INFORMATION THAT WILL BE EDIT IN THE editrecipe.html    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('editrecipe.html', recipe=the_recipe,
                           categories=all_categories,
                           page_title="Edit Recipe") 
 
 
 
                           
# THIS FUNCTION SEND THE NEW INFORMATION FROM editrecipe.html TO THE DATABASE
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'category_name':request.form.get('category_name'),
        'name':request.form.get('name'),
        'image':request.form.get('image'),
        'ingredient': request.form.get('ingredient'),
        'description': request.form.get('description')
    })
    return redirect(url_for('index')) 





# THIS FUNCTION DELETE THE RECIPE FROM THE DATABASE
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('index'))
    

@app.route('/cookingtools')
def cookingtools():
    data =[]
    with open("data/cookingtools.json", "r") as json_data:
         data = json.load(json_data)
    return render_template("cookingtools.html", page_title="Cooking Tools", cookingtools=data)
    

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash ("Thanks {}, we have recived your message!".format(request.form["name"]))
    return render_template("contact.html", page_title="Contact")

  
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
            
            

           