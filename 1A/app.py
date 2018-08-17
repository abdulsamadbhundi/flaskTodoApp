from flask import Flask, jsonify ,request ,jsonify ,make_response,json
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.json_util import dumps
app = Flask(__name__)
app.config['MONGO_DBNAME']='miti'
app.config['MONGO_URI']='mongodb://samad:samad123@ds121382.mlab.com:21382/practisedb'
mongo = PyMongo(app)

@app.route('/',methods=['GET'])
def get():
    todo=mongo.db.todo

    output=[]
    for q in todo.find():
        id = json.loads(dumps(q['_id']))
        output.append({'_id' : id["$oid"] ,'name' : q['name'] , 'task': q['task'], 'complete': q['complete']})


    return jsonify(output)
@app.route('/',methods=['POST'])
def add():
    output=[]
    todos=mongo.db.todo

    task=request.json['task']
    name=request.json['name']
    id=todos.insert({'task':task,'name':name,'complete':False})
    new_todo=todos.find_one({'_id': id})
    output={'name' : new_todo['name'], 'task' : new_todo['task'], 'complete' : new_todo['complete']}
    return jsonify(output)


@app.route('/update/<id>',methods=['PUT'])
def editone(id):
    todo=mongo.db.todo
    # id = json.loads(dumps(todo['_id']))
    #langs=[todoer for todoer in todos if todoer['$oid']==id]
    todose = mongo.db.todo.find_one({"_id": ObjectId(id)})
    if todose:
         todose['complete'] = True
         todo.save(todose)
         return 'Task done'
    else:
        return "no id found"
    # return jsonify({todo['complete']:'True'})


@app.route('/delete/<id>',methods=['DELETE'])
def remove(id):
    todo=mongo.db.todo
    todose = mongo.db.todo.delete_one({"_id": ObjectId(id)})
    if todose:
        return "Task Deleted"
    else :
        return "no id found"












#@app.route('/update',methods=['POST'])
##def update():
 ####   id = request.get_json(silent=True)
  ###
  ###  output=[]
   ## todos=mongo.db.todo
    #result = todos.find_one({'_id': ObjectId(id['id'])})
    # for r in result:
    #     output.append({'name': r['name'], 'task': r['task']})
    #
    #
    # todos.save(result)
    #
    # _result = todos.find_one({'id': ObjectId(id["id"])})
   #return jsonify(result)
app.run(debug=True)