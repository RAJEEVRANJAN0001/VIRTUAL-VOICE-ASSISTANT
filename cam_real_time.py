
#cam_real_time.py

import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load pre-trained face cascade classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load your pre-trained model
model = load_model('/Users/rajeevranjanpratapsingh/PycharmProjects/voise_assistent/trained_modal".h5"file/emotion_model_final_2.h5')  # path of trained model


# Function to capture video from webcam
def start_webcam():
    video = cv2.VideoCapture(0)  # 0 indicates the default camera (you can change it if necessary)
    return video


# Function to update emotion percentages on the video frame with different colors
def update_emotion_percentage(frame, emotion_counts, total_faces):
    # Define colors for each emotion
    emotion_text_colors = {
        'Angry': (0, 0, 255),  # Red
        'Disgust': (0, 255, 0),  # Green
        'Fear': (255, 255, 0),  # Yellow
        'Happy': (255, 0, 0),  # Blue
        'Sad': (128, 0, 128),  # Purple
        'Surprise': (0, 165, 255),  # Orange
        'Neutral': (255, 255, 255)  # White
    }

    # Calculate emotion percentages
    percentages = {emotion: count / total_faces * 100 if total_faces != 0 else 0 for emotion, count in
                   emotion_counts.items()}

    # Display percentages on the frame with different colors
    y_offset = 20
    for emotion, percentage in percentages.items():
        text_color = emotion_text_colors[emotion]
        cv2.putText(frame, f'{emotion}: {percentage:.1f}%', (10, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.6, text_color,
                    2)
        y_offset += 20


# Start the webcam
video = start_webcam()

while True:
    # Capture video frame
    ret, frame = video.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Face detection using Haar Cascade
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Initialize counters for each emotion
    emotion_counts = {emotion: 0 for emotion in ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']}

    for (x, y, w, h) in faces:
        roi_color = frame[y:y + h, x:x + w]

        # Preprocess frame for CNN input
        resized_frame = cv2.resize(roi_color, (48, 48))
        gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
        normalized_frame = gray_frame / 255.0
        input_data = np.expand_dims(np.expand_dims(normalized_frame, axis=-1), axis=0)

        # Make predictions using the trained CNN model
        prediction = model.predict(input_data)

        # Update emotion counts
        emotion_label = np.argmax(prediction)
        emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
        predicted_emotion = emotion_labels[emotion_label]
        emotion_counts[predicted_emotion] += 1

        # Display the predicted emotion and draw a colored rectangle
        rectangle_color = (255, 255, 255)  # White
        cv2.putText(frame, predicted_emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, rectangle_color, 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), rectangle_color, 2)

    # Update and display emotion percentages on the video frame
    update_emotion_percentage(frame, emotion_counts, len(faces))
    cv2.imshow('Emotion Recognition', frame)

    if cv2.waitKey(1) == 27:  # Press 'Esc' key to exit the loop
        break

# Release the webcam and close OpenCV windows
video.release()
cv2.destroyAllWindows()
