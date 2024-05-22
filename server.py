from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route ("/emotionDetector")
def emotion_detect():
    text_to_detect = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_detect)

    list_emotions = []
    x = response.pop('dominant_emotion')
    for emotion, value in response.items():
        list_emotions.append(f'"{emotion}" : {value}')
    return ("For the given statement, the system response is: " + ", ".join(list_emotions) + ". The dominant emotion is " + x + ".")

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
