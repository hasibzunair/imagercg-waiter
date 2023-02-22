# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy every content from the local folder to the image
COPY . .

# Run server, deafult gradio url is http://127.0.0.1:7860
CMD [ "python3", "-u", "/app/main.py" ]