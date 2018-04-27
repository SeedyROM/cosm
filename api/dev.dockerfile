FROM python:3.6
ENV PYTHONBUFFERED = 1
ENV DOCKER = true
RUN mkdir /src
WORKDIR /src
ADD requirements.txt /src
RUN pip install -r requirements.txt
ADD . /src
CMD ["bash", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py devcreatesuperuser && python manage.py runserver 0.0.0.0:8000"]