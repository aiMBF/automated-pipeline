FROM python:3.12-slim

WORKDIR /app

COPY poll_api.py .

RUN pip install requests

CMD ["python", "poll_api.py"]