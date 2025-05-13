from transformers import pipeline

classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

def predict_emotion(text):
    result = classifier(text)[0]
    emotion = result['label'].lower()
    score = result['score']
    return emotion, score

