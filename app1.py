from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("model/decision_tree.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    age = int(request.form["age"])
    applicant_income = float(request.form["income"])
    loan_amount = float(request.form["loan_amount"])
    credit_history = int(request.form["credit_history"])

    data = np.array([[age, applicant_income, loan_amount, credit_history]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        result = "✅ Loan Approved"
    else:
        result = "❌ Loan Rejected"

    return render_template("index.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)