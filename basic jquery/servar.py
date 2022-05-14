from flask import Flask,render_template,jsonify,request

print(Flask)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("ajax.html")

@app.route('/ajax_servar')
def ajax():
    
    return jsonify({
        "name":"varun",
        "age":1,
        "table":[
            {"sub":'tamil',"mark":10},
            {"sub":'eng',"mark":110},
            {"sub":'math',"mark":30},
            ]
    })


 

value = 1

@app.route('/get_call')
def get_call():
    global value 
    return jsonify({
        "value":value
    })

@app.route('/post_call',methods=['POST'])
def post_call():
    global value 
    value += 1
    
    import json
    
    ajax = json.loads(request.form['json'])
    print(ajax['full_name'])
    return jsonify({
        "value":"respio]-"
    })

    
if __name__ == "__main__":
    app.run()