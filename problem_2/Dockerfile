FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && apt-get install -y openjdk-17-jdk-headless curl

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN chmod +x /app/entrypoint.sh

CMD ["/app/entrypoint.sh"]
