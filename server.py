"""
This module provides a Flask web application for detecting emotions in text.
It includes routes for analyzing text and rendering the index page.
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("emotion_detector")

@app.route("/emotion_detector")
def sent_detector():
    """
    Analyze the text provided by the user and return the emotions detected.
    
    Returns:
        dict: A dictionary with the detected emotions and their scores.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    # Check if the status code is 400 or the dominant emotion is None
    if response['status_code'] == 400 or response['dominant_emotion'] is None:
        return jsonify({
            'message': 'Invalid text! Please try again.'
        })

    return jsonify({
        'anger': response['anger'],
        'disgust': response['disgust'],
        'fear': response['fear'],
        'joy': response['joy'],
        'sadness': response['sadness'],
        'dominant_emotion': response['dominant_emotion']
    })

@app.route("/")
def render_index_page():
    """
    Render the index page for the emotion detector application.
    
    Returns:
        template: The index.html template for the application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
