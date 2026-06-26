# 🚢 Titanic Survival Prediction using Machine Learning

## 📌 Project Overview

This project demonstrates a **Classification problem in Machine Learning** by predicting whether a passenger survived the Titanic disaster. The model learns patterns from passenger information such as age, sex, passenger class, and fare to classify passengers into two categories:

* **Survived (1)**
* **Not Survived (0)**

This project also includes a **Streamlit web application** that allows users to enter passenger details and receive survival predictions in real time.

---

## 🎯 Problem Type

**Machine Learning Task:** Classification

**Target Variable:** `Survived`

* `0` → Did Not Survive
* `1` → Survived

---

## 📂 Dataset

The dataset contains passenger information including:

* Passenger Class (Pclass)
* Sex
* Age
* SibSp (Number of siblings/spouses aboard)
* Parch (Number of parents/children aboard)
* Fare
* Embarked

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Joblib
* Streamlit
* Matplotlib
* Seaborn

---

## ⚙️ Machine Learning Workflow

### 1. Data Collection

Load the Titanic dataset.

### 2. Data Cleaning

* Handle missing values
* Remove unnecessary columns
* Encode categorical variables

### 3. Feature Engineering

Convert categorical variables into numerical format.

### 4. Data Scaling

Standardize numerical features using StandardScaler.

### 5. Model Training

Train a classification model such as:

* K-Nearest Neighbors (KNN)
* Logistic Regression
* Decision Tree
* Random Forest

### 6. Model Evaluation

Evaluate performance using:

* Accuracy Score
* Confusion Matrix
* Classification Report

### 7. Model Deployment

Deploy the trained model using Streamlit.

---

## 📁 Project Structure

```text
Titanic-Survival-Prediction/
│── 01_Classification_Algorithms.ipynb
├── main.py
├── train.csv
├── knn_titanic.pkl
├── scaler.pkl
├── columns.pkl
├── README.md
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/SubhasishOmnify-HQ/Machine-Learning-Journey/02_Classification_Algorithms
```

Install dependencies:

Run the Streamlit application:

```bash
streamlit run main.py
```

---

## 🧠 Classification Algorithms

This project focuses on supervised learning classification algorithms:

| Algorithm              | Type                        |
| ---------------------- | --------------------------- |
| Logistic Regression    | Binary Classification       |
| K-Nearest Neighbors    | Instance-Based Learning     |
| Decision Tree          | Tree-Based Classification   |
| Random Forest          | Ensemble Learning           |
| Support Vector Machine | Margin-Based Classification |

---

## 📊 Model Performance

Metrics used:

* Accuracy Score
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

## 🌐 Streamlit Application

The web application allows users to:

✅ Enter passenger details.

✅ Predict survival probability.

✅ View results instantly.

✅ Experience an interactive interface.

---

## Future Improvements

* Hyperparameter tuning
* Feature engineering
* Ensemble methods
* Model comparison
* Probability prediction
* Docker deployment
* Cloud deployment

---

## Conclusion

This project demonstrates how classification algorithms can be applied to real-world datasets. By analyzing passenger characteristics, the model predicts whether a person would have survived the Titanic disaster. It provides hands-on experience in data preprocessing, feature engineering, model training, evaluation, and deployment using Streamlit.

---

### Author

**SUBHASISH SAHOO**

Machine Learning Enthusiast | Python Developer