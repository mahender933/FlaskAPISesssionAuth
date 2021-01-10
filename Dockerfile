FROM python:alpine3.7
COPY . /demo_app
WORKDIR /demo_app
RUN pip install -r requirements.txt
EXPOSE 5000
RUN chmod +x manage.py
# Make Entrypoint executable
RUN chmod +x db_init.sh
RUN ./db_init.sh
CMD ["python", "manage.py", "runserver", "-h", "0.0.0.0"]


