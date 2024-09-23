from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template('index.html')


@app.route("/emotionDetector")
def RunSentimentAnalysis():
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text!  Please try again"
        
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    
    return (
        f"For the given statement, the system response is: <br> 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, <br>'joy: {joy}, and 'sadness': {sadness}."
        f"<br>The dominant emotion is <b>{dominant_emotion}</b>." 
    )

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
