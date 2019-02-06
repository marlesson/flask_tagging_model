#gcloud builds submit --tag gcr.io/datascience-225400/flask-api .

FROM python:3
COPY . /app
WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
EXPOSE 80

ENTRYPOINT python ./main.py

