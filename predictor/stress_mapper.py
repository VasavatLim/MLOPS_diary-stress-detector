stress_weight = {
    "joy": 0.1,
    "love": 0.2,
    "admiration": 0.2,
    "amusement": 0.2,
    "approval": 0.3,
    "caring": 0.4,
    "gratitude": 0.2,
    "optimism": 0.2,
    "excitement": 0.3,
    "pride": 0.3,
    "relief": 0.3,
    "curiosity": 0.4,
    "desire": 0.4,
    "realization": 0.4,

    "neutral": 0.5,
    "confusion": 0.6,
    "remorse": 0.7,
    "annoyance": 0.75,
    "disappointment": 0.8,
    "nervousness": 0.8,
    "fear": 0.85,
    "sadness": 0.85,
    "disapproval": 0.9,
    "anger": 0.95,
    "grief": 1.0,
    "disgust": 1.0,
    "embarrassment": 0.9
}


def map_emotion_to_stress(emotion, score):
    weight = stress_weight.get(emotion.lower(), 0.5)
    return round(weight * score * 10, 2)
