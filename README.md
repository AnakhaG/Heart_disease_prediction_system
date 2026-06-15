# Heart Disease Prediction System ❤️

A machine learning-based web application built using **Flask** that predicts the likelihood of heart disease based on patient health parameters.

---

## 📌 Project Overview

This project uses a trained machine learning model to analyze medical input data and predict whether a person is likely to have heart disease. It also includes a simple web interface for user interaction.

---

## 🎯 Features

* User-friendly web interface
* Patient data input form
* Real-time prediction
* Trained ML model for classification
* Data visualization dashboard
* SQLite database integration for storing history

---

## 🛠️ Technologies Used

* Python 🐍
* Flask 🌐
* Scikit-learn 🤖
* Pandas & NumPy 📊
* HTML, CSS, JavaScript 🎨
* SQLite 🗄️

---

## 📁 Project Structure

```
disease_prediction/
│
├── app.py
├── train_model.py
├── predict.py
├── requirements.txt
├── model/
│   ├── heart_model.pkl
│   └── scaler.pkl
├── dataset/
│   └── heart.csv
├── database/
│   └── database.py
├── static/
├── templates/
└── notebooks/
```

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/YourUsername/Heart_disease_prediction_system.git
cd Heart_disease_prediction_system
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

```bash
venv\Scripts\activate   # Windows
source venv/bin/activate # Mac/Linux
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

---

## 📊 Dataset

The dataset used is based on standard heart disease datasets containing features like:

* Age
* Sex
* Blood Pressure
* Cholesterol
* Heart Rate
* Other medical attributes

---

## ⚠️ Disclaimer

This project is for **educational purposes only** and should not be used as a medical diagnostic tool.

---

## 👨‍💻 Author

* Developed by: **Anakha**
* Project Type: Academic / Final Year Project

---

## ⭐ Future Improvements

* Improve model accuracy
* Deploy using cloud (AWS/Heroku)
* Add user authentication system
* Enhance UI/UX design

---
