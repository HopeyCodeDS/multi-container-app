#!/bin/bash

set -e

# Function to print status messages
print_status() {
  echo "=========================================="
  echo "$1"
  echo "=========================================="
}

print_status "Stopping and removing existing containers"
docker-compose -f deployment/docker-compose.yml down

print_status "Building and starting containers"
docker-compose -f deployment/docker-compose.yml up --build -d

print_status "Printing container status"
docker-compose -f deployment/docker-compose.yml ps

sudo install minikube-linux-amd64 /usr/local/bin/minikube
minikube version

minikube start --profile=minikube

print_status "Stopping Minikube"
minikube stop

print_status "Deleting Minikube"
minikube delete

print_status "Starting Minikube"
minikube start --force --extra-config=kubeadm.ignore-preflight-errors=DirAvailable,FileAvailable,Port-10250,Swap,NumCPU,Mem,SystemVerification,FileContent--proc-sys-net-bridge-bridge-nf-call-iptables --v=5

print_status "Creating the volume"
kubectl apply -f ./deployment/k8s/persistent-volume.yml
kubectl apply -f ./deployment/k8s/persistent-volume-claim.yml

print_status "Creating the database credentials"
kubectl apply -f ./deployment/k8s/postgres-secret.yaml
kubectl create secret generic ssl-certs-secret --from-file=./src/certs/server.crt --from-file=./src/certs/server.key

print_status "Creating the PostgreSQL ConfigMaps for initialization scripts"
kubectl create configmap create-table-script --from-file=./deployment/create_table.sql
kubectl create configmap insert-data-script --from-file=./deployment/insert_data.sql

print_status "Creating the PostgreSQL deployment and service"
kubectl apply -f ./deployment/k8s/postgres-deployment.yml
kubectl apply -f ./deployment/k8s/postgres-service.yml

print_status "Waiting for PostgreSQL to be ready"
kubectl rollout status deployment/postgres

print_status "Creating the Flask deployment and service"
kubectl apply -f ./deployment/k8s/flask-deployment.yaml
kubectl apply -f ./deployment/k8s/flask-service.yaml

print_status "Waiting for Flask to be ready"
kubectl rollout status deployment/enterprise-web-app

print_status "Checking the status of the Flask service"
kubectl get services enterprise-web-app

print_status "Deployment completed successfully"

print_status "Opening Minikube dashboard"
minikube dashboard