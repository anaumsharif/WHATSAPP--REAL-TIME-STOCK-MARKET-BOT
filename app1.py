from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return{
        "Result ": "You have successfully created the first route ! "
    }
    
@app.route("/webhook",methods = ["POST"])
def webhook():
    message = request.form['message']
    return{
        "Result ": message
    }