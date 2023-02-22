# run backend
docker run -p 8000:80 --name cls-serve hasibzunair/classification_model_serving
# run frontend
docker run -p 7860:7860 --add-host host.docker.internal:host-gateway --name frnt-serve hasibzunair/frontend_serving