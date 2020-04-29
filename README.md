# Api-fetcher

requirements:
-----------------
  - python >= 3.6
  - virtualenv
------------------

* first clone the repo:
  - https://github.com/motaz-hejaze/Api-fetcher.git


* cd into cloned folder:
  - cd Api-fetcher

* create virtual environmet:
  - virtualenv venv -p python3.6
  
* activate your virtual environment:
  - source venv/bin/activate (linux)

* install required python packages:
  - pip install -r requirements.txt

* create database and tables:
  - cd project/
  - python manage.py makemigrations
  - python manage.py migrate

* create superuser:
  - python manage.py creasuperuser

* runserver:
  - python manage.py runserver

* within your browser , go to http://127.0.0.1:8000/
