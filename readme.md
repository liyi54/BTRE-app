# Property Listing Web App with Django

A Real Estate listing platform with an admin panel

* [Live URL](https://vast-harbor-23833.herokuapp.com/)

## Getting Started

These instructions will get you a copy of the project up and running on a remote heroku server.

### Prerequisites

```
asgiref==3.2.5
certifi==2020.6.20
chardet==3.0.4
cloudinary==1.22.0
Django==3.0.4
django-cloudinary-storage==0.3.0
gunicorn==20.0.4
idna==2.10
Pillow==7.0.0
psycopg2==2.8.4
psycopg2-binary==2.8.4
pytz==2019.3
requests==2.24.0
six==1.15.0
sqlparse==0.3.1
urllib3==1.25.10
whitenoise==5.2.0

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
3. Create a heroku app

4. Install cloudinary and postgresdb as add-ons

5. Edit and update the settings.py file

6. Run Migrations with the following commands
```
# python manage.py makemigrations
# python manage.py migrate
```
7. Create static files
```
python manage.py collectstatic
```
8. Push to the heroku server
```
git push heroku master
```
9. Create a superuser to access your admin panel
```
heroku python manage.py createsuperuser
```

## Built With

* [Django](https://docs.djangoproject.com/en/3.0/) - Web framework
* [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/) - Web responsiveness and template
* [jquery](https://api.jquery.com/) - JavaScript Library


## Acknowledgments

* Brad Traversy(Django Dev to Deployment)
