import streamlit as st
import numpy as np
import cv2
from tensorflow.keras.models import load_model
import warnings
from PIL import Image

# Ignore TensorFlow warnings
warnings.filterwarnings('ignore', category=UserWarning, module='tensorflow')

# Load pre-trained model
model = load_model('Emotion_model.h5', compile=False)

# Emotion labels
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Set Streamlit config
st.set_page_config(page_title="😊 Emotion Detector", layout="wide")

# Header
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>Facial Emotion Detection App</h1>", unsafe_allow_html=True)
st.markdown("Upload a clear face image to predict the emotion.")

# File uploader
uploaded_file = st.file_uploader("📤 Upload an image", type=['jpg', 'jpeg', 'png'])

# Layout
col1, col2 = st.columns(2)

if uploaded_file is not None:
    with col1:
        st.image(uploaded_file, caption='🖼️ Uploaded Image', use_column_width=True)

    # Image preprocessing
    image = Image.open(uploaded_file).convert('L')
    image = image.resize((48, 48))
    img_array = np.array(image).astype('float32') / 255.0
    img_array = np.expand_dims(img_array, axis=(0, -1))  # Add batch and channel dimensions

    # Make prediction
    prediction = model.predict(img_array)[0]
    predicted_emotion = emotion_labels[np.argmax(prediction)]

    with col2:
        st.markdown(f"### 🎯 Predicted Emotion: **:green[{predicted_emotion}]**")
        st.markdown("### 📊 Emotion Probabilities:")
        emotion_dict = {label: round(float(prob)*100, 2) for label, prob in zip(emotion_labels, prediction)}
        st.bar_chart(emotion_dict)

        # Display progress bars for each emotion
        st.markdown("### 🔍 Emotion Confidence Levels")
        for label, prob in emotion_dict.items():
            st.progress(prob / 100.0, text=f"{label}: {prob}%")

# Footer
st.markdown("---")
st.markdown("<center>Made with ❤️ using Streamlit & TensorFlow</center>", unsafe_allow_html=True)
