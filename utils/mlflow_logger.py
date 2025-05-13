import mlflow

def log_prediction(emotion, stress_score):
    mlflow.set_experiment("stress-detector")
    with mlflow.start_run():
        mlflow.log_param("emotion", emotion)
        mlflow.log_metric("stress_score", stress_score)