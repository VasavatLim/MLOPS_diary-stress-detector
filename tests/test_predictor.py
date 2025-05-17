from predictor.emotion_model import predict_emotion
from predictor.stress_mapper import map_emotion_to_stress

def test_predict_emotion():
    label, score = predict_emotion("I feel happy")
    assert isinstance(label, str)
    assert 0 <= score <= 1

def test_stress_mapper():
    score = map_emotion_to_stress("joy", 0.9)
    assert 0 <= score <= 10
