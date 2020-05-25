# Scheduler: micro/base event manager

## Requirements

Tested on Python 3.7.5 Django 3.0
Uses also django-channels and VueJs (served directly via Django, needs Internet connection to fetch related JS libraries).

## Running

* I suggest to create virtual environment, perfectly based on python 3.7 and activate to work in it.
* Fetch repo: `git clone https://github.com/kocki/scheduler.git`
* Go into project directory: `cd scheduler`
* Install dependencies: `pip install -r requirements/prod.txt`. Use `dev` instead of `prod` if you need developer stack.
* Run project: `./manage.py runserver`
* Open http://localhost:8000/ in browser to open Scheduler.
* Open http://localhost:8000/admin/ to access to django admin panel.

## Functionality

* Can add, update and remove events. It's for demo purpose only so lot of functionalites is missed (e.g. better date/time input field/picker), but it works.
* Open Scheduler to observe than add event using django admin, other window with Scheduler or django shell. New event should appear in browser opened to observe.
* Movie preview available here: https://youtu.be/yZed_ei0lII

##

* Security layer is completely skipped.
* There is no tests.
* Some ToDos marked in code.

## Usage comments

1. Events are categorised by **event type**. It is flexible to configure via django admin panel: http://localhost:8000/admin/events/eventtype/
2. There is **event data** field designed tu use for any setup/configuration/simple data transfering reasons. To keep this project simplest it is text field, but it seems to be better to implement it as JSON field. It is not included in Scheduler Add/Update forms, becuse it is intended to be used by any machine way.
