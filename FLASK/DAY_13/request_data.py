from flask import Flask, request
app = Flask(__name__)
@app.route("/search")
def search():
    name = request.args.get("name")
    return f"Hello {name}"
app.run(debug=True)