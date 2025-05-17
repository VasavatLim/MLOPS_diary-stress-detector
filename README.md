# README.md
# 📘 Stress Detection from Diary Text

## 🧠 Project Overview
This project is a web application that predicts a user's emotional state from a diary entry and estimates their stress score based on the emotion. Built with Streamlit, it provides an intuitive UI where users enter diary text and view visual results. MLflow is used for experiment tracking, and prediction logs are saved to CSV and version-controlled with DVC.

---

## 🔧 Tools and Technologies Used

| Tool                        | Purpose |
|-----------------------------|---------|
| **Hugging Face Transformers** | Pretrained model for emotion classification (RoBERTa-based) |
| **Hugging Face Tokenizer** | To tokenize the text |
| **Streamlit**               | Web interface development |
| **MLflow**                  | Logging experiments, parameters, and metrics |
| **DVC (Data Version Control)** | Versioning of output CSV files |
| **Pandas**                  | CSV handling and manipulation |
| **Torch**                   | Inference with Hugging Face model |

---

## 📁 Project Directory Structure

``` bash
project/
├── app.py                      # Streamlit web application
├── predictor/
│   ├── __init__.py
│   ├── emotion_model.py       # Loads Hugging Face model and predicts emotions
│   └── stress_mapper.py       # Maps emotion to stress score
├── utils/
│   ├── __init__.py
│   └── mlflow_logger.py       # Utility for logging with MLflow
├── data/
│   └── diary_log.csv          # Stores diary predictions (tracked with DVC)
├── requirements.txt           # Required dependencies
└── README.md                  # Project documentation
```
---
## 🛠 Installation & Run Instructions

### 1. Clone the project and set up the environment
```bash
git clone https://github.zhaw.ch/kafleric/MLOPS_Project.git
cd MLOPS_Project
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Initialize DVC and track the CSV
```bash
dvc init
dvc add data/diary_log.csv
git add data/diary_log.csv.dvc .gitignore
git commit -m "Track diary log with DVC"
```

### 3. Run the Streamlit application
```bash
streamlit run app.py
```

### 4. (Optional) Start MLflow UI
```bash
mlflow ui
```
- Access it via: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🔍 Emotion Detection Method

1. Uses `cardiffnlp/twitter-roberta-base-emotion` from Hugging Face
2. Tokenizes input diary text
3. Returns the predicted emotion label and confidence score

```python
label, score = predict_emotion(text)
# Example: ("disappointment", 0.89)
```

---

## 🔢 Stress Score Calculation

Each emotion is associated with a weight that reflects its stress level. The final stress score is computed as:

```python
stress_score = round(weight * confidence * 10, 2)
```

Example:
| Emotion        | Weight | Confidence | Stress Score |
|----------------|--------|------------|---------------|
| grief          | 1.0    | 0.92       | 9.2           |
| joy            | 0.1    | 0.95       | 0.95          |

---

## 🧾 Data Logging with DVC
- Diary input, emotion label, confidence score, and stress score are saved to `data/diary_log.csv`
- File is tracked with DVC for version control across different experiments

---

## 📊 MLflow Logging
- Each prediction is logged with:
  - `emotion`: predicted label
  - `stress_score`: calculated value

```python
mlflow.log_param("emotion", emotion)
mlflow.log_metric("stress_score", stress)
```

Logs can be visualized on the MLflow dashboard.

---

---

## 📦 Automation with GitHub Actions

This project includes a GitHub Actions workflow to automatically log diary entries and track them using DVC.

### 🚀 Workflow Overview

- Takes a manually entered diary text input
- Runs emotion and stress prediction using the model
- Appends results to `data/diary_log.csv`
- Tracks the CSV with DVC
- Commits and pushes the changes back to GitHub

### 🛠 How to Use

1. Go to the [**Actions tab**](https://github.com/VasavatLim/MLOPS_diary-stress-detector/actions) of this repository.
2. Select the workflow **📘 Log Diary Entry**.
3. Click **"Run workflow"** (top-right).
4. Enter your diary entry (e.g., _"I feel overwhelmed by my workload."_).
5. Click the green **"Run workflow"** button.

After a few seconds, the system will:
- Run inference on your entry
- Log the emotion and stress score to `data/diary_log.csv`
- Version the update using DVC
- Push changes to the repo

### 🧠 Internals

- The workflow is defined in: `.github/workflows/log_diary.yml`
- It uses `PYTHONPATH=.` to support relative imports
- The prediction is handled by: `scripts/log_prediction.py`

### 🔐 Permissions

Make sure your repository has:
- **Actions enabled**
- **Write permissions for GITHUB_TOKEN** under repository settings:
  - Go to **Settings → Actions → General → Workflow permissions**
  - Select **"Read and write permissions"**

---



## 🙋‍♀️ Author
- **Sunghyun Shin, Vasavat Limnanthasin**
- MLOps Final Project — ZHAW School of Engineering
