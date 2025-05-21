# README.md
# 📘 Stress Detection from Diary Text

## 🧠 Project Overview
This app is designed to help users better understand their emotions by analyzing what they write in a diary. Just open the app, type in how you're feeling, and it will instantly predict your emotional state and give you a stress score. Behind the scenes, it uses Streamlit for the interface, MLflow to keep track of predictions, and DVC to version-control the logs, keeping everything organized and reproducible.

## 📁 Project Directory Structure

```bash
MLOPS_diary-stress-detector/
├── app.py                      # Streamlit web application
├── predictor/
│   ├── __init__.py
│   ├── emotion_model.py        # Loads Hugging Face model and predicts emotions
│   └── stress_mapper.py        # Maps emotion to stress score
├── utils/
│   ├── __init__.py
│   └── mlflow_logger.py        # Utility for logging with MLflow
├── scripts/
│   └── log_prediction.py       # Command-line prediction + logging tool
├── tests/
│   ├── test_predictor.py       # Unit tests for predictor functions
│   └── .flake8                 # Linting config
├── data/
│   └── diary_log.csv           # Stores diary predictions (tracked with DVC)
├── .github/
│   └── workflows/
│       ├── log_diary.yml       # Manual diary entry workflow
│       └── ci.yml              # CI workflow (pytest + flake8)
├── requirements.txt            # Required dependencies
└── README.md                   # Project documentation
```

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

## 🛠 Installation & Run Instructions

### 1. Clone the project and set up the environment
```bash
git clone https://github.com/VasavatLim/MLOPS_diary-stress-detector.git
cd MLOPS_diary-stress-detector
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### ⚠️ Important: If You Cloned the Repository

If you cloned this repository, the `data/diary_log.csv` file is tracked using DVC and not stored in Git. You must either:

1. **Download the file manually** from our shared DVC storage:
   [📂 Google Drive – diary_log.csv](https://drive.google.com/drive/folders/1NMWlYDQV13rYirQiksOY8ufe57Uoj33F?usp=sharing)
   
   Then, place it in the `data/` directory:

   ```bash
   mv ~/Downloads/diary_log.csv data/diary_log.csv


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

This workflow automatically handles diary entries submitted from the **Streamlit app**, turning them into structured, versioned logs.

### 🛠 How It Works – Step by Step

**1. User submits a diary entry in the app**  
They write their thoughts in the Streamlit interface and hit submit.

**2. The app triggers a GitHub Action**  
Using the GitHub API (`workflow_dispatch`), the app starts the `log_diary.yml` workflow.

**3. The GitHub Action processes the entry**  
It runs the emotion prediction model, calculates the stress score, and appends the result to `data/diary_log.csv`.

**4. DVC tracks the updated log**  
The changed CSV is versioned using **DVC**, so you can reproduce or roll back experiments later.

**5. Changes are committed and pushed**  
The updated log file is automatically committed and pushed back to the GitHub repository—no manual steps required.

### 🎯 Why This Matters

- You don’t need to run `log_prediction.py` or update the CSV manually  
- All predictions are version-controlled, tracked, and reproducible  
- It makes the logging process feel invisible to the user—but fully automated for the team


---

## 🧪 2. CI Workflow (Code Testing)

This workflow helps keep the project clean, functional, and reliable by testing and linting the code automatically.

### 🛠 How It Works – Step by Step

**1. You push code or open a pull request**  
Any time you make changes and push to the repo (or open a PR to `main`), the workflow kicks in.

**2. GitHub Actions runs checks automatically**  
It runs two important tools to keep the codebase healthy:
- ✅ `pytest` — runs all unit tests to make sure nothing is broken
- ✅ `flake8` — checks for formatting and style issues

**3. Get immediate feedback**  
If something fails, GitHub will let you know exactly where and why—so you can fix it right away.

### 🎯 Why This Matters

- Helps you catch bugs before they make it into `main`  
- Keeps code consistent and easy for others to read  
- Encourages best practices and makes collaboration smoother

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
