"""Import libraries"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route ("/emotionDetector")
def emotion_detect():
    """
    This method outputs the sentiment analysis for a user's sentence given an input.
    """
    text_to_detect = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_detect)

    list_emotions = [] #creating a list for the emotions
    x = response.pop('dominant_emotion') #dominant emotion value

    if x is None: #x is the dominant emotion value I found above
        return "Invalid text! Please try again!"
    for emotion, value in response.items():
        list_emotions.append(f'"{emotion}" : {value}')
    return "For the given statement, the system response is: " + \
            ", ".join(list_emotions) + ". The dominant emotion is " + \
            x + "."

@app.route("/")
def render_index_page():
    """
    This method renders the HTML file to display our web app
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
