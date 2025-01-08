FROM python:3.11.11-slim

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libffi-dev \
    && apt-get clean

WORKDIR /app

COPY requirements.txt /app

RUN pip install -U pip
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY src /app

EXPOSE 8501