# Checkers
This text you see here is *actually* written in Markdown! To get a feel for Markdown's syntax, type some text into the left window and watch the results in the right.
### Tech

* [ADjango] - A high-level Python Web framework that encourages rapid development and clean, pragmatic design!
* [pipenv] - Python Development Workflow for Humans.
* [Twitter-Bootstrap] - great UI boilerplate for modern web apps


### Installation

Chekers requires [Python 3.7] to run.
you can install it as follows:
```sh
$ sudo apt install pipenv
or
$ pip  install pipenv
```

### Create virtualenv
```sh
$ pipenv --python 3.7
$ pipenv shell
```
Install the dependencies and devDependencies and start the server.

### installing dependencies
locate Pipfile, run the the following, inside the same directory
```sh
$ pipenv install
```
 # or
 locate requirements.txt, run the the following, inside the same directory

```sh
 $ pipenv install -r requirements.txt 
```
### Runnging the server
locate manage.py, run the the following, inside the same directory

```sh
 $ python manage.py runserver
```

### Making migrations 
locate manage.py, run the the following, inside the same directory
```sh
 $ python manage.py makemigrations
```
```sh
 $ python manage.py migrate
   python manage.py migrate
```
