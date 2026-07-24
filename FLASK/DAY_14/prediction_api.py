#import required libraries
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def predict():
    if request.method == "POST":
        experience = float(request.form["experience"])
        #dummy ai prediction
        salary = experience * 10000
        return f"Predicted Salary: ₹{salary}"
    return render_template("predict.html")
app.run(debug=True)