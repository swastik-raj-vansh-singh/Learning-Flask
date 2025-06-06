from flask import Flask ,jsonify,request

app = Flask(__name__)

items = [
    {"id":1 , "name" : "Item1" , "description": "this is item 1"},
    {"id":2 , "name" : "Item2" , "description": "this is item 2"}
]

@app.route("/")
def home():
    return ("Welcome to the home page od to do list")


# retrive all the items 
@app.route('/items',methods = ['GET'])
def get_items():
    return jsonify(items)


# retireve a specific items
@app.route('/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id),None)
    if item is None:
        return jsonify({"error": "item not found"})
    
    return jsonify(item)


# post : create a new task
@app.route('/items',methods=['POST'])
def create_item():
    if not request.josn or not 'name' in  request.json:
        return jsonify({"errork": "item not found"})
    
    new_item = {
        "id" : items[-1]["id"] + 1 if items else 1,
        "name" : request.json("name"),
        "description" : request.json("description")
    }

    items.append(new_item)
    return jsonify(new_item)


# PUT : update the existing item
@app.route('/items/<int:item_id>',methods = ['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id),None)

    if item is None:
        return jsonify({"error": "item not found"})
    
    items["name"] = request.json.get('name',item['name'])
    items["description"] = request.json.get('description',item['description'])
    return jsonify(item)


# DELECT : Deleting an items
@app.route('/items/<int:item_id>',methods = ['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"result" : " Item deleted"})


if __name__ == "__main__":
    app.run()