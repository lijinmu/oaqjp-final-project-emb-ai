"""Flask app for detecting emotions from user input via an HTTP endpoint."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """Endpoint to analyze emotions from input text."""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response

    response = emotion_detector(text_to_analyze)
    status_code = response[0].status_code
    formatted_response = response[1]
    print(formatted_response)
    # Extract the labels and result from the response

    if status_code == 200:

        emotions = formatted_response['emotionPredictions'][0]['emotionMentions'][0]['emotion']
        if emotions:
            anger_score = emotions['anger']
            disgust_score = emotions['anger']
            fear_score = emotions['anger']
            joy_score = emotions['anger']
            sadness_score = emotions['anger']
            emotions = {
                "anger": anger_score,
                "disgust": disgust_score,
                "fear": fear_score,
                "joy": joy_score,
                "sadness": sadness_score
            }
            max_emotion = max(emotions, key=emotions.get)
            if max_emotion is None:
                text =  "Invalid text! Please try again!"
            else:
                text = (
                    f"For the given statement, the system response is {emotions}. "
                    f"The dominant emotion is {max_emotion}."
                )
            return { text }
    # If the response status code is 500, set label and score to None
    elif status_code == 400:
        return { "Invalid text! Please try again!" }

    else:
        return { "Invalid text! Please try again!" }

@app.route("/")
def render_index_page():
    """render html page"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
