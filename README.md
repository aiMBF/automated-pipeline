# 📊 FastAPI Monitoring with Prometheus & Grafana

This project sets up a complete monitoring pipeline for a simulated FastAPI service, using **Prometheus** for metrics collection and **Grafana** for visualization. It includes automatic load simulation and exposes custom metrics like request volume, error rate, and latency.

---

## 🚀 Features

- Custom Prometheus metrics (`api_requests_total`, `api_request_duration_seconds`)
- Randomized API latency and 500 errors to simulate real-world conditions
- Load generator (polls the API every 5 seconds)
- Grafana dashboards with KPIs: total requests, errors, latency, availability
- Fully containerized with Docker Compose

---

## 📁 Project Structure

```
.
├── api/                  # FastAPI app with Prometheus instrumentation
│   ├── main.py
│   └── Dockerfile
├── load_tester/          # Script that simulates API traffic
│   ├── poll_api.py
│   └── Dockerfile
├── prometheus.yml        # Prometheus scrape config
├── docker-compose.yml    # Stack: Prometheus + Grafana + API + Load Tester
└── README.md
```

---

## How It Works

1. The FastAPI app exposes `/data` and `/metrics`
2. `/data` simulates response time and randomly returns 500s
3. A load generator (`poll_api.py`) sends a request every 5 seconds
4. Prometheus scrapes `/metrics` from the FastAPI service
5. Grafana reads metrics from Prometheus and displays dashboards

---

## 🧪 Getting Started

### 1. Clone the project

```bash
git clone https://github.com/aiMBF/fastapi-monitoring.git
cd fastapi-monitoring
```

### 2. Start the stack

```bash
docker compose up --build
```

- API: [http://localhost:8000/data](http://localhost:8000/data)
- Prometheus: [http://localhost:9090](http://localhost:9090)
- Grafana: [http://localhost:3000](http://localhost:3000)  
  Login: `admin / admin`

### 3. Import the dashboard in Grafana

- Go to **Dashboards -> New → Import**
- Upload the included `grafana_dashboard.json`

---

## 📊 Metrics Tracked

| Metric                          | Description                             |
|---------------------------------|-----------------------------------------|
| `api_requests_total`           | Total number of requests by status code |
| `api_request_duration_seconds` | Response time in seconds   |
| `up`                           | API availability (1 = up, 0 = down)     |

---

## 📦 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [Prometheus](https://prometheus.io/)
- [Grafana](https://grafana.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## 📌 TODO

- Add Slack alerting with Alertmanager
- Add support for multiple endpoints
- Add readiness/liveness probes

# Grafana Visualisation 
- ! [Metrics visualization](screenshots/grafana_visualisation.png)
