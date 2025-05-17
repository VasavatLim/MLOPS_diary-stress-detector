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
| **Torch**                   | Runs the pretrained emotion model |
| **Streamlit**               | Web interface for diary input and visual feedback |
| **Pandas**                  | CSV handling and manipulation |
| **MLflow**                  | Logs predictions and metrics for tracking |
| **DVC (Data Version Control)** | Tracks `diary_log.csv` across experiments |
| **GitHub Actions**          | Automates diary logging and CI testing workflows |
| **Pytest**                  | Runs automated unit tests in CI |
| **Flake8**                  | Enforces Python code formatting and style |

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
│   └── test_predictor.py      # Unit tests for predictor functions
├── data/
│   └── diary_log.csv          # Stores diary predictions (tracked with DVC)
├── .github/
│   └── workflows/
│       ├── log_diary.yml      # Manual diary entry workflow
│       └── ci.yml             # CI workflow (pytest + flake8)
├── requirements.txt           # Required dependencies
├── .flake8                    # Linting config
└── README.md                  # Project documentation
```s
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

# 🤖 Automation Summary

This project integrates two key automation workflows using **GitHub Actions** to streamline logging and maintain code quality. These workflows ensure the system remains reliable, testable, and maintainable.

---

## 📘 Log Diary Entry Workflow

### 🔧 What It Does:
- Accepts a diary entry from the GitHub interface
- Predicts the emotion and confidence using a pretrained model
- Calculates a stress score based on the predicted emotion
- Appends the result to `data/diary_log.csv`
- Tracks the updated log using **DVC**
- Commits and pushes the changes back to the repository

### ▶️ Trigger:
- **Manual** (Run from GitHub Actions tab)

### 🧠 Purpose:
Automate the full diary logging process without requiring local script execution.

---

## 🧪 CI Workflow (Continuous Integration)

### 🔧 What It Does:
- Runs **unit tests** (`pytest`) to verify the model logic works as expected
- Runs **code linting** (`flake8`) to ensure consistent formatting and style

### ▶️ Trigger:
- **Automatic** (On every push or pull request to `main`)

### 🧠 Purpose:
Catch bugs early, enforce good code style, and maintain a healthy codebase for collaboration.

---

## ✅ Benefits of Automation

- Saves time by automating manual tasks
- Ensures code correctness and consistency
- Reduces human error during development
- Makes the project more reproducible and professional

---

## 📎 Summary

| Workflow Name       | Trigger         | Main Function                             |
|---------------------|------------------|--------------------------------------------|
| 📘 Log Diary Entry   | Manual (GitHub UI) | Logs new diary entry with emotion & stress |
| 🧪 CI Workflow       | On push / PR      | Tests code + checks formatting             |

These two workflows form the backbone of the project's automation, combining reproducibility with reliable development practices.


---



## 🙋‍♀️ Author
- **Sunghyun Shin, Vasavat Limnanthasin**
- MLOps Final Project — ZHAW School of Engineering
