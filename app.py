
from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = joblib.load("model/heart_model.pkl")
scaler = joblib.load("model/scaler.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        features = [float(x) for x in request.form.values()]

        final_features = np.array(features).reshape(1, -1)

        final_features = scaler.transform(final_features)

        prediction = model.predict(final_features)[0]

        confidence = round(
            max(model.predict_proba(final_features)[0]) * 100,
            2
        )

        if prediction == 1:

            status = "Heart Disease Detected"
            risk = "High Risk"

            recommendations = [
                "Consult a cardiologist.",
                "Monitor blood pressure regularly.",
                "Follow a heart-healthy diet.",
                "Reduce salt and saturated fat intake.",
                "Exercise as advised by your doctor.",
                "Avoid smoking and alcohol.",
                "Schedule further medical tests."
            ]

        else:

            status = "No Heart Disease Detected"
            risk = "Low Risk"

            recommendations = [
                "Maintain a balanced diet.",
                "Exercise regularly.",
                "Get routine health checkups.",
                "Maintain a healthy body weight.",
                "Manage stress effectively.",
                "Stay physically active.",
                "Continue healthy lifestyle habits."
            ]

        return render_template(
            "result.html",
            status=status,
            risk=risk,
            confidence=confidence,
            recommendations=recommendations
        )

    except Exception as e:
        return f"Prediction Error: {e}"


# DASHBOARD ROUTE
@app.route("/dashboard")
def dashboard():

    model_data = {
        "lr": 77.05,
        "dt": 73.77,
        "rf": 83.61,
        "knn": 73.77
    }

    prediction_data = {
        "heart": 164,
        "healthy": 138
    }

    return render_template(
        "dashboard.html",
        model_data=model_data,
        prediction_data=prediction_data
    )


if __name__ == "__main__":
    app.run(debug=True)
