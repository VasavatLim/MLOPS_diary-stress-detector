from predictor.emotion_model import predict_emotion
from predictor.stress_mapper import map_emotion_to_stress
from utils.mlflow_logger import log_prediction
import pandas as pd
import os
from datetime import datetime
import altair as alt
import streamlit as st
import requests
# Load the secret
GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]

# Use it, for example, in headers:
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

def trigger_logging_workflow(diary_text):
    GITHUB_API = "https://api.github.com/repos/VasavatLim/MLOPS_diary-stress-detector/actions/workflows/log_diary.yml/dispatches"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }
    payload = {
    "ref": "main",
    "inputs": {
        "diary_text": diary_text  # ✅ must match the YAML
    }
}


    response = requests.post(GITHUB_API, headers=headers, json=payload)
    return response.status_code, response.text

# Set page
st.set_page_config(
    page_title="My Stress Diary",
    page_icon="📘",
    layout="wide"  
)

# Style
st.markdown("""
    <style>
        .stApp {
            background-color: #FCEED5;
            font-family: 'Georgia', serif; 
            background-image: url("https://blog.kakaocdn.net/dn/cMB7VM/btrCB7UVTbN/9xtGaEhtFkMl86KunkFSF1/img.png");
        }
        .stAppHeader{
            background-color: #FFEBEF;
        }
        .diary-icon{
            width: 65px;
            vertical-align: middle; 
            margin-right: 10px;
        }

        .img{
            margin-right: 10px;
        }
        .inputMessage{
            font-size: 2.0rem;
            margin-top: 20px;
        }
        #emotion-message{
            margin-top: 5rem;
        }
        

        .stTextArea textarea{
            font-size: 20px;
            background-color: #FFF5F7;
            border-radius: 15px; 
            border: 3px solid #FFE0E0; 
            padding: 1rem;
        }
        
        .emotion-box {
            background-color: white;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 2px 2px 12px rgba(180, 180, 180, 0.2);
            margin-top: 20px;
            text-align: center;
            border: 2px solid #FFE0E0;
        }
        
        .title {
            text-align: center;
            color: #FF1493; 
            font-size: 8rem;
            font-weight: bolder;
            margin-top: 1rem;

            text-shadow: 
                -2px -2px 0 #000,  
                2px -2px 0 #000,  
                -2px 2px 0 #000,  
                2px 2px 0 #000;  
        }
        
        .section-divider {
            border:1px solid #FFD1DC;
        }
        
        .fire-icon{
            width: 50px;
            vertical-align: middle; 
            margin-right: 10px;
        }
        
        .chart-message{
            margin: 2rem;
            font-size: 1.5rem;
            margin-left: 0;
            background-color: #FFF8F9;
            margin-right: 0;
            border-radius: 15px; 
            border: 3px solid #FFE0E0; 
            text-align: center;
            padding: 5.5px;
        }
        
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='title'>My Stress Diary</div>", unsafe_allow_html=True)
st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

# User input
st.markdown(""" <div class='inputMessage'><img class='diary-icon' src="https://cdn-icons-png.flaticon.com/512/7925/7925965.png"><strong>Write down what happened today</strong></div>""", unsafe_allow_html=True)
user_input = st.text_area(label="",placeholder="Dear Diary, today I felt...", height=300 )

# Save CSV 
def save_to_csv(text, emotion, score, stress):
    file_path = "data/diary_log.csv"
    os.makedirs("data", exist_ok=True)
    new_row = pd.DataFrame([{
        "date": datetime.today().strftime('%Y-%m-%d'),
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

# Emotional detection and making output
if user_input:
    status, msg = trigger_logging_workflow(user_input)

    if status == 204:
        st.success("✅ Your entry was logged successfully to GitHub!")
    else:
        st.error(f"❌ Failed to trigger GitHub workflow.\nStatus: {status}\nMessage: {msg}")

    emotion, score = predict_emotion(user_input)
    stress = map_emotion_to_stress(emotion, score)
    log_prediction(emotion, stress)
    save_to_csv(user_input, emotion, score, stress)

    emotion_colors = {
    "joy": "#FFE0E0",
    "love": "#FFB6C1",
    "admiration": "#FFDEE9",
    "amusement": "#FFD1DC",
    "approval": "#FFDDDD",
    "caring": "#FFE8E8",
    "gratitude": "#FFF0F5",
    "optimism": "#FFD6E8",
    "excitement": "#FFC8DD",
    "pride": "#FFE3ED",
    "relief": "#FFEBF0",
    "curiosity": "#F9CEDF",
    "desire": "#FAD5E5",
    "realization": "#FDE2E4",

    "neutral": "#F5E6E8",
    "confusion": "#EBD9EC",
    "remorse": "#EAC4D5",
    "annoyance": "#E6A5A5",
    "disappointment": "#E6A5A5",
    "nervousness": "#FADADD",
    "fear": "#F7CACA",
    "sadness": "#D8BFD8",
    "disapproval": "#ECA1A6",
    "anger": "#F08080",
    "grief": "#C1B6C9",
    "disgust": "#E57373",
    "embarrassment": "#F8C8DC"
    }

    color = emotion_colors.get(emotion.lower(), "#A9A9A9")

    st.markdown(f"""
        <div class="emotion-box">
            <h3 style='color:{color}; font-size: 2rem;'> Emotion: <strong>{emotion.upper()}</strong></h3>
            <h3 style='color:#FF6F61; font-size: 1.8rem;'> Stress Score: <strong>{stress} / 10</strong></h3>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

# Vilualize recorded data
def load_and_plot_log():
    file_path = "data/diary_log.csv"
    if not os.path.exists(file_path):
        st.info("No diary history found yet.")
        return

    df = pd.read_csv(file_path)
    if 'stress_score' not in df.columns or 'date' not in df.columns or 'emotion' not in df.columns:
        st.warning("The CSV file does not contain valid stress data.")
        return

    df['date'] = pd.to_datetime(df['date'])
    df.sort_values('date', inplace=True)

    st.markdown(""" <div class='inputMessage' id='emotion-message'><img class='diary-icon' src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTjNRqGa0qMKkoO6xiweZV1hSOYWhLVwh7A3w&s"><strong>Emotion & Stress Trends</strong> </div>""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    
    line_chart = alt.Chart(df).mark_line(
    color='#FF8DAA',  
    strokeWidth=3
    ).encode(
        x='date:T',
        y='stress_score:Q'
    ).properties(
        width=600,
        height=300,
        title='Stress Score Over Time'
    ).configure_axis(
        labelFontSize=12,
        titleFontSize=14
    ).configure_title(
        fontSize=16,
        anchor='start'
    )
    
    emotion_counts = df['emotion'].value_counts()
    
    emotion_df = emotion_counts.reset_index()
    emotion_df.columns = ['emotion', 'count']

    color_map = {
    "joy": "#FFE0E0",
    "love": "#FFB6C1",
    "admiration": "#FFDEE9",
    "amusement": "#FFD1DC",
    "approval": "#FFDDDD",
    "caring": "#FFE8E8",
    "gratitude": "#FFF0F5",
    "optimism": "#FFD6E8",
    "excitement": "#FFC8DD",
    "pride": "#FFE3ED",
    "relief": "#FFEBF0",
    "curiosity": "#F9CEDF",
    "desire": "#FAD5E5",
    "realization": "#FDE2E4",

    "neutral": "#F5E6E8",
    "confusion": "#EBD9EC",
    "remorse": "#EAC4D5",
    "annoyance": "#E6A5A5",
    "disappointment": "#E6A5A5",
    "nervousness": "#FADADD",
    "fear": "#F7CACA",
    "sadness": "#D8BFD8",
    "disapproval": "#ECA1A6",
    "anger": "#F08080",
    "grief": "#C1B6C9",
    "disgust": "#E57373",
    "embarrassment": "#F8C8DC"
    }

    bar_chart = alt.Chart(emotion_df).mark_bar().encode(
        x=alt.X('emotion:N', title='Emotion'),
        y=alt.Y('count:Q', title='Count'),
        color=alt.Color('emotion:N', scale=alt.Scale(domain=list(color_map.keys()), range=list(color_map.values())), legend=None),
    ).properties(
        width=600,
        height=300,
        title='Emotion Distribution'
    ).configure_axis(
        labelFontSize=12,
        titleFontSize=14
    ).configure_title(
        fontSize=16,
        anchor='start'
    )

    with col1:
        st.markdown("""<div class='chart-message'><img class='fire-icon' src="https://cdn-icons-png.flaticon.com/512/11280/11280633.png"/> Daily Stress Score</div>""", unsafe_allow_html=True)
        # st.line_chart(df.set_index('date')['stress_score'])
        st.altair_chart(line_chart, use_container_width=True)

    with col2:
        st.markdown(""" <div class='chart-message'><img class='fire-icon' src="https://cdn-icons-png.flaticon.com/512/11280/11280633.png"/>Emotion Frequency""", unsafe_allow_html=True)
        emotion_counts = df['emotion'].value_counts()
        st.altair_chart(bar_chart, use_container_width=True)
    ##
        

    # Emtion stastics + summary
    st.markdown(""" <div class='chart-message'><img class='fire-icon' src="https://cdn-icons-png.flaticon.com/512/11280/11280633.png"/>Emotion Statistics</div>""", unsafe_allow_html=True)

    # st.dataframe(df['stress_score'].describe().to_frame().rename(columns={"stress_score": "value"}), height=200)
    desc_df = df['stress_score'].describe().to_frame().rename(columns={"stress_score": "value"})
    desc_df['value'] = desc_df['value'].map(lambda x: f"{x:.2f}")  # 문자열로 변환

    styled = desc_df.style\
    .set_table_styles([
        {'selector': 'th', 'props': [('text-align', 'center'), ('background-color', '#FADADD')]}
    ])\
    .applymap(lambda x: 'text-align: center;', subset=['value'])\
    .set_properties(**{
        'font-size': '14px',
        'color': '#333',
        'background-color': '#FAF3F3'
    })

    st.table(styled)




# Do visualization
load_and_plot_log()
