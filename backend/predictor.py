"""Model inference and helper codes"""

import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
import os
import torch

from PIL import Image
from io import BytesIO
from torchvision import transforms

def get_prediction_model():
    model = torch.hub.load('pytorch/vision:v0.10.0', 'resnet18', pretrained=True)
    model.eval()
    return model

def read_image(image_encoded):
    image = Image.open(BytesIO(image_encoded))
    return image

def preprocess(input_image):
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    input_tensor = preprocess(input_image)
    input_batch = input_tensor.unsqueeze(0) # create a mini-batch as expected by the model
    return input_batch

def predict(input_image, model):
    # Move the input and model to GPU for speed if available
    if torch.cuda.is_available():
        input_image = input_image.to('cuda')
        model.to('cuda')

    with torch.no_grad():
        output = model(input_image)
    # The output has unnormalized scores. To get probabilities, you can run a softmax on it.
    probabilities = torch.nn.functional.softmax(output[0], dim=0)
    
    results = {"success": False}
    results["predictions"] = []
    # Read the categories
    with open("imagenet_classes.txt", "r") as f:
        categories = [s.strip() for s in f.readlines()]
    # Show top categories per image
    top5_prob, top5_catid = torch.topk(probabilities, 5)
    for i in range(top5_prob.size(0)):
        r = {"label": categories[top5_catid[i]], "probability": float(top5_prob[i].item())}
        results["predictions"].append(r)
    results["success"] = True
    return results

