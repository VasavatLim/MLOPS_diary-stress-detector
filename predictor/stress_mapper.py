stress_weight = {
    "joy": 0.1,
    "love": 0.2,
    "admiration": 0.2,
    "neutral": 0.5,
    "surprise": 0.5,
    "fear": 0.8,
    "sadness": 0.85,
    "disappointment": 0.9,
    "anger": 0.95,
    "grief": 1.0,
    "nervousness": 0.8
}

def map_emotion_to_stress(emotion, score):
    weight = stress_weight.get(emotion.lower(), 0.5)
    return round(weight * score * 10, 2)
