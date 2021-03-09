from flask import Flask, request,Response,jsonify
import configparser

config = configparser.ConfigParser()
config.read('config')
app = Flask(__name__)
list_of_items = {}
@app.route('/item',methods=['GET','POST','DELETE'])
def items():
   if request.method == 'GET':
       return jsonify(list_of_items)

   if request.method == 'POST':
       content = request.get_json(silent=False)
       if not request.is_json:
           return Response("{'Error':'not valid json'}", status=400,mimetype='application/json')
       else:
           list_of_items[str(content['id'])] = str(content['name'])
           return Response("{'Message':'Added to items'}",status=200,mimetype='application/json')

   if request.method == 'DELETE':
       content = request.get_json(silent=False)
       if not request.is_json:
           return Response("{'Error':'not valid json'}", status=400,mimetype='application/json')
       else:
           del list_of_items[str(content['id'])]
           return Response("{'Message':'Item deleted'}", status=200,mimetype='application/json')

if __name__=='__main__':
    app.run(port=config['DEFAULT']['Port'])
        

    