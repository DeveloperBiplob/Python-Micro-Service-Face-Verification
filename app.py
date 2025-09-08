# Single image 

from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from deepface import DeepFace
import cv2, numpy as np, json

app = FastAPI()

# Helper to convert uploaded image to OpenCV format
def read_image(file):
    data = np.frombuffer(file, np.uint8)
    img = cv2.imdecode(data, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError("Invalid image file or format.")
    return img

@app.post("/register-face")
async def register_face(user_id: str = Form(...), face: UploadFile = File(...)):
    try:
        print("--------------------------------------hell0")
        img = read_image(await face.read())

        # Generate embedding
        embedding_data = DeepFace.represent(img, model_name="Facenet")
        if not embedding_data:
            return JSONResponse(status_code=400, content={"error": "No face detected in the image."})

        embedding = embedding_data[0]["embedding"]
        return {"status": "success", "embedding": embedding}

    except Exception as e:
        # Return detailed error for Laravel debugging
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.post("/verify-face")
async def verify_face(embedding: str = Form(...), face: UploadFile = File(...)):
    try:
        print("-----------------------------------------------hell0 from verify")
        db_embedding = json.loads(embedding)
        print("mbedding code:------------------------------------------------------", db_embedding)

        img = read_image(await face.read())
        embedding_data = DeepFace.represent(img, model_name="Facenet")
        # print('embedding_data:------------------------------------------------------', embedding_data)
        if not embedding_data:
            return JSONResponse(status_code=400, content={"error": "No face detected in the image."})

        result = embedding_data[0]["embedding"]
        sim = np.dot(result, db_embedding) / (np.linalg.norm(result) * np.linalg.norm(db_embedding))

        return {"verified": sim >= 0.75, "similarity": float(sim)}

    except json.JSONDecodeError:
        return JSONResponse(status_code=400, content={"error": "Invalid embedding format."})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})




# User for Face Embedding then return it on api
@app.post("/face-embedding")
async def register_face(user_id: str = Form(...), face: UploadFile = File(...)):
    try:
        print("--------------------------------------hell0")
        img = read_image(await face.read())

        # Generate embedding
        embedding_data = DeepFace.represent(img, model_name="Facenet")
        if not embedding_data:
            return JSONResponse(status_code=400, content={"error": "No face detected in the image."})

        embedding = embedding_data[0]["embedding"]
        return {"status": "success", "embedding": embedding}

    except Exception as e:
        # Return detailed error for Laravel debugging
        return JSONResponse(status_code=500, content={"error": str(e)})
