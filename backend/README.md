# PyTorch + FastAPI Backend

Serves a dockerized deep learning image classification model using FastAPI. I used an ImageNet pretrained model that can predict 1000 different classes of general objects. See class list [here](https://deeplearning.cms.waikato.ac.nz/user-guide/class-maps/IMAGENET/).

### Local development
To use this code for local development, install the requirements using (make sure Python version is 3.8):
```bash
git clone https://github.com/hasibzunair/imagercg-waiter
cd imagercg-waiter/backend
pip install -r requirements.txt
```
Now, you're setup!

#### Usage
To launch the FastAPI application locally, run:
```python
python main.py
```

A FastAPI application will run on your local machine. See Swagger UI at `http://127.0.0.1:8000/docs` for more info. To interact with it, open a new terminal and just send a curl request like this:
```bash
curl -X POST -F image=@test1.jpeg "http://127.0.0.1:8000/api/predict"
```

Using the `test1.jpeg` image, the `JSON` response result should look like this, with labels and the probability values for the given image:
```json
{
  "success": true, 
  "predictions": 
  [
    {
      "label": "king penguin", 
      "probability": 0.999931812286377
    }, 
    {
      "label": "guenon", 
      "probability": 9.768833479029126e-06
    }, 
    {
      "label": "megalith", 
      "probability": 8.01052556198556e-06
    }, 
    {
      "label": "cliff", 
      "probability": 7.119778274500277e-06
    }, 
    {
      "label": "toucan", 
      "probability": 6.5011186052288394e-06
    }
  ]
}
```

Or, submit a request using a Python script:
```python
python request.py
```
The result should look like this:
```bash
1. king penguin: 0.9999
2. guenon: 0.0000
3. megalith: 0.0000
4. cliff: 0.0000
5. toucan: 0.0000
```

To try it with any of your own images(`*.jpg`,`*.jpeg`,`*.png`), set path to your image `YOUR_IMG_PATH` and run:
```bash
curl -X POST -F image=@YOUR_IMG_PATH "http://127.0.0.1:8000/api/predict"
```

### Dockerized backend

To containerize the backend, we create a docker image and run 
and instance of the image (a container), using:
```
# build
docker build -t classification_model_serving .
# run
docker run -p 8000:80 --name cls-serve classification_model_serving
```

Now, the model is deployed as an API endpoint in your local machine using docker. Finally, run `curl -X POST -F image=@test1.jpeg "http://0.0.0.0:8000/api/predict"` in your terminal. You should get the same JSON response as above.

#### Push to and test image from Docker Hub
```
# tag
docker tag classification_model_serving hasibzunair/classification_model_serving
# push
docker push hasibzunair/classification_model_serving
# run backend from hub
docker run -p 8000:80 --name cls-serve hasibzunair/classification_model_serving
```

Again, you should be able to run `curl -X POST -F image=@test1.jpeg "http://0.0.0.0:8000/api/predict"` and get the same JSON format predictions.