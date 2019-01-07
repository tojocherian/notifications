# Notificaitons

## Dependency

Will run on any machine with python3 and django installed
No external dependencies

## How to run

```
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ git clone https://github.com/tojocherian/notifications.git
$ cd notifications
$ pip install requirements.py
$ python3 manage.py runserver
```
## How to access the project

Then visit http://localhost:8000 to view the app.

All the JSON data will be loaded to the DB.

Then notifications related to each post will be available http://localhost:8000/posts/notifications/<post_id>/


## How to deploy

The project can be hosted on any platform (AWS EC2, Gcloud, Heroku).

Setup the the project using virtual environment and download the source code.

Make sure the the server's ip is added to allowed_hosts and DEBUG is False.

We can setup the WSGI application server and configure nginx. 

Once the configuration is done, restart nginx and start the WSGI server.

We can access the project using the ip and port number.

## Running the test

```
$ python manage.py test
```
