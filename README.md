# face_emotion_detection_cnn
Here is a **fresh, modern, and more visually appealing** version of your README file for the Face Emotion Detection project. It focuses on **clarity**, **design structure**, and **developer appeal**, with polished language, improved formatting, and icons for engagement.

---

# 😊 Facial Emotion Detection using Deep Learning

### 🔍 Recognizing Emotions from Facial Expressions with Custom CNN & Real-time Web Deployment

---

## 📌 Overview

This project demonstrates a custom-built Convolutional Neural Network (CNN) that detects and classifies human emotions from facial images into **seven categories**:

> **😠 Angry | 😖 Disgust | 😨 Fear | 😀 Happy | 😢 Sad | 😲 Surprise | 😐 Neutral**

Trained on grayscale facial images, the model achieves:

* ✅ **\~70% Validation Accuracy**
* ✅ **\~67% Training Accuracy**

The final model is deployed via a **Flask-based web application** for easy and interactive use.

---

## 🧠 Core Features

* 🧱 Custom CNN architecture built from scratch
* 🖼️ Input: 48x48 grayscale facial images
* 🔄 Real-time prediction via image upload
* 🧪 Model tested and validated using best practices
* 💻 User-friendly web interface built with Flask and HTML/CSS

---

## 🚀 Live Prediction Flow

1. User uploads a face image.
2. Image is resized & preprocessed (48x48, grayscale).
3. Image passed to trained CNN model.
4. Model returns most probable emotion.
5. Web app displays image and prediction result.

---

## 🧱 Project Structure

```
Emotion-Detection/
│
├── main.py                      #  Streamlit backend (Web App)
├── Emotion_model.h5           # Trained CNN model            
├── static/
│   └── face image.jpg     # Temporary uploaded image
├── Emotion_Detection.ipynb  # Notebook for model training
├── README.md                  # Project documentation
```

---

## 🏗️ CNN Model Architecture

* **Layers**: Conv2D → MaxPooling2D → BatchNorm → Dropout → Dense
* **Optimizer**: Adam
* **Loss Function**: Categorical Crossentropy
* **Final Layer**: Softmax for 7-class emotion output
* **Regularization**: Dropout + Data Augmentation

📉 *Refer to the notebook for training metrics and architecture details.*

---

## 📊 Model Performance

| Metric           | Value                   |
| ---------------- | ----------------------- |
| Accuracy         | \~65% (val)             |
| Loss             | ↓ Converged             |
| Confusion Matrix | ✔️ Included in notebook |
| Augmentation     | ✔️ Flip, Zoom, Rotation |

---

## 🧪 Technologies Used

| Category             | Tools / Libraries          |
| -------------------- | -------------------------- |
| 💻 Programming       | Python                     |
| 🧠 Deep Learning     | TensorFlow, Keras          |
| 🖼️ Image Processing | OpenCV, Pillow             |
| 🌐 Web Framework     | Streamlit|
| 📊 Data/Plotting     | NumPy, Matplotlib, Seaborn |

---

## 💡 Real-World Use Cases

* 🎭 Emotion-aware Human-Computer Interfaces
* 🧠 Mental Health Monitoring & Therapy Apps
* 📊 Social Media Sentiment Analysis
* 📞 Emotion-driven Customer Support Systems
* 🚗 Driver Alertness Detection Systems

---

## 📷 Sample Emotions Detected

| Emotion  | Emoji |
| -------- | ----- |
| Angry    | 😠    |
| Disgust  | 😖    |
| Fear     | 😨    |
| Happy    | 😀    |
| Sad      | 😢    |
| Surprise | 😲    |
| Neutral  | 😐    |

---

## 🛠️ How to Run Locally

1. ✅ Clone this repo:

   ```bash
   git clone https://github.com/your-username/Emotion-Detection.git
   cd Emotion-Detection
   ```

2. 🔧 Install dependencies:

   ```bash
   pip install streamlit tensorflow numpy opencv-python pillow
   ```

3. 🚀 Launch the web app:

   ```bash
   python main.py
   ```

**Emotion Detection

https://github.com/user-attachments/assets/c205c3b6-3ba2-4572-9915-51caec6c5dfa


