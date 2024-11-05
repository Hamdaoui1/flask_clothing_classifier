# Flask Clothing Classifier

This repository hosts a Flask API that classifies images of clothing items using a pre-trained MobileNetV2 model. The application is containerized using Docker and deployed on an Oracle Cloud instance, allowing public access for testing and usage.

## Prerequisites

To use or modify this project, ensure you have the following:
- Docker installed
- A Flask-compatible Python environment (Python 3.8+)
- Basic knowledge of deploying Docker containers to cloud services like Oracle Cloud

## Features

This API:
- Accepts image input via a POST request.
- Uses MobileNetV2 to classify clothing categories.
- Returns the category in French if recognized as a clothing item; otherwise, it labels the item as "autres".

## API Deployment and Access

The API is deployed on an Oracle Cloud instance and accessible to the public. To interact with the API, send a POST request with an image file to:

http://<Public_IP_Address>:8080/classify

Replace <Public_IP_Address> with the actual public IP of the Oracle instance.

## Project Setup and Usage

1. **Clone the Repository**: Clone this repository to your local environment.

   git clone https://github.com/yourusername/flask_clothing_classifier.git
   cd flask_clothing_classifier

2. **Build the Docker Image**: Use Docker to create an image from the Dockerfile.

   docker build -t flask_clothing_classifier .

3. **Run the Docker Container Locally**: To test the API locally, you can run the container and map port 8080 to port 5000 inside the container.

   docker run -d -p 8080:5000 flask_clothing_classifier

4. **Deploying to Oracle Cloud**: Follow these steps if deploying to an Oracle Cloud instance:
   - Transfer the Docker image to the Oracle instance.
   - Use podman to load the Docker image on Oracle Linux if Docker isn’t available.
   - Configure Oracle's firewall to allow connections on port 8080.
   - Run the container on Oracle and verify the public accessibility.

## API Usage

Send a POST request with an image file to classify. Example command:

curl -X POST -F image=@/path/to/image.jpg http://<Public_IP_Address>:8080/classify

This returns the category label in French if the item is recognized as clothing, or "autres" if it is not.
