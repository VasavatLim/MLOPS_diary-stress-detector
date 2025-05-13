# Stress Detection from Diary Text

This project detects emotional content from diary entries using a pretrained Hugging Face model, maps the emotion to a stress score, and displays the result through a Streamlit web interface. MLflow is used to log experiment results.

## Run Instructions
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

4. (Optional) View MLflow dashboard:
   ```bash
   mlflow ui
   ```

---
Feel free to modify the emotion-to-stress mapping in `predictor/stress_mapper.py`.
