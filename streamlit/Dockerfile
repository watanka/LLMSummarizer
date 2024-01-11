FROM python:3.10-slim

WORKDIR /streamlit
ENV OPENAI_API_KEY ${OPENAI_API_KEY}

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8500

ENTRYPOINT [ "streamlit", "run", "ui.py"]