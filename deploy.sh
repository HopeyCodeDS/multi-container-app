#!/bin/bash

# Stop and remove existing containers
docker-compose -f deployment/docker-compose.yml down

# Build and start containers
docker-compose -f deployment/docker-compose.yml up --build -d

# Print status
docker-compose -f deployment/docker-compose.yml ps
