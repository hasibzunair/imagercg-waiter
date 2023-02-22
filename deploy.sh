# run backend
docker run -d -p 8000:80 --name cls-serve hasibzunair/classification_model_serving

# wait 10 seconds for the model to download
sleep 10

# run frontend
docker run -p 7860:7860 --add-host host.docker.internal:host-gateway --name frnt-serve hasibzunair/frontend_serving