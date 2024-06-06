# Use official Python image from the Docker Hub
FROM python:3.9

# Set environment variables
ENV POSTGRES_DB=Enterprise
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=Student_1234
ENV POSTGRES_HOST=postgres

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y netcat-openbsd

# Add postgresql client
RUN apt-get install -y postgresql-client

# Add entrypoint.sh
COPY ./entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Copy SSL certificates
COPY certs/server.crt /app/certs/server.crt
COPY certs/server.key /app/certs/server.key

# Make port 5000 available to the world outside this container
EXPOSE 8080
#EXPOSE 5000

# Define environment variable
ENV NAME World

# Run entrypoint.sh when the container launches
CMD ["sh", "/app/entrypoint.sh"]

