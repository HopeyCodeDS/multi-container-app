#!/bin/bash

# Stop and remove existing containers
docker-compose -f deployment/docker-compose down

# Build and start containers
docker-compose -f deployment/docker-compose up --build -d

# Print status
docker-compose -f deployment/docker-compose ps
