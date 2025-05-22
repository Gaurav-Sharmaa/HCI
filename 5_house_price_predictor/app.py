from flask import Flask, render_template, request
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd

app = Flask(__name__)

# Sample dataset - in real project, load from CSV
data = pd.DataFrame({
    "bedrooms": [2, 3, 4, 3, 5],
    "bathrooms": [1, 2, 2, 2, 3],
    "sqft": [800, 1200, 1500, 1300, 2000],
    "year_built": [1990, 1985, 2000, 2010, 2015],
    "location_rating": [5, 7, 8, 6, 9],
    "price": [300000, 450000, 500000, 480000, 650000]
})

# Train model
X = data[["bedrooms", "bathrooms", "sqft", "year_built", "location_rating"]]
y = data["price"]
model = LinearRegression().fit(X, y)

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get form data and make prediction
        features = [float(request.form.get(f)) for f in X.columns]
        prediction = model.predict([features])[0]
        return render_template('index.html', prediction=f"${round(prediction, 2)}")
    return render_template('index.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)