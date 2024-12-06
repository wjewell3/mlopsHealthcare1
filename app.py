from flask import Flask, jsonify
from prometheus_client import start_http_server, Summary, Counter

app = Flask(__name__)

# Prometheus metrics
REQUEST_COUNT = Counter("app_requests", "Number of requests received")
REQUEST_TIME = Summary("request_processing_time", "Time spent processing requests")

@app.route("/predict", methods=["POST"])
@REQUEST_TIME.time()
def predict():
    REQUEST_COUNT.inc()
    # Example Vertex AI Prediction logic
    return jsonify({"prediction": "success"})

@app.route("/metrics", methods=["GET"])
def metrics():
    # Prometheus metrics will be automatically served here
    return "Prometheus metrics endpoint"

if __name__ == "__main__":
    start_http_server(8000)  # Prometheus metrics on port 8000
    app.run(host="0.0.0.0", port=5000)
