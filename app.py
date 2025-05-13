import streamlit as st
from predictor.emotion_model import predict_emotion
from predictor.stress_mapper import map_emotion_to_stress
from utils.mlflow_logger import log_prediction

# 페이지 설정
st.set_page_config(
    page_title="Stress Detector from Diary",
    page_icon="📘",
    layout="centered"
)

# 타이틀
st.markdown(
    "<h1 style='text-align: center; color: #4B8BBE;'>📘 Stress Detector from Diary</h1>",
    unsafe_allow_html=True
)

st.markdown("<hr style='border:1px solid #ddd;'>", unsafe_allow_html=True)

# 사용자 입력
st.markdown("### 📝 Please enter today's diary entry:")
user_input = st.text_area("", placeholder="e.g. I feel overwhelmed by everything today...")

# 예측 실행
if user_input:
    emotion, score = predict_emotion(user_input)
    stress = map_emotion_to_stress(emotion)
    log_prediction(emotion, stress)

    st.markdown("<hr style='border:1px solid #ddd;'>", unsafe_allow_html=True)

    # 감정별 색상 지정
    emotion_colors = {
        "joy": "#FFD700",
        "love": "#FF69B4",
        "surprise": "#40E0D0",
        "neutral": "#D3D3D3",
        "sadness": "#87CEFA",
        "fear": "#FF7F50",
        "anger": "#FF6347"
    }
    color = emotion_colors.get(emotion.lower(), "#A9A9A9")

    # 출력
    st.markdown(
        f"<h3 style='color:{color}'>💡 Detected Emotion: <strong>{emotion.upper()}</strong></h3>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<h3 style='color:#FF4B4B'>🔥 Stress Score: <strong>{stress} / 10</strong></h3>",
        unsafe_allow_html=True
    )

    st.markdown("<hr style='border:1px solid #ddd;'>", unsafe_allow_html=True)
