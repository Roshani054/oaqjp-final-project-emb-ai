from flask import Flask,request,jsonify
from final_project.emotion_detection import emotion_detector

app=Flask(__name__)

@app.route('/emotionDetector', methods = ['POST'])
def emotionDetector():
    data=request.get_json()
    text=data.get("text", "")

    emotions=emotion_detector(text)
    if emotions["dominant_emotion"] is None:
        return "Invalid text! Please try again! "
    return jsonify(emotions)

if __name__="__main__":
    app.run(host="0.0.0.0",port=5000)