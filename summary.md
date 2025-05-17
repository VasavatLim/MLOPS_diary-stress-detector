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
Automatic – runs on every `push` or `pull request` to the `main` branch

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

