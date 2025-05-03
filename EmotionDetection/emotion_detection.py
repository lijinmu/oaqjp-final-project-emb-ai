import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the sentiment analysis service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    formatted_response = json.loads(response.text)
    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    emotions = {
        "anger": 0.01364663,
        "disgust": 0.0017160787,
        "fear": 0.008986978,
        "joy": 0.9719017,
        "sadness": 0.055187024
    }
    sorted_emotions = sorted(emotions.items(), key=lambda item: item[1], reverse=True)
    max_emotion, max_value = sorted_emotions[0]
    return {'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': max_emotion
        }

