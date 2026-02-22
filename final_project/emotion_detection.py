import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    if text_to_analyze is None or len(text_to_analyze).strip() ==0:
        return{
                    "anger":None,
                    "disgust":None,
                    "fear":None,
                    "joy":None,
                    "sadness":None,
                    "dominant_emotion": None

    }
        
    payload = { "raw_document": { "text": text_to_analyze} }
    response=requests.post(URL,headers=Headers,json=payload)

    if response.status_code == 400:
        return{

                    "anger":None,
                    "disgust":None,
                    "fear":None,
                    "joy":None,
                    "sadness":None,
                    "dominant_emotion": None

        }

    response_dict=json.loads(response.text)
    emotions=response_dict["emotionPredictions"][0]["emotion"]
    dominant_emotion=max(emotions,key=emotions.get)
    return {
        "anger":emotions["anger"],
        "disgust":emotions["disgust"],
        "fear":emotions["fear"],
        "joy":emotions["joy"],
        "sadness":emotions["sadness"],
        "dominant_emotion": dominant_emotion

    }