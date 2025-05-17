# 🔄 Workflow Automation in Stress Detection System

This document explains the two GitHub Actions workflows used in this project and compares the benefits of using automated workflows (CI/CD) versus managing everything manually.

---

## 📘 1. Log Diary Entry Workflow

### 🔧 Purpose:
To automate the process of logging new diary entries, predicting the user's emotion and stress level, and storing the result in a version-controlled CSV file.

### ⚙️ What It Does:
- Takes a diary text input from the GitHub UI
- Uses the trained model to predict emotion and confidence
- Calculates the stress score based on the emotion
- Appends the result to `data/diary_log.csv`
- Tracks the CSV with DVC
- Commits and pushes the updates to GitHub

### 🧠 Why It's Useful:
- Consistent and structured logging
- Enables team members to contribute entries easily
- Ensures all logs are versioned with DVC
- No need to run Python scripts locally

### 📎 Trigger:
Manual – triggered via GitHub UI using **"Run workflow"**

---

## 🧪 2. CI Workflow (Continuous Integration)

### 🔧 Purpose:
To ensure that the codebase is clean, tested, and working properly every time a developer pushes changes.

### ⚙️ What It Does:
- Runs unit tests using `pytest` (e.g. for `predict_emotion()` and `map_emotion_to_stress()`)
- Checks code formatting with `flake8`
- Can be extended to validate data, DVC status, etc.

### 🧠 Why It's Useful:
- Catches bugs early during development
- Prevents broken code from reaching production
- Enforces code quality and testing practices
- Builds trust when working as a team

### 📎 Trigger:
- ✅ From the deployed **Streamlit app**, using the GitHub API (`workflow_dispatch`)
- 🧑‍💻 Also supports manual execution via GitHub UI if needed


---

## 🔍 With vs. Without Workflows

| Feature                        | ✅ With Workflows                          | ❌ Without Workflows                      |
|-------------------------------|--------------------------------------------|-------------------------------------------|
| Diary entry logging           | Automatic via GitHub Actions               | Manually run script locally               |
| Version control of logs       | DVC auto-tracked in workflow               | Easy to forget DVC commands               |
| Unit tests on every push      | ✅ Always checked                          | ❌ Must remember to run manually          |
| Code quality enforcement      | ✅ Checked by flake8                       | ❌ Not enforced                           |
| Team collaboration            | ✅ Reliable, testable contributions        | ❌ Risk of breaking codebase              |
| Deployment (Streamlit)        | Optional: auto-deploy on `main` push       | Must manually redeploy                   |
| Reproducibility               | High – consistent workflow                 | Lower – depends on individual discipline  |
| Professionalism               | ✅ MLOps-ready pipeline                    | ❌ Solo/hobby project feel                |

---

## 🏁 Summary

Using GitHub Actions for CI and diary logging has transformed this project from a simple ML app into a **reproducible, testable, and team-ready MLOps workflow**.

Both workflows are visible under the **Actions** tab in the GitHub repository:
- `📘 Log Diary Entry`
- `🧪 Run CI Checks`

Together, they support automation, accountability, and reliability in every part of the ML system lifecycle.

---

# 🧰 Tool Summary

This project integrates a set of powerful tools for machine learning, web deployment, experiment tracking, data versioning, testing, and automation. Below is a breakdown of each tool and its role in the system.

---

## 🧠 Machine Learning

| Tool                        | Purpose |
|-----------------------------|---------|
| **Hugging Face Transformers** | Loads a pretrained RoBERTa model for emotion classification |
| **Hugging Face Tokenizer** | Tokenizes diary text into input format for the model |
| **Torch (PyTorch)**         | Runs the model inference under the hood |
| **Numpy** *(implicit)*      | Handles array operations used in inference/calculations |

---

## 📊 Data Handling

| Tool        | Purpose |
|-------------|---------|
| **Pandas**  | Reads and writes diary logs to `data/diary_log.csv` |
| **CSV File**| Serves as the local storage for all diary log entries |

---

## 🧾 Experiment Tracking & Reproducibility

| Tool            | Purpose |
|------------------|---------|
| **MLflow**       | Logs each prediction’s emotion and stress score |
| **DVC (Data Version Control)** | Tracks changes to `diary_log.csv` and enables reproducibility across runs |

---

## 🌐 Web Application

| Tool        | Purpose |
|-------------|---------|
| **Streamlit** | Provides an interactive UI for users to submit diary entries and view emotion/stress feedback visually |

---

## 🧪 Testing & Code Quality

| Tool        | Purpose |
|-------------|---------|
| **Pytest**  | Runs unit tests on prediction and mapping functions |
| **Flake8**  | Linting tool to enforce clean, consistent Python code |

---

## 🤖 Automation & CI/CD

| Tool            | Purpose |
|------------------|---------|
| **GitHub Actions** | Automates:
- 📘 Diary logging via `log_diary.yml` (includes safe git merge config to avoid push conflicts)
- 🧪 Code testing + linting via `ci.yml` (runs on every push or PR) |

| **GITHUB_TOKEN** *(built-in)* | Used to push changes to the repo securely within workflows |

---

## ✅ Summary

This toolchain supports:
- Robust ML inference with traceability (Transformers, MLflow, DVC)
- Reliable web-based input/output (Streamlit)
- Automated code validation (Pytest, Flake8, GitHub Actions)
- Clean and reproducible workflow for long-term MLOps projects

Each tool was chosen to serve a specific function in a lightweight but professional MLOps setup.

---
