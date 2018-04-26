FROM python:3.6
ENV PYTHONBUFFERED = 1
RUN mkdir /src
WORKDIR /src
ADD requirements.txt /src
RUN pip install -r requirements.txt
ADD . /src