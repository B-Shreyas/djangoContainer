# djangoContainer
To create Python-Django environment in Docker

![Docker-Django](https://user-images.githubusercontent.com/60639143/80909225-56b1b200-8d44-11ea-97a0-30afb4075e75.jpg)


# Running Django project in Docker container

This is an example, in simplest form, of running Django project in Docker container.
With this, you need not to create virtual environment or to install anything at all.

# You can download/pull my images on following link:

https://hub.docker.com/repository/docker/shreyas20/python_in_django

### Steps:
- Clone this git repo.

    `git clone https://github.com/B-Shreyas/djangoContainer.git`

 - Build a docker image using the Dockerfile in root directory of this repo.

    `docker build -t image_name .`

 - start the container.

    `docker container run --rm -p 8800:8800 --name django-sample image_name`

     - go to browser localhost:8800


### Notes:
- To test the project as you code, mount the current directory while running container.

 `sudo docker container run -v "$(pwd)":/usr/src/app  --rm -p 8800:8800 --name django-sample image_name`


### Installing Docker:
Please follow steps given at below link to install Docker.

https://docs.docker.com/get-docker/

We are using Docker version 19.03.8, build afacb8b7f0
for this article.


### Starting docker container of application:

- Create your Django project. You may start with hello world Django project Or you can clone this github repo.
- Add requirements.txt file and add django==1.10.0 in it.

- Create a Dockerfile and add below text in it.

  Each step is explained using comment above it.
  
  ![stepsExplain](https://user-images.githubusercontent.com/60639143/80909541-ce80dc00-8d46-11ea-9277-f3f8d3dae5b5.jpg)

 ### Now lets create a docker image of our project. Run below command.

     docker build -t image_name .

 ### Run a container using this newly created image.

     docker container run --rm -p 8800:8800 --name django-sample image_name

 ### Now open another terminal and run the below command to see the running containers.

     docker container ls -a
     
 ### output will be something like this:
   
  ![output](https://user-images.githubusercontent.com/60639143/80909928-d5f5b480-8d49-11ea-9fd1-0582d21d4127.jpg) 

 
 - Now go to localhost:8800/helloworld/  in your browser and you can see the template being rendered.

  
  ![localhost](https://user-images.githubusercontent.com/60639143/80909925-d2622d80-8d49-11ea-996b-d501315f8e51.jpg) 

 
 ### You we provide absolute path as well instead of "$(pwd)" . Now if you change your response text in views.py  file, it will be reflected immediately in the browser. You can see in the terminal output of docker container that python server is reloaded as you change and save some file.  


  ![terminal](https://user-images.githubusercontent.com/60639143/80909932-dd1cc280-8d49-11ea-8385-704db1170454.jpg)



 ### Now we can develop your application without worrying about virtual environments. Everytime you are going to develop an Django application, follow the above steps to start the application in container.
