# 🛡️ VisionGuard
### AI-Powered Medicine Package Tampering Detection using Deep Learning

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?style=for-the-badge&logo=tensorflow)
![Flask](https://img.shields.io/badge/Flask-Web_App-black?style=for-the-badge&logo=flask)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 📌 Project Overview

VisionGuard is an AI-powered web application developed to detect whether a medicine package is **Intact** or **Damaged** using Deep Learning.

The system uses a Convolutional Neural Network (CNN) trained on medicine package images and provides instant predictions with confidence scores through a simple Flask web application.

This project aims to improve medicine safety by assisting pharmacies, manufacturers, warehouses, and consumers in identifying damaged medicine packages before use.

---

## 🎯 Objectives

- Detect damaged medicine packages automatically.
- Reduce the risk of distributing damaged medicines.
- Improve medicine quality inspection.
- Provide fast and reliable AI-based predictions.
- Demonstrate the practical application of Computer Vision in healthcare.

---

## 🚀 Features

✅ Upload medicine package images

✅ AI-based damage detection

✅ Confidence score display

✅ Attractive Flask web interface

✅ Real-time prediction

✅ Deep Learning (CNN)

---

## 🧠 Technologies Used

- Python
- TensorFlow
- Keras
- Flask
- HTML
- CSS
- NumPy

---

## 📂 Project Structure

```
VisionGuard/
│
├── dataset/
│   └── train/
│       ├── damaged/
│       └── intact/
│
├── model/
│   └── medicine_model.keras
│
├── static/
│   ├── css/
│   ├── uploads/
│   └── results/
│
├── templates/
│   └── index.html
│
├── app.py
├── predict.py
├── train_model.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/Monika181530/VisionGuard-AI.git
```

Go to the project folder

```bash
cd VisionGuard-AI
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

Install required packages

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Flask server

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## 🧠 Model Details

Model Type:
- Convolutional Neural Network (CNN)

Input Image Size:
- 224 × 224 pixels

Output Classes:
- Damaged
- Intact

Loss Function:
- Binary Crossentropy

Optimizer:
- Adam

Framework:
- TensorFlow / Keras

---

## 📊 Workflow

```
Upload Image
       │
       ▼
Image Preprocessing
       │
       ▼
CNN Model Prediction
       │
       ▼
Confidence Score
       │
       ▼
Damaged / Intact Result
```

---

## 📸 Application Screenshots

### Home Page

(Add screenshot here)

---

### Prediction Result

(Add screenshot here)

---

### Confidence Score

(Add screenshot here)

---

## 💡 Future Enhancements

- Mobile Application
- Live Camera Detection
- QR Code Verification
- Batch Image Processing
- Multi-class Damage Detection
- Cloud Deployment
- IoT Integration

---

## 👩‍💻 Author

**Monika**

GitHub:
https://github.com/Monika181530

Project:
VisionGuard – AI-Powered Medicine Package Tampering Detection

---

## 📜 License

This project is developed for educational and academic purposes.

---

## ⭐ If you found this project useful, consider giving it a Star on GitHub!git add README.md