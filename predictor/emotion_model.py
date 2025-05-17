from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import torch
import numpy as np

MODEL_NAME = "cardiffnlp/twitter-roberta-base-emotion"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
labels = model.config.id2label


def predict_emotion(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    with torch.no_grad():
        logits = model(**inputs).logits
    probs = softmax(logits.numpy()[0])
    idx = np.argmax(probs)
    label = labels[idx]
    score = probs[idx]
    return label.lower(), float(score)
