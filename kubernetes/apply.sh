#!/bin/bash

# Delete existing minikube cluster
minikube delete

# Start minikube
minikube start --driver=docker

# Create config map for init-db.sql
kubectl create configmap init-db-config --from-file=init-db.sql

# Apply persistent volume and claim
kubectl apply -f postgres-pv.yaml

# Apply PostgreSQL deployment and service
kubectl apply -f postgres-deployment.yaml
kubectl apply -f postgres-service.yaml

# Apply application deployment and service
kubectl apply -f deployment.yaml
#kubectl apply -f service.yaml

# Wait for all pods to be running
kubectl wait --for=condition=available --timeout=600s deployment/postgres
kubectl wait --for=condition=available --timeout=600s deployment/momodu-rilwan-opeyemi-app

# Get Minikube IP and service ports
minikube service momodu-rilwan-opeyemi-app --url
