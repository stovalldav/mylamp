FROM python:2.7-slim

WORKDIR /app

ADD ./pyListen/ /app

CMD ["python", "/app/listen.py"]

EXPOSE 8080
