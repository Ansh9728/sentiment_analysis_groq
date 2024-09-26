# Sentiment Analysis API

This repository contains a FastAPI application that performs sentiment analysis on customer reviews using the Groq API. The application is dockerized for easy deployment.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Docker_Setup](#docker_setup)
- [Application Testing](#testing_development)
- [Docker Container Management](#docker_container_management)
- [Directl Run DockerHub](#run_using_dockerhub)

## Prerequisites

Before you begin, ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- Python 3.7+ (for local development, if needed)

## Installation

1. Clone the repository:

   ```bash
   git clone (https://github.com/Ansh9728/sentiment_analysis_groq.git)
   cd sentiment_analysis_groq

## Docker Setup

### Step 1: Build the Docker Image

Run the following command to build the Docker image:

```bash
docker build -t <image_name> .
```

This will create a Docker image tagged as `provided image name`.

### Step 2: Run the Docker Container

Once the image is built, you can run the container by executing:

```bash
docker run -d -p 8000:8000 --name <container_name> <image_name>
example:  sudo docker run --env-file .env -d -p 8000:8000 --name sentiment_api sentiment-analysis-api
```

- `-d`: Runs the container in detached mode (in the background).
- `-p 8000:8000`: Maps port 8000 of your local machine to port 8000 of the container.
- `--name container_name`: Names the running container as `containe_namer`.
- `--env-file .env`: send the enviroment variable during runtime 
- 
### Step 3: Access the Application

Once the container is running, you can access the FastAPI app at:

- **API Base URL**: `(http://0.0.0.0:8000 )`
- **API Documentation** (Swagger UI): `http://localhost:8000/docs`

## Testing and Development

For development purposes, you can directly run the FastAPI app without Docker:

#### Install Dependencies (Optional for Local Development)

First, create a Python virtual environment and install the dependencies from `requirements.txt`:

```bash
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Run the FastAPI Application Locally

You can start the FastAPI server locally using Uvicorn:

```bash
run python main.py
```

The app will be accessible at `http://127.0.0.1:8000/` locally.

## Docker Container Management

#### Stop the Container

To stop the running Docker container:

```bash
docker stop <container_name>
```

#### Restart the Container

To restart a stopped Docker container:

```bash
docker start <container_name>
```

#### Remove the Container

To remove the Docker container after stopping it:

```bash
docker rm <container_name>
```

To show error and logs Docker container:

```bash
docker logs -f  <container_name>
```
## Running the Application Directly from Docker Hub

If you want to run the application directly from Docker Hub without building it locally, you can pull the image and run it with the following commands:
Step 1: Pull the Docker Image

```bash
docker pull your_dockerhub_username/sentiment-analysis-api:latest

```
Step 2: Run the Docker Container

Once the image is pulled, run the container with:


```bash
docker run -d -p 8000:8000 --name container_name --env-file .env your_dockerhub_username/sentiment-analysis-api:latest

```

    -d: Runs the container in detached mode (in the background).
    -p 8000:8000: Maps port 8000 of your local machine to port 8000 of the container.
    --name fastapi_container: Names the running container as fastapi_container.
    --env-file .env: Passes the environment variables from your .env file.
