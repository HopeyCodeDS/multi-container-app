#!/bin/bash

minikube start

echo "Creating the volume..."
kubectl apply -f ./deployment/k8s/persistent-volume.yml
kubectl apply -f ./deployment/k8s/persistent-volume-claim.yml

echo "Creating the database credentials..."
kubectl apply -f ./deployment/k8s/postgres-secret.yaml

echo "Creating the postgres deployment and service..."
kubectl apply -f ./deployment/k8s/postgres-deployment.yml
kubectl apply -f ./deployment/k8s/postgres-service.yml

echo "Creating the database tables..."
kubectl apply -f ./deployment/k8s/create-table-configmap.yaml
kubectl apply -f ./deployment/k8s/insert-data-configmap.yaml

echo "Creating the flask deployment and service..."

kubectl apply -f ./deployment/k8s/flask-deployment.yaml
kubectl apply -f ./deployment/k8s/flask-service.yaml

echo "Checking the status of the flask deployment and service..."

kubectl rollout status deployment/enterprise-web-app
kubectl get services enterprise-web-app


echo "Adding the ingress..."
minikube addons enable ingress
kubectl delete -A ValidatingWebhookConfiguration ingress-nginx-admission
kubectl apply -f ./deployment/k8s/minikube-ingress.yml