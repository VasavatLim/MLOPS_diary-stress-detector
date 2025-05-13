import streamlit as st
from predictor.emotion_model import predict_emotion
from predictor.stress_mapper import map_emotion_to_stress
from utils.mlflow_logger import log_prediction
import pandas as pd
import os

# Set page
st.set_page_config(
    page_title="Stress Detector from Diary",
    page_icon="📘",
    layout="centered"
)

# Set Title
st.markdown(
    "<h1 style='text-align: center; color: #4B8BBE;'>📘 Stress Detector from Diary</h1>",
    unsafe_allow_html=True
)

st.markdown("<hr style='border:1px solid #ddd;'>", unsafe_allow_html=True)

# User input
st.markdown("### 📝 Please enter today's diary entry:")
user_input = st.text_area("", placeholder="e.g. I feel overwhelmed by everything today...")

# Save result as CSV결 (for DVC)
def save_to_csv(text, emotion, score, stress):
    file_path = "data/diary_log.csv"
    os.makedirs("data", exist_ok=True)

    new_row = pd.DataFrame([{
        "text": text,
        "emotion": emotion,
        "score": round(score, 4),
        "stress_score": stress
    }])

    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df = pd.concat([df, new_row], ignore_index=True)
    else:
        df = new_row

    df.to_csv(file_path, index=False)

# Expect the emotion 
if user_input:
    emotion, score = predict_emotion(user_input)
    stress = map_emotion_to_stress(emotion, score)
    log_prediction(emotion, stress)
    save_to_csv(user_input, emotion, score, stress)

    st.markdown("<hr style='border:1px solid #ddd;'>", unsafe_allow_html=True)

    # Set colors by emotion
    emotion_colors = {
        "joy": "#FFD700",
        "love": "#FF69B4",
        "surprise": "#40E0D0",
        "neutral": "#D3D3D3",
        "sadness": "#87CEFA",
        "fear": "#FF7F50",
        "anger": "#FF6347",
        "disappointment": "#DC143C",
        "grief": "#708090",
        "nervousness": "#FFA07A",
        "admiration": "#00FA9A"
    }
    color = emotion_colors.get(emotion.lower(), "#A9A9A9")

    # Output
    st.markdown(
        f"<h3 style='color:{color}'>💡 Detected Emotion: <strong>{emotion.upper()}</strong></h3>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<h3 style='color:#FF4B4B'>🔥 Stress Score: <strong>{stress} / 10</strong></h3>",
        unsafe_allow_html=True
    )

    st.markdown("<hr style='border:1px solid #ddd;'>", unsafe_allow_html=True)
