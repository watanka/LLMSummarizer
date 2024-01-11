FROM python:3.10-slim

WORKDIR /summarizer
COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8090

ENTRYPOINT [ "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8090" ]