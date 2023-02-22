# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy every content from the local folder to the image
COPY . .

# Run server
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=80"]