# Django2SimpleBlog

[![Build Status](https://travis-ci.org/Tony133/Django2SimpleBlog.svg?branch=master)](https://travis-ci.org/Tony133/Django2SimpleBlog)

Simple Example Blog with Django 2.0

## Create Virtual Environment

```
    $ python -m venv myvenv or python3 -m venv myvenv
```
## Start up Environment

```
    $ source myvenv/bin/activate
```
## Install Django

```
    $ pip install django or pip install django==2.0
```

## Getting Migrate Table on database

```
    $ python manage.py migrate
```

## Create SuperUser for Admin

```
    $ python manage.py createsuperuser
```

## Getting Fixtures

```
    $ python manage.py loaddata data.json 
```

## Run App
```
    $ python manage.py runserver
