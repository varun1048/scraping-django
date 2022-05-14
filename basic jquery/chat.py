from flask import Flask,render_template,jsonify,request,jsonify
import json

print(Flask)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("chat.html")

@app.route('/message',methods=['POST'])
def message():
    ajax = json.loads(request.form['ajax'])
    print(ajax["message"])
    response = jsonify({'message': ajax["message"]+" from server" })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    
    
    
app.run()