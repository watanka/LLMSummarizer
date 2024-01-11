FROM python:3.10-slim

WORKDIR /streamlit

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8500

ENTRYPOINT [ "streamlit", "run", "ui.py"]