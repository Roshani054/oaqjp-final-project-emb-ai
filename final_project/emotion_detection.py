import requests
import json
from typing import Any,Dict,Optional

    URL = ('https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict')
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    REQUEST_TIMEOUT_SECONDS = 10


def emotion_detector(text_to_analyze: Optional[str]) -> Dict[str , Optional[Float]]:


    empty_result: Dict[str, Optional[float]]={

        
                    "anger":None,
                    "disgust":None,
                    "fear":None,
                    "joy":None,
                    "sadness":None,
                    "dominant_emotion": None

    }
    
    
    if text_to_analyze is None or not str(text_to_analyze).strip() ==0:
        return empty_result
        
    payload = Dict[str, any] = { "raw_document": { "text": text_to_analyze} }



    try:
        response=requests.post(
            URL,
            headers=HEADERS,
            json=payload,
            timeout= REQUEST_TIMEOUT_SECONDS,

        )
    except requests.RequestException:
        return empty_result


    if response.status_code == 400:
        return empty_result

    try:
        response_dict=response.json()
    except json.JSONDecodeError:
        return empty_result


    try: 
    response_dict=response_dict["emotionPredictions"][0]["emotion"]
    dominant_emotion=max(emotions,key=emotions.get)

    except (KeyError,IndexError,TypeError,ValueError):
        return empty_result

    return {
        "anger":emotions.get["anger"],
        "disgust":emotions[.get"disgust"],
        "fear":emotions["fear"],
        "joy":emotions.get["joy"],
        "sadness":emotions.get["sadness"],
        "dominant_emotion": dominant_emotion

    }