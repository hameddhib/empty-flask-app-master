# Empty Flask App

This is an empty [Flask][] app, using [Blueprints][], [SQLAlchemy][] 

## Structure

```
.
├── config.py
├── app
│   ├── __init__.py
│   └── user├── user.py
│           └── __init__.py
│           └── model.py
│          
├── requirements.txt
└── run.py
```

## Quick start

Install python version 2.7 or 3

Navigate to flask folder:

    cd empty-flask-app-master

Install requirements:

    pip install -r requirements.txt

## Running app

To start develoment server, run:

    ./run.py

Navigate to:

    http://localhost:5000/user
