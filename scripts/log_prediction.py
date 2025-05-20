# scripts/log_prediction.py

import sys
import pandas as pd
from predictor.emotion_model import predict_emotion
from predictor.stress_mapper import map_emotion_to_stress
from utils.mlflow_logger import log_prediction

text = sys.argv[1]
output_csv = "data/diary_log.csv"

label, confidence = predict_emotion(text)
stress = map_emotion_to_stress(label, confidence)

# Append to CSV
new_row = pd.DataFrame([{
    "text": text,
    "emotion": label,
    "confidence": round(confidence, 2),
    "stress_score": stress
}])

try:
    df = pd.read_csv(output_csv)
    df = pd.concat([df, new_row], ignore_index=True)
except FileNotFoundError:
    df = new_row

df.to_csv(output_csv, index=False)

# Optional MLflow logging
log_prediction(label, stress)

print(f"Logged: {label} ({confidence:.2f}), stress={stress}")