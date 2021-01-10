FROM python:alpine3.7
COPY . /demo_app
WORKDIR /demo_app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "manage.py", "runserver", "-h", "0.0.0.0"]


