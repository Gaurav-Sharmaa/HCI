from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

print("🚀 Flask app is starting...")

# Load dataset
df = pd.read_csv('heart.csv')

# Use selected features
features = ['age', 'chol', 'cp', 'thalach', 'trestbps']
X = df[features]
y = df['target'] if 'target' in df.columns else df['num'].apply(lambda x: 1 if x > 0 else 0)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        try:
            age = float(request.form["age"])
            chol = float(request.form["chol"])
            cp = float(request.form["cp"])
            thalach = float(request.form["thalach"])
            trestbps = float(request.form["trestbps"])

            input_data = [[age, chol, cp, thalach, trestbps]]
            risk_proba = model.predict_proba(input_data)[0][1]
            risk_percent = round(risk_proba * 100, 2)

            result = f"Heart Disease Risk: {risk_percent}%"
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
