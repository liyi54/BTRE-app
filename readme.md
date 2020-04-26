# Property Listing Web App with Django

A Real Estate listing platform with an admin panel

* [Live URL](http://bigtimerealestate.xyz)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

```
asgiref==3.2.5
Django==3.0.4
Pillow==7.0.0
psycopg2==2.8.4
psycopg2-binary==2.8.4
pytz==2019.3
sqlparse==0.3.1
psql==11.5

```
A requirements.txt file has been created, use the following command to install these packages
```
pip install -r requirements.txt
```

### Installing

1. Create a virtual environment in the project directory
```
python3 -m venv ./venv
```
2. Activate the Virtual environment
```
source venv/bin/activate
```
3. Create a database
```
CREATE DATABASE [database name];
```
4. Create a user
```
CREATE USER [username] WITH PASSWORD 'abc123!';
```
5. Grant the user access to the database
```
GRANT ALL PRIVILEGES ON DATABASE [database name] TO [username];
```
6. In the BTRE_APP/settings.py fie, update the following properties under DATABASES
```
NAME: [database name]
USER: [username]
PASSWORD: [password]
```
7. Run Migrations with the following commands
```
# python manage.py makemigrations
# python manage.py migrate
```
8. Create a superuser to access your admin panel
```
python manage.py createsuperuser
```
9. Create static files
```
python manage.py collectstatic
```
10. Run the server
```
python manage.py runserver
```

## Built With

* [Django](https://docs.djangoproject.com/en/3.0/) - Web framework
* [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/) - Web responsiveness and template
* [jquery](https://api.jquery.com/) - JavaScript Library


## Acknowledgments

* Brad Traversy(Django Dev to Deployment)
