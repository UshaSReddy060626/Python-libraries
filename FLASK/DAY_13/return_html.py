from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "<h1>Welcome</h1><p>This is Flask</p>"
app.run(debug=True)