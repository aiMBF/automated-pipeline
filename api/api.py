from fastapi import FastAPI, Response, status
import random
import time
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST


app = FastAPI()

# Prometheus metrics
REQUEST_COUNT = Counter(
    "api_requests_total", "Total number of requests", ["endpoint", "http_status"]
)
REQUEST_LATENCY = Histogram(
    "api_request_duration_seconds", "Latency of requests", ["endpoint"]
)

@app.get("/data")
def get_data():
    start_time = time.time()

    # Simulate latency
    simulated_latency = random.uniform(0.1, 2.0)
    time.sleep(simulated_latency)

    # Simulate random HTTP error
    if random.random() < 0.2:
        REQUEST_COUNT.labels(endpoint="/data", http_status="500").inc()
        return Response(content="Internal error", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    REQUEST_COUNT.labels(endpoint="/data", http_status="200").inc()
    REQUEST_LATENCY.labels(endpoint="/data").observe(time.time() - start_time)

    return {"message": "Data OK", "latency": round(simulated_latency, 2)}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
