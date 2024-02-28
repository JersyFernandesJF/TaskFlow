TaskFlow

# Introduction

The goal of this project is to provide minimalistic django project template that everyone can use, which _just works_ out of the box and has the basic setup you can expand on. 

Template is written with django 1.11 and python 3 in mind.

<img width="1440" alt="Captura de ecrã 2024-02-28, às 11 46 14" src="https://github.com/JersyFernandesJF/TaskFlowAPI/assets/102835855/07328952-206c-4369-9dba-18cc251e06c0">

### Main features

* Separated dev and production settings

* Example app with custom user model

* Bootstrap static files included

* Procfile for easy deployments

* Separated requirements files

* Postgres by default if no env variable is set

# Usage

To use this template to start your own project:

### Postgres

 You will need have install on your machine Postgres and create after clone the .env file.
 
 #To install Postgres
 
  https://www.postgresql.org/download/

  #Create a .env file and add
  
  SECRET_KEY=django-insecure-728k0bs%91o$^sp%aa_ji@2fmtwpdk7r1na#*$%l2+%)7tnpo3
  DB_NAME=taskflow
  DB_USER=postgres
  DB_PASSWORD=Ii13a2019
  DB_HOST=localhost
  DB_PORT=5432

### Existing virtualenv

If your project is already in an existing python3 virtualenv first install django by running

    $ pip install django
    
And then run the `django-admin.py` command to start the new project:

    $ django-admin.py startproject \
      --template=https:[//github.com/nikola-k/django-template/zipball/master](https://github.com/JersyFernandesJF/TaskFlowAPI) \
      --extension=py,md \
      <TaskFLow>
      
### No virtualenv

This assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages.

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

If you don't have django installed for python 3 then run:

    $ pip3 install django
    
And then:

    $ python3 -m django startproject \
      --template=https:[//github.com/nikola-k/django-template/zipball/master](https://github.com/JersyFernandesJF/TaskFlowAPI) \
      --extension=py,md \
      TaskFlow
      
      
After that just install the local dependencies, run migrations, and start the server.

{% endif %}

# TaskFlow

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/USERNAME/{{ project_name }}.git](https://github.com/JersyFernandesJF/TaskFlowAPI)
    $ cd TaskFlow
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements/local.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
