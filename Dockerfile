FROM node:18-alpine as builder

COPY /frontend /frontend

RUN cd /frontend/ && npm install && npm run build 

FROM python:3.10-slim

COPY . .
COPY .env /.env

COPY --from=builder /frontend /

ENV OPENAI_API_KEY ${OPENAI_API_KEY}

RUN pip3 install -r requirements.txt


EXPOSE 8090

ENTRYPOINT [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8090" ]
# ["gunicorn", "--bind", "unix:/tmp/myapi.sock", "main:app", "--worker-class", "uvicorn.workers.UvicornWorker"]
