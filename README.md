# 📊 Customer Churn Prediction System Using Predictive Analytics and Machine Learning

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.59-red?logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![License](https://img.shields.io/badge/License-MIT-green)

A machine learning web application that predicts customer churn using **Predictive Analytics**, **Scikit-Learn**, and **Streamlit**.

Developed as the **Major Project** for the **Master of Computer Applications (MCA)** program at **Chandigarh University**.

---
## 📑 Table of Contents

- Project Objectives
- Features
- Technologies Used
- Machine Learning Models
- Project Structure
- Dataset
- Installation
- Application Screenshots
- Future Improvements
- Author
- License

## 📌 Project Objectives

- Analyze customer churn patterns using exploratory data analysis.
- Identify factors influencing customer churn.
- Build and compare multiple machine learning models.
- Predict customer churn using the best-performing model.
- Provide an interactive dashboard for visualization and prediction.

---

## ✨ Features

- 📊 Interactive Streamlit Dashboard
- 📈 Exploratory Data Analysis (EDA)
- 🤖 Customer Churn Prediction
- 📉 Model Performance Comparison
- 📥 Download Prediction Results
- 📋 Project Information Page

---

## 🛠️ Technologies Used

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-Learn |
| Web Framework | Streamlit |
| Model Serialization | Joblib |
| Excel Support | OpenPyXL |

---

## 🤖 Machine Learning Models

| Model | Accuracy |
|-------|----------|
| Logistic Regression | **80.34%** ✅ |
| Random Forest | 79.49% |
| Decision Tree | 78.50% |

**Selected Model:** Logistic Regression

---

## 📂 Project Structure

```text
customer-churn-prediction-system/
│
├── assets/
├── data/
│   ├── raw/
│   └── cleaned/
├── images/
├── models/
├── notebooks/
├── reports/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── streamlit_app.py
```

---

## 📊 Dataset

**Dataset:** IBM Telco Customer Churn Dataset

The dataset contains customer demographic information, subscription details, service usage, billing information, and churn status.

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/PriyanshuChand/customer-churn-prediction-system.git
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
python -m streamlit run streamlit_app.py
```

---

## 📸 Application Screenshots

### Home Page

![Home](screenshots/home_page.png)

### Data Analysis

![Dashboard](screenshots/data_analysis.png)

### Predict Churn

![Prediction](screenshots/predict_churn.png)

### About Project

![About](screenshots/about_project.png)

---

## 🚀 Future Improvements

- Deploy the application using Streamlit Community Cloud.
- Add XGBoost and LightGBM models.
- Integrate a real-time customer database.
- Add user authentication.
- Improve prediction accuracy using hyperparameter tuning.
- Support batch predictions through CSV upload.Add user authentication and login.

---

## 👨‍💻 Author

**Priyanshu Chand**

Master of Computer Applications (MCA)

Chandigarh University

📧 GitHub: https://github.com/PriyanshuChand

---

## 📜 License

This project is licensed under the MIT License.