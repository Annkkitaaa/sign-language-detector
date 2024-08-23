from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import cv2
import numpy as np
import pickle
import mediapipe as mp

app = Flask(__name__)
CORS(app)

# Load your model and set up MediaPipe
model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

labels_dict = {0: 'Hello', 1: 'Yes', 2: 'I love you', 3: 'No'}

@app.route('/detect', methods=['POST'])
def detect_gesture():
    # Get the image data from the request
    image_data = request.json['image']
    
    # Decode the base64 image
    image_data = base64.b64decode(image_data.split(',')[1])
    image = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)
    
    # Convert to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Process the image
    results = hands.process(image_rgb)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            data_aux = []
            x_ = []
            y_ = []
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                x_.append(x)
                y_.append(y)
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.append(x - min(x_))
                data_aux.append(y - min(y_))
            
            prediction = model.predict([np.asarray(data_aux)])
            predicted_character = labels_dict[int(prediction[0])]
            
            return jsonify({'gesture': predicted_character})
    
    return jsonify({'gesture': 'No hand detected'})

if __name__ == '__main__':
    app.run(debug=True)