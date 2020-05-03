# djangoContainer
To create Python-Django environment in Docker

![Docker-Django](https://user-images.githubusercontent.com/60639143/80909225-56b1b200-8d44-11ea-97a0-30afb4075e75.jpg)


# Running Django project in Docker container

This is an example, in simplest form, of running Django project in Docker container.
With this, you need not to create virtual environment or to install anything at all.

### Steps:

 - Clone this git repo.

    `git clone https://github.com/anuragrana/docker-django-example`

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
