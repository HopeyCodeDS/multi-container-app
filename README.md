# Project Overview

## Overview
This project deploys a multi-container application consisting of a Python web server and a PostgreSQL database.

## Project Structure
Explanation of the project structure and the purpose of each file and directory.

## Setup Instructions
1. Clone the repository.
2. In the src directory build the image, push to or pull from my docker registry with the command below



            # Build image
            docker build -t opeyemimomodu/enterprise-web-app .

            # Push image
            docker push opeyemimomodu/enterprise-web-app

            # Pull image
            docker pull opeyemimomodu/enterprise-web-app



2. Navigate to the `deployment` directory.
3. Run the `deploy.sh` script to build and start the docker containers.
4. Navigate to the root directory, open the `deploy_kubernetes.sh` file to view the kubernetes setup.
5. Better still for automated deployment, run the `automated_deployment.sh` in the root directory.

## Usage
- The web server will be accessible at http://127.0.0.1:8080/employees or http://localhost:8080/employees on dockers.

[//]: # (- The web server will be accessible at `https://localhost:5000`.)
- The endpoint `/employees` will fetch the list of employees from the database.

### Deployment
Docker Deployment alone

For local development or testing, you can deploy the application using Docker Compose:


    cd deployment/
    docker-compose up -d
´´´

### Automated Deployment 

For production deployment or Kubernetes testing environments, you can deploy the application to a Kubernetes cluster:


    ./automated_deployment.sh

´´´
This script will run all necessary docker and Kubernetes resources defined in the script.

### Screenshots of successfully deployment
![shot1.png](images%2Fshot1.png)
![shot2.png](images%2Fshot2.png)
![shot3.png](images%2Fshot3.png)
![shot4.png](images%2Fshot4.png)
![kubernetes_shot1.png](images%2Fkubernetes_shot1.png)
![kubernetes_shot2.png](images%2Fkubernetes_shot2.png)
![kubernetes_shot3.png](images%2Fkubernetes_shot3.png)


## Technologies Used
- Python
- Flask
- PostgreSQL
- Docker
- Docker Compose
- Kubernetes
- Terraform 

[//]: # (## Note)

[//]: # (If the bash script doesn't run directly, you can start everything up by running the commands individually, especially for the kubernetes parts.)
