FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Required to install mysqlclient with pip
RUN apt-get update \
  && apt-get install -y python3-dev default-libmysqlclient-dev gcc pkg-config \
  && rm -rf /var/lib/apt/lists/*

# Install dependencies using requirements.txt
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . /app/

# Copy and set entrypoint
COPY docker-entrypoint.sh /app/
COPY wait-for-it.sh /app/
RUN chmod +x /app/docker-entrypoint.sh /app/wait-for-it.sh

EXPOSE 8000
