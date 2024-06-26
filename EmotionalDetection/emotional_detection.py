import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myjson = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
    response = requests.post(URL, json = myjson, headers = header)
    formatted_response = json.loads(response.text) #json

    if response.status_code == 400 or response.status_code == 500: #if blank
        formatted_emotions = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            }
        return formatted_emotions
    else: #if we can perform sentiment analysis
        emotions = formatted_response["emotionPredictions"][0]["emotion"]
        max_emotion = max(emotions, key=emotions.get)
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']

        formatted_emotions = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': max_emotion
            }
        return formatted_emotions
