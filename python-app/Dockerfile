FROM python:3.12.7-bookworm

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

VOLUME ["/app/src"]

EXPOSE 8001

CMD ["python3", "src/main.py"]
