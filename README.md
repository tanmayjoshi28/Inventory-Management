# Inventory-Management
A versatile Inventory management system using Django .

### Install [Django](https://docs.djangoproject.com/en/3.0/intro/install/) 
#### To Run open Terminal :
##### Go to directory in which manage.py is located :
ENTER the follwing stepwise
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### If it is showing error python not defined :
Refer [This](https://geek-university.com/python/add-python-to-the-windows-path/) Article

## To access Admin :
### First create a superuser:
#### Open Terminal :
#### Go to directory in which manage.py is located :
```
python manage.py createsuperuser
```
Follow the prompts and runserver again , add '/admin' to the url
