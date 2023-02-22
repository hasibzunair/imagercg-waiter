# Image Recognition Waiter

This application deploys a deep learning image classification model as an API endpoint that recognizes what object is present in an image. It accepts images from the user, call the endpoint that makes a prediction, and shows results in a frontend UI. It demonstrates use-cases of different tools such as `PyTorch`, `FastAPI`, `Gradio` and `Docker`.

<p align="left">
  <a href="#"><img src="./frontend/test1.jpeg" width="200"></a> <br />
  <em> 
    Model Output: `king penguin: 0.99`.
  </em>
</p>


### Usage
To launch the application, run:
```
sh deploy_app.sh
```
The app is live in `http://0.0.0.0:7860`. Upload images to make a prediction, or simply use the examples! For details on how the `frontend` and `backend` components were built, see respective folders. 

### Note
I did this small project after completing [Docker for the Absolute Beginner - Hands On - DevOps](https://www.udemy.com/course/learn-docker/).

#### Todos
* Google cloud run for backend
* Docker compose
* Kubernetes (make some pods lol!)