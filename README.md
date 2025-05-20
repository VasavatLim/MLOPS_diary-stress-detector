# README.md
# 📘 Stress Detection from Diary Text

## 🧠 Project Overview
This app helps users reflect on their feelings by analyzing diary entries and estimating a stress level based on the predicted emotion. It’s built with Streamlit and designed to be easy to use—just type in a diary entry and get instant emotional insights. MLflow is used for experiment tracking, and prediction logs are saved to CSV and version-controlled with DVC.

---

## 🔧 Tools & Technologies

### 🧪 Tools from MLOps Lab Series

| Tool                        | Purpose |
|-----------------------------|---------|
| **🤗 Transformers**         | RoBERTa-based emotion classification |
| **Streamlit**               | Frontend UI for diary input and feedback  |
| **MLflow**                  | Logs model predictions and metrics  |
| **DVC (Data Version Control)** | Tracks and versions `diary_log.csv`  |
| **GitHub Actions**          | Automates diary logging and CI workflows  |

---

### 🛠 Other Technologies

| Technology                  | Purpose |
|-----------------------------|---------|
| **PyTorch**                 | Backend for running the emotion model |
| **Hugging Face Tokenizer** | Converts text into model-friendly tokens |
| **Pandas**                  | Handles CSV data operations |
| **Pytest**                  | Runs unit tests during CI |
| **Flake8**                  | Enforces Python style and formatting |
| **Git (custom config)**     | Enables safe auto-merge in workflows |

---

## 📁 Project Directory Structure

```bash
MLOPS_diary-stress-detector/
├── app.py                      # Streamlit web application
├── predictor/
│   ├── __init__.py
│   ├── emotion_model.py       # Loads Hugging Face model and predicts emotions
│   └── stress_mapper.py       # Maps emotion to stress score
├── utils/
│   ├── __init__.py
│   └── mlflow_logger.py       # Utility for logging with MLflow
├── scripts/
│   └── log_prediction.py      # Command-line prediction + logging tool
├── tests/
│   ├── test_predictor.py      # Unit tests for predictor functions
│   └── .flake8                # Linting config
├── data/
│   └── diary_log.csv          # Stores diary predictions (tracked with DVC)
├── .github/
│   └── workflows/
│       ├── log_diary.yml      # Manual diary entry workflow
│       └── ci.yml             # CI workflow (pytest + flake8)
├── requirements.txt           # Required dependencies
└── README.md                  # Project documentation
```
---

## 🛠 Installation & Run Instructions

### 1. Clone the project and set up the environment
```bash
git clone https://github.com/VasavatLim/MLOPS_diary-stress-detector.git
cd MLOPS_diary-stress-detector
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

# 🤖 Automation with GitHub Actions

This project includes two key automation workflows using **GitHub Actions**:

- ✅ Logging diary entries automatically from the deployed Streamlit app
- ✅ Maintaining clean, working code through continuous integration (CI)

Together, these make your ML project production-ready, testable, and reproducible.

---

## 📘 1. Log Diary Entry Workflow

### 🔧 What It Does:
- Accepts a diary entry from the deployed **Streamlit app**
- Runs a GitHub Action (`log_diary.yml`) to:
  - Predict emotion and confidence using a pretrained model
  - Calculate a stress score
  - Append the result to `data/diary_log.csv`
  - Track the updated file using **DVC**
  - Commit and push changes to GitHub

### ▶️ How It’s Triggered:
- From **Streamlit**, via GitHub API (`workflow_dispatch`)
- Users write in the app → it calls the GitHub Action automatically

### 🧠 Purpose:
- Replaces the need to run `log_prediction.py` manually
- Ensures predictions are versioned and saved without any local steps

---

## 🧪 2. CI Workflow (Code Testing)

### 🔧 What It Does:
- On every **code push or pull request**, it automatically runs:
  - ✅ `pytest` — to verify unit tests pass
  - ✅ `flake8` — to enforce consistent coding style

### ▶️ How It’s Triggered:
- Automatically on:
  - Every `git push`
  - Every PR to the `main` branch

### 🧠 Purpose:
- Catches bugs early
- Keeps your codebase clean and readable
- Enforces best practices for teamwork and review

---

## 🧩 Summary Table

| Workflow Name        | Trigger Source           | Actions Performed                                  |
|----------------------|---------------------------|----------------------------------------------------|
| 📘 Log Diary Entry    | Streamlit app API call     | Logs diary input → predicts → tracks with DVC      |
| 🧪 CI Workflow        | Git push / Pull Request    | Runs tests and lint checks on new code             |

---

## ✅ Benefits of Using GitHub Actions

- 🔁 **Automation**: No need to run local scripts
- 🔍 **Reliability**: Your code is tested every time it's changed
- 🧠 **Reproducibility**: All logs and model outputs are version-controlled
- 🚀 **Deployability**: Seamlessly integrates with cloud apps like Streamlit

---

## 🔗 Workflow Files

- `.github/workflows/log_diary.yml`: Diary logging automation (includes safe Git pull + merge strategy)
- `.github/workflows/ci.yml`: Continuous integration for test & lint


---



## 🙋‍♀️ Author
- **Sunghyun Shin, Vasavat Limnanthasin**
- MLOps Final Project — ZHAW School of Engineering
