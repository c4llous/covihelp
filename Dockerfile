# Pull from base image 

FROM python:3.9

# Set Environment Variable 

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work direcotry 

WORKDIR /code

# Install Dependencies 

COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

# Copy project

COPY . /code/