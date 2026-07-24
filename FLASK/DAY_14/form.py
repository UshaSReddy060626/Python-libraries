from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        name = request.form["student_name"]
        return f"Hello {name}"
    return render_template("form.html")
app.run(debug=True)