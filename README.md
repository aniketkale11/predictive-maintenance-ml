# Predictive Maintenance & Bearing Fault Detection

## Problem Statement
Rotating machinery in factories contains bearings that develop 
faults over time. Undetected faults cause unexpected breakdowns 
and huge financial losses. This project detects faults early 
using vibration sensor data.

## Dataset
CWRU Bearing Dataset — Real vibration sensor data
- Normal bearing data
- Inner Race fault data  
- Outer Race fault data

## Approach
1. Loaded raw .mat vibration files
2. Extracted 7 features using sliding window
   - RMS, STD, Kurtosis, Skewness
   - Crest Factor, Peak-to-Peak, FFT Energy
3. Trained Isolation Forest for anomaly detection
4. Trained Autoencoder for health score
5. Trained Random Forest for fault classification

## Results
- Anomaly Detection Rate : 100%
- Classification Accuracy: 100%
- Fault Types Detected   : Normal / Inner Race / Outer Race

## Health Monitor Output
Status      : ⚠️ Inner Race Fault
Health Score: 45/100
Severity    : Critical
Action      : Immediate maintenance required!

## Libraries Used
- Python, NumPy, Pandas
- Scikit-learn, TensorFlow
- Matplotlib, Bokeh
- SciPy
