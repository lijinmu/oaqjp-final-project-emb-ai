import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the sentiment analysis service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    formatted_response = json.loads(response.text)
    print(formatted_response)

    return {response, formatted_response}
    
    status_code = response.status_code
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
        max_value = emotions[max_emotion]
        return {'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': max_emotion
            }
    else:
        emptyResponse = {
            "anger": "none", 
            "disgust": "none", 
            "fear": "none", 
            "joy": "none", 
            "sadness": "none", 
            "dominant_emotion":"none"
            }
        return emptyResponse

