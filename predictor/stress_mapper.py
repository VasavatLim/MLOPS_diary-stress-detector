emotion_to_stress = {
    "joy": 1,
    "love": 2,
    "surprise": 3,
    "neutral": 4,
    "sadness": 7,
    "fear": 8,
    "anger": 9
}

def map_emotion_to_stress(emotion):
    return emotion_to_stress.get(emotion, 5)