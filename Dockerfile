# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.12-alpine
# run in un buffered mode, which is recommended with python running in docker containers
# doesn't buffer outputs, just prints directly
ENV PYTHONUNBUFFERED 1
# create root directory for our project in the container
RUN mkdir /Backend
# Set the working directory to /code
WORKDIR /Backend
# Copy the current directory contents into the container at /code
ADD . /Backend/
# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
