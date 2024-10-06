# Prometheus monitoring for Sample Python App

## Services

- Prometheus dashboard: http://localhost:9090
- Python App page: http://localhost:8001/
- Python App metrics endpoint: http://localhost:8000/metrics

## Run

Start services:
```bash
docker-compose up -d
```

Reload code changes in container with Python App:
```bash
docker-compose restart python-web-server
```
