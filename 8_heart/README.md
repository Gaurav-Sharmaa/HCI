# ❤️ Heart Disease Risk Prediction Web App

This is a simple Flask-based web application that predicts the risk of heart disease using basic health parameters like age, cholesterol, chest pain type, etc. The prediction is powered by a Logistic Regression model from scikit-learn.

---

python -m ensurepip --upgrade

pip install Flask==3.1.1 scikit-learn==1.6.1 pandas==2.2.3 numpy==2.2.6

python app.py

✅ Sample Input 1 (Low Risk Example)
Field	Value
Age	45
Chol	180
CP	0
Thalach	170
Trestbps	120

👉 Expected result: Lower risk percentage (e.g., ~10–30%)

✅ Sample Input 2 (Moderate Risk Example)
Field	Value
Age	58
Chol	240
CP	2
Thalach	140
Trestbps	135

👉 Expected result: Moderate risk (e.g., ~40–60%)

✅ Sample Input 3 (High Risk Example)
Field	Value
Age	65
Chol	300
CP	3
Thalach	100
Trestbps	160

👉 Expected result: Higher risk (e.g., ~70–90%)