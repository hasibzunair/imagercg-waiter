"""Image classification API server code"""
import os
from fastapi import FastAPI, File, UploadFile
import uvicorn
from predictor import read_image, preprocess, get_prediction_model, predict

# USAGE:
# curl -X POST -F image=@test.jpeg "http://127.0.0.1:8000/api/predict"

# Get classes list
if not os.path.exists("./imagenet_classes.txt"):
    os.system("wget https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt")

app = FastAPI(title="Image Classification API", description="API for image classification using deep learning.", version="1.0")
model = None

@app.on_event("startup")
def model():
    global model
    # Load model once
    model = get_prediction_model()

@app.get("/")
def read_root():
    return {"hello": "world"}

@app.post("/api/predict")
async def predict_image(image: bytes = File(...)):
    # Read image
    image = read_image(image)
    # Preprocess image
    image = preprocess(image)
    # Predict
    predictions = predict(image, model)
    print(predictions)
    return predictions

if __name__ == "__main__":
    uvicorn.run(app, debug=True)
    print("Running server.")
    # See 127.0.0.1:8000/docs for more info.
    # ENDPOINT_URL is http://127.0.0.1:8000/api/predict