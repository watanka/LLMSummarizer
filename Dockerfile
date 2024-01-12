FROM python:3.10-slim

COPY . .
ENV OPENAI_API_KEY=${OPENAI_API_KEY}

RUN pip3 install -r requirements.txt


EXPOSE 8090

ENTRYPOINT [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8090" ]
# ["gunicorn", "--bind", "unix:/tmp/myapi.sock", "main:app", "--worker-class", "uvicorn.workers.UvicornWorker"]
