## Django Polls Application


Assignment: Learn Django by Implementing the Tutorial App
- Made a polls app using python with Django.

by Arisa Pangpeng 6110545678

## Requirements


 The application requires
 * Python 3.6 or newer
 * Django 2.1.2 or newer
 * Python add-on modules as in [requirements.txt](requirements.txt)

## Installing
**You must cloning the Django app** as a zip file and extract the file or clone the repository to your local machine with Terminal :
```
git clone https://github.com/kidstylex/django-polls.git

```

Install required packages :
```
pip install -r requirements.txt 
```
Create database using :
```
py manage.py migrate
```
If you want to create admin user :
```
py manage.py createsuperuser
```

Create `.env` text file in \django-polls and **file must contain** : 'SECRET_KEY, DEBUG, ALLOWED_HOSTS, DB_ENGINE and DB_NAME'

**EXAMPLE**
```
# You can generate SECRET_KEY using : https://djecrety.ir/

SECRET_KEY = 'YOUR_SECRET_KEY'

DEBUG = True/False

ALLOWED_HOSTS = .localhost

DB_ENGINE = 'django.db.backends.sqlite3'

DB_NAME = 'db.sqlite3'
```

## How to run
1. Open Terminal and change current directory to django-polls directory :
```
C:\Users\..\..>cd django-polls
```

2. Typing `py manage.py runserver` on Terminal and you'll get a message like this :

```
C:\Users\..\..\django-polls>py manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
September 16, 2019 - 15:09:04
Django version 2.2.5, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
3. You'll see web server when you go to http://localhost:8000
- admin page: http://localhost:8000/admin
- to vote polls: http://localhost:8000/polls


