FROM mysql:latest

FROM python:3.8

#create folder
RUN mkdir -p /opt/code
RUN mkdir -p /opt/code/api

#Install dependencies
COPY requirements.txt /opt/code/api
WORKDIR /opt/code/api

RUN apt-get update
RUN apt-get install -y python3-setuptools nano 
RUN apt-get install -y python3-pip
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install mysqlclient

# Expose the default port
EXPOSE 3306
EXPOSE 8080

# COPY ./app /app

#Uvicorn 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]