from flask import Flask,jsonify,request

app = Flask(__name__)

pizzaDB= [
    {'name': 'tonno', 'vorm':'rond','ingredienten':['tomaat','kaas','tonijn','tarwebloem']},
    {'name': 'salami', 'vorm':'rond','ingredienten':['tomaat','kaas','salami','tarwebloem']},
    {'name': 'hawaii', 'vorm':'rond','ingredienten':['tomaat','kaas','ananas','tarwebloem']}
   ]

@app.route("/", methods = ['GET'])
def getPizza():
    return jsonify({'pizzaDB':pizzaDB})

@app.route("/<string:name>",methods = ['GET'])
def getOnePizza(name):
    resultPizza = []
    for pizza in pizzaDB:
        if pizza['name']== name:
            print(pizza)
            resultPizza.append(pizza)

    return jsonify({'pizzaDB':resultPizza})

@app.route("/", methods = ['POST'])
def addOnePizza():
    pizza = {'name': request.json['name'],'vorm':request.json['vorm'],'ingredienten': request.json['ingredienten']}
    pizzaDB.append(pizza)
    return jsonify({'pizzaDB' : pizzaDB})

if __name__ == '__main__':
    app.run()
