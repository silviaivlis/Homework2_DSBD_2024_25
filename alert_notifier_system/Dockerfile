FROM python:3.13-slim

WORKDIR /app

COPY alert_notifier_system/requirements.txt .

COPY alert_notifier_system/ .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1

CMD ["python", "alertNotifierSystem.py"]