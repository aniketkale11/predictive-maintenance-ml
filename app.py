
import streamlit as st
import numpy as np
import joblib
import os

# Load model with correct path
model_path = os.path.join(os.path.dirname(__file__), "rf_model.pkl")
model = joblib.load(model_path)

st.set_page_config(page_title="Bearing Health Monitor")
st.title("Bearing Health Monitor")
st.markdown("### Enter Vibration Feature Values:")

col1, col2 = st.columns(2)

with col1:
    rms          = st.number_input("RMS",          value=0.0, format="%.6f")
    std          = st.number_input("STD",          value=0.0, format="%.6f")
    kurtosis     = st.number_input("Kurtosis",     value=0.0, format="%.6f")
    skewness     = st.number_input("Skewness",     value=0.0, format="%.6f")

with col2:
    crest_factor = st.number_input("Crest Factor", value=0.0, format="%.6f")
    peak_to_peak = st.number_input("Peak to Peak", value=0.0, format="%.6f")
    fft_energy   = st.number_input("FFT Energy",   value=0.0, format="%.6f")

if st.button("PREDICT HEALTH"):
    features = np.array([[rms, std, kurtosis, skewness,
                          crest_factor, peak_to_peak, fft_energy]])
    prediction = model.predict(features)[0]

    fault_map = {0: "Normal", 1: "Inner Race Fault", 2: "Outer Race Fault"}

    if prediction == 0:
        health = 95
        severity = "Low"
        action = "No action needed"
    elif prediction == 1:
        health = 45
        severity = "Critical"
        action = "Immediate maintenance required!"
    else:
        health = 30
        severity = "Critical"
        action = "Immediate maintenance required!"

    st.markdown("---")
    st.markdown("## Health Monitor Result")
    st.markdown(f"**Status      :** {fault_map[prediction]}")
    st.markdown(f"**Health Score:** {health}/100")
    st.markdown(f"**Severity    :** {severity}")
    st.markdown(f"**Action      :** {action}")
    st.progress(health)
