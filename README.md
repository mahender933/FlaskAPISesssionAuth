# Authentication using Session
Simple application built using flask in which session based authentication has been used.

To override the default session set session TTL enviroment variable with name `SESSION_EXPIRY_TTL` having value in minutes by 
using export command if in unix based system


`export SESSION_EXPIRY_TTL=int_value_in_minutes`

# Improvements TODO
* Test coverage needs to be increased
* Documentation pending for apis
* Integrate support for multiple environment : development, production and testing.


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
 

### Initialize migration
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
`docker run -d -p 5000:5000 flask-demo-app`


## Endpoints 
* Api overview - `http://localhost:5000/api`
* Signup:  `http://localhost:5000/sign-up`
* Login: `http://localhost:5000/login`
* Logout: `http://localhost:5000/logout`
* Profile: `http://localhost:5000/profile` 

#### API Overview (/api)
    * Method Allowed : GET
    * Returns all endpoints
    
#### Signup (/sign-up)
    * Adds a new user
    * Method Allowed : POST
        "payload_example": {
            "username": "(str) Username which is unique",
            "email": "(str) Email address",
            "phone_number": (str) Phone Number(validates indian phone number),
            "password": (str) Password must contain at least one character, one number and any one of these (underscore, hyphen, hash) and Password max length should be 6.
        }

#### Login (/login)
    * Login existing user
    * Method Allowed : POST
        "payload_example": {
            "username": "(str) Username",
            "password": (str) Password for that user.
        }

#### Logout (/logout)
    * Logout currently logged in user.
    * Method Allowed : POST

#### Profile (/profile)
    * Returns currently logged in user profile related information such as username, email etc.
    * Method Allowed : GET
    
    
    

