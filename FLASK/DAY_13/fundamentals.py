#import flask
from flask import Flask
app=Flask(__name__)

#route
@app.route("/")
def home():
    return "Home Usha"

#returning text
app.run(debug=True)




