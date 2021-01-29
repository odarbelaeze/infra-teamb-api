FROM python:3.9-alpine
COPY requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt
COPY app.py /src/app.py
WORKDIR /src
EXPOSE 8080
CMD uvicorn --host 0.0.0.0 --port 8080 app:app
