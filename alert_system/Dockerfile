FROM python:3.13-slim

WORKDIR /app

COPY alert_system/requirements.txt .

COPY alert_system/ .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1

CMD ["python", "alertSystem.py"]