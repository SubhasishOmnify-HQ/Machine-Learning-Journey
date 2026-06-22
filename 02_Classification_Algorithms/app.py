import streamlit as st
import pandas as pd
import joblib
import time

st.set_page_config(page_title="Heart Disease Prediction", page_icon="❤️")

# Load model files
model = joblib.load("knn_titanic.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")

# CSS
st.markdown("""
<style>
.risk-box{
    background:linear-gradient(135deg,#ff4b4b,#ff7b7b);
    color:white;
    padding:30px;
    border-radius:20px;
    text-align:center;
    font-size:30px;
    font-weight:bold;
    animation:pulse 1.2s infinite;
}

.safe-box{
    background:linear-gradient(135deg,#00c853,#64dd17);
    color:white;
    padding:30px;
    border-radius:20px;
    text-align:center;
    font-size:30px;
    font-weight:bold;
    animation:glow 1.5s infinite;
}

@keyframes pulse{
0%{transform:scale(1);}
50%{transform:scale(1.08);}
100%{transform:scale(1);}
}

@keyframes glow{
0%{box-shadow:0 0 10px #00ff00;}
50%{box-shadow:0 0 40px #00ff00;}
100%{box-shadow:0 0 10px #00ff00;}
}
</style>
""", unsafe_allow_html=True)

st.title("❤️ Heart Disease Prediction")
st.write("Developed by Akarsh")

# Inputs
age = st.slider("Age", 18, 100, 40)
sex = st.selectbox("Sex", ["M", "F"])
chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])
resting_bp = st.number_input("Resting Blood Pressure", 80, 200, 120)
cholesterol = st.number_input("Cholesterol", 100, 600, 200)
fasting_bs = st.selectbox("Fasting Blood Sugar >120", [0, 1])
resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
max_hr = st.slider("Maximum Heart Rate", 60, 220, 150)
exercise_angina = st.selectbox("Exercise Angina", ["Y", "N"])
oldpeak = st.slider("Oldpeak", 0.0, 6.0, 1.0)
st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

if st.button("Predict"):

    with st.spinner("🔍 Analyzing..."):
        progress = st.progress(0)

        for i in range(100):
            time.sleep(0.02)
            progress.progress(i + 1)

    raw_input = {
        "Age": age,
        "RestingBP": resting_bp,
        "Cholesterol": cholesterol,
        "FastingBS": fasting_bs,
        "MaxHR": max_hr,
        "Oldpeak": oldpeak,
        "Sex_" + sex: 1,
        "ChestPainType_" + chest_pain: 1,
        "RestingECG_" + resting_ecg: 1,
        "ExerciseAngina_" + exercise_angina: 1,
        "ST_Slope_" + st_slope: 1
    }

    input_df = pd.DataFrame([raw_input])

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]

    scaled_input = scaler.transform(input_df)

    prediction = model.predict(scaled_input)[0]

    if prediction == 1:
        st.markdown("""
        <div class="risk-box">
        ⚠️ HIGH RISK OF HEART DISEASE
        </div>
        """, unsafe_allow_html=True)

    else:
        st.balloons()
        st.markdown("""
        <div class="safe-box">
        ✅ GOOD HEART HEALTH
        </div>
        """, unsafe_allow_html=True)