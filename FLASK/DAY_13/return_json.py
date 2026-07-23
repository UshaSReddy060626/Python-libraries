from flask import Flask, jsonify
app = Flask(__name__)
@app.route("/")
def home():
    return jsonify({
        "name": "Usha",
        "course": "Flask",
        "status": "Learning"})
app.run(debug=True)