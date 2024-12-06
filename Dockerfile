# Base image
FROM python:3.9-slim

# Install dependencies
RUN pip install flask prometheus-client google-cloud-aiplatform

# Add the application code
WORKDIR /app
COPY . /app

# Expose Prometheus metrics endpoint
EXPOSE 8000

# Start the application
CMD ["python", "app.py"]
