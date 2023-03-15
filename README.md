# Image Recognition Waiter

This application *serves* a deep learning image classification model that recognizes what object is present in an image. It accepts images from the user, makes request to an API endpoint that makes a prediction, and shows results in a frontend UI. 

It demonstrates use-cases of different tools such as `PyTorch`, `FastAPI`, `Gradio` and `Docker`.

***A detailed writeup is published in [Towards AI](https://medium.com/towards-artificial-intelligence/build-and-deploy-custom-docker-images-for-object-recognition-d0d127b2603b)!***

<p align="left">
  <a href="#"><img src="./frontend/test1.jpeg" width="200"></a> <br />
  <em> 
    Model Output: `king penguin: 0.99`.
  </em>
</p>


### Usage
To launch the application, run:
```
git clone https://github.com/hasibzunair/imagercg-waiter
cd imagercg-waiter/backend
sh deploy.sh
```

The app is live in `http://0.0.0.0:7860`. Upload images to make a prediction, or simply use the examples! For details on how the `frontend` and `backend` components were built, see respective folders. 

### Note
I did this project after completing [Docker for the Absolute Beginner - Hands On - DevOps](https://www.udemy.com/course/learn-docker/).

#### Todos
* Google cloud run for backend
* Docker compose
* Kubernetes (make some pods lol!)

### References
Also see [learn-docker](https://github.com/hasibzunair/learn-docker).
