"""
This file uses Flask to run the emotion detection web application.

Defines the routes for the main page and the emotion detection function.

Formats results.

"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

#Defines the main route
@app.route("/")
def render_index_page():

    """
    Renders the index page of the emotion detection web application.

    Loads the HTML template page.

    """

    return render_template('index.html')

#Defines the route for the emotion detector
@app.route("/emotionDetector")
def run_sentiment_analysis():

    """
    Processes the user's text input and calls the function to analyze the text.

    Returns the formatted emotion detection results.

    """

    text_to_analyze = request.args.get('textToAnalyze')

    #Gets the emotion analysis from calling the emotion detector function
    response = emotion_detector(text_to_analyze)

    #Produces an error response if no text is entered
    if response['dominant_emotion'] is None:
        return "Invalid text!  Please try again"

    #Extracts the emotion names and score numbers from the function response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    #Returns the formatted string results
    return (
        f"For the given statement, the system response is: <br> 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, <br>'joy: {joy}, and 'sadness': {sadness}."
        f"<br>The dominant emotion is <b>{dominant_emotion}</b>." 
    )

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
