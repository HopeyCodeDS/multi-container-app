# Exam Project

## Overview
This project deploys a multi-container application consisting of a Python web server and a PostgreSQL database.

## Project Structure
Explanation of the project structure and the purpose of each file and directory.

## Setup Instructions
1. Clone the repository.
2. In the src directory build the image and push to docker registry with the command below



            # Build image
            docker build -t opeyemimomodu/enterprise-web-app .

            # Push image
            docker push opeyemimomodu/enterprise-web-app



2. Navigate to the `deployment` directory.
3. Run the `deploy.sh` script to build and start the containers.
4. Navigate to the root directory, open the `deploy_kubernetes.sh` file to setup the kubernetes

## Usage
- The web server will be accessible at `http://127.0.0.1:8080/employees`.

[//]: # (- The web server will be accessible at `https://localhost:5000`.)
- The endpoint `/employees` will fetch the list of employees from the database.

## Technologies Used
- Python
- Flask
- PostgreSQL
- Docker
- Docker Compose
- Kubernetes
- Terraform 

## Note
If the script doesn't run it all directly, you can everything up by running the commands individually, especially for the kubernetes parts.
