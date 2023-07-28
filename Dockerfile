FROM python:3.8

#Set the working directory
WORKDIR /

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 1

#copy all the files
COPY . .

#Install the dependencies
RUN apt-get -y update
RUN apt-get update && apt-get install -y python3 python3-pip
# RUN pip3 install cmake
# RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip3 install -r requirements.txt

#Expose the required port
# EXPOSE 5000

# run gunicorn
# CMD gunicorn Spardha.wsgi.application --bind 0.0.0.0:$PORT
# CMD gunicorn Spardha.wsgi.application --bind 0.0.0.0:8000
# CMD python Spardha/manage.py runserver $PORT
CMD python Spardha/manage.py runserver
