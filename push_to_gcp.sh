# Authenticate with GCP
gcloud auth configure-docker

# Build Docker image
docker build -t gcr.io/<your-project-id>/vertex-ai-app:latest .

# Push image to GCR
docker push gcr.io/<your-project-id>/vertex-ai-app:latest
