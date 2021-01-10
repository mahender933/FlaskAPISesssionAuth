# Authentication using Session
Simple application built using flask in which session based authentication has been used
.

To override the default session TTL set enviroment variable with name `SESSION_EXPIRY_TTL` having value in minutes by 
using export command if in unix based system


`export SESSION_EXPIRY_TTL=int_value_in_minutes`

# Improvements TODO
* Test coverage needs to be increased
* Documentation pending for apis


# Requirements
Python 3.7
In Ubuntu and Debian you can install Python 3.7 like this:
```
$ sudo apt-get install python3.7 python3.7-pip
```

# Installation
* Go to root path where `requirements.txt` resides by using `cd` command.
* Install all requirements by using `pip`  
```
pip install -r requirements.txt
```
 

### Initialise migration
python manage.py db init

### Generate an initial migration
python manage.py db migrate -m "Initial Migration"

### Apply the migration to database
python manage.py db upgrade

### Start a server
python manage.py runserver

### Testing 
Run test cases by following command

``python manage.py test``

### Run server using Docker

*  Build the image
``
docker build -t flask-demo-app:latest .
``
* Run Docker Container
`docker run -d -p 5000:5000 flask-tutorial`



