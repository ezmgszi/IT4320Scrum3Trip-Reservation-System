#FROM python:3.7-alpine
#docker-compose up --build
FROM frolvlad/alpine-python-machinelearning
WORKDIR /project
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD ["python","wsgi.py"]
