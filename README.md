1. pip install -r requirements.txt
2. For Run First run it     => source venv/Scripts/activate
2. Start Server             => uvicorn app:app --host 0.0.0.0 --port 5000 --reload

# Core ASGI + Web Server
fastapi==0.115.0
uvicorn[standard]==0.30.6
gunicorn==23.0.0

# File uploads (required by FastAPI for Form/File)
python-multipart==0.0.9

# DeepFace & dependencies
deepface==0.0.93
retina-face==0.0.15

# TensorFlow & Keras split packages
tensorflow==2.20.0
tf-keras==2.20.0

# Scientific & ML dependencies
numpy==1.26.4
pandas==2.2.2
opencv-python==4.10.0.84
matplotlib==3.9.2

# Optional but useful
scikit-learn==1.5.2
Pillow==10.4.0
