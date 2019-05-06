# Project Template for a Reproducible Research Project

## Setup

To start a new research project, ensure all the requirements are fulfilled then run

```
cookiecutter
```

## Requirements

The template uses [cookiecutter](https://github.com/audreyr/cookiecutter) for scaffolding. Currently only tested on OS X.

To setup a new project you need to have `R` installed.

# Working with R in Docker

One way of using this template is to work with R in a docker container. To do so, first build your container using

```sh
docker build -t test_image -f Dockerfile --build-arg UID=$(id -u) .
```

We can then create the container running

```sh
docker run -it -v $(pwd):/work -p 8888:8888 --name test_container test_image
```

And jump into it by doing

```sh
if [ `docker inspect -f {% raw -%}{{.State.Running}}{%- endraw %} test_container` = "false" ] ; then
        docker start test_container
fi
start-container: ## start docker container
	@echo "$$START_DOCKER_CONTAINER" | $(SHELL)
	@echo "Launched test_container..."
docker attach test_container
```

For testing, to cleanup

```sh
docker ps --all
docker images --all
docker rm test_container
docker rmi test_image
```
