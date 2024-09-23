from flask import Flask, render_template, request
from EmotionDetection.emotion-detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def RunSentimentAnalysis():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    return "For the given statement, the system response is \'anger\':", anger, "\'disgust\':", disgust, "\'fear\':", fear, "\'joy\':", joy, "and \'sadness\':", sadness, ".  The dominant emotion is", dominant_emotion, "." 

if __name__ = "__main__":
    app.run(localhost:5000)