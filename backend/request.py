# USAGE
# python request.py
# Also try
# curl -X POST -F image=@test.jpeg "ENDPOINT_URL"

# Import the necessary packages
import requests

# Initialize the REST API endpoint URL along with the input
# image path
REST_API_URL = "http://127.0.0.1:8000/api/predict" # for local dev
IMAGE_PATH = "test1.jpeg" # example image

# Load the input image and construct the payload for the request
image = open(IMAGE_PATH, "rb").read()
payload = {"image": image}

# Submit the request
r = requests.post(REST_API_URL, files=payload).json()

# Ensure the request was sucessful
if r["success"]:
	# Loop over the predictions and display them
	for (i, result) in enumerate(r["predictions"]):
		print("{}. {}: {:.4f}".format(i + 1, result["label"],
			result["probability"]))
else:
	print("Request failed")