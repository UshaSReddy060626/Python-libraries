#import required libraries
from flask import Flask, request, jsonify
app = Flask(__name__)

#request.args example
@app.route("/student")
def student():

    #get data from url
    name = request.args.get("name")
    age = request.args.get("age")
    return f"Name: {name}, Age: {age}"

#request.json and jsonify example
@app.route("/predict", methods=["POST"])
def predict():

    #receive json data
    data = request.json

    #get values
    experience = data["experience"]

    #dummy ai prediction
    salary = experience * 10000

    #return json response
    return jsonify({
        "experience": experience,
        "predicted_salary": salary,
        "status": "Success"
    })
app.run(debug=True)