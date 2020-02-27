import os
from flask import Flask, render_template, redirect, request, url_for, flash, json
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstclouster-fth3h.mongodb.net/recipe?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
def index():
#    return "<h1>Hello</1><h2> World_3</>" esta es una forma de poner html 
#    pero no es la mas aducuada. En la linea de abajoveremos otra forma
     return render_template("index.html") 
     

@app.route('/vegans')
def vegans():
    return render_template("vegans.html")
    
@app.route('/vegetarians')
def vegetarians():
    return render_template("vegetarians.html")    
    
@app.route('/sharerecipe')
def sharerecipe():
    return render_template("sharerecipe.html")  
    
@app.route('/cookingtools')
def cookingtools():
    data =[]
    with open("data/cookingtools.json", "r") as json_data:
         data = json.load(json_data)
    return render_template("cookingtools.html", page_title="About_2 json", cookingtools=data)
    

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        
        # print("Hello, Is there anybody there? ")  ESTO SE VE EN LA CONSOLA
        # print(request.form)
        flash ("Thanks {}, we have recived your message!".format(request.form["name"]))
        
    return render_template("contact.html")
    
if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
            
            

           