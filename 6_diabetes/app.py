from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
cols = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", 
        "Insulin", "BMI", "DiabetesPedigreeFunction", "Age", "Outcome"]
df = pd.read_csv(url, names=cols)

# Features to use (match these with your form field names)
features = {
    'age': 'Age',
    'glucose': 'Glucose',
    'bp': 'BloodPressure',
    'bmi': 'BMI',
    'dpf': 'DiabetesPedigreeFunction'
}

X = df[list(features.values())]
y = df["Outcome"]
model = RandomForestClassifier(random_state=42).fit(X, y)

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get form data using the correct field names
            input_data = [
                float(request.form['age']),
                float(request.form['glucose']),
                float(request.form['bp']),
                float(request.form['bmi']),
                float(request.form['dpf'])
            ]
            prediction = model.predict([input_data])[0]
            result = "Diabetic" if prediction == 1 else "Non-Diabetic"
        except KeyError as e:
            return f"Missing form field: {e}", 400
        except ValueError as e:
            return f"Invalid input: {e}", 400
            
        return render_template('index.html', result=result)
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)