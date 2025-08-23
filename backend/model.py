# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-classification", model="jy46604790/Fake-News-Bert-Detect")
classifier = pipe

# Map model's label to readable string
label_map = {
    "LABEL_0" : "FAKE", "LABEL_1" : "REAL"
}

# Function that predicts the label and score for a given text
def predict(text):
    result = classifier(text)[0]
    return{
        "label": result['label'],
        "score": result['score']
    }