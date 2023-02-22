import gradio as gr
import requests

# Set URL
# Run: 
# docker run -p 8000:80 --name cls-serve hasibzunair/classification_model_serving
REST_API_URL = "http://host.docker.internal:8000/api/predict"

# Inference!
def inference(image_path):

    # Load the input image and construct the payload for the request
    image = open(image_path, "rb").read()
    payload = {"image": image}

    # Submit the request
    r = requests.post(REST_API_URL, files=payload).json()

    # Ensure the request was sucessful, format output for visualization
    output = {}
    if r["success"]:
        # Loop over the predictions and display them
        for (i, result) in enumerate(r["predictions"]):
            output[result["label"]] = result["probability"]
            print("{}. {}: {:.4f}".format(i + 1, result["label"],
                result["probability"]))
    else:
        print("Request failed")
    return output

# Define ins outs placeholders
inputs = gr.inputs.Image(type='filepath')
outputs = gr.outputs.Label(type="confidences",num_top_classes=5)

# Define style
title = "Image Recognition Waiter"
description = "This is a prototype application which demonstrates how artifical intelligence based systems can recognize what object(s) is present in an image. This fundamental task in computer vision known as `Image Classification` has applications stretching from autonomous vehicles to medical imaging. To use it, simply upload your image, or click one of the examples images to load them, which I took at <a href='https://espacepourlavie.ca/en/biodome' target='_blank'>Montréal Biodôme</a>! Read more at the links below."
article = "<p style='text-align: center'><a href='https://arxiv.org/abs/1512.03385' target='_blank'>Deep Residual Learning for Image Recognition</a> | <a href='https://github.com/pytorch/vision/blob/main/torchvision/models/resnet.py' target='_blank'>Github Repo</a></p>"

# Run inference
frontend = gr.Interface(inference, 
            inputs, 
            outputs, 
            examples=["test1.jpeg", "test2.jpeg"], 
            title=title, 
            description=description, 
            article=article,
            analytics_enabled=False)


# Launch app and set PORT
try:
    frontend.launch(server_name="0.0.0.0", server_port=7860)
except KeyboardInterrupt:
    frontend.close()
except Exception as e:
    print(e)
    frontend.close()



