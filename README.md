# Sign-Up-Form

This is simple sign up form with backend(using Flask) and a database(using PostgreSQL)

## Getting started

These instructions will get you a copy of the project up and running on your local machine for development.

## Prerequisites

To get started you need the following

```
Python installed on your local machine
PostgresSQL installed on your local machine

Flask
Flask-SQLAlchemy
Psycopg2
```

## Creating an environment

You need a virtual environment to manage the dependancies

Open your terminal/cmd and cd to the project folder.
In that that folder create a virtual environment called `env`

#windows

`python -m venv env`

#linux/macOS

`python3 -m venv env`

## Activate the environment

Before you work on the project, activate the corresponding environment:

On the terminal/cmd, open the project in VSCODE `code .`

In vs code open command palette `(View > Command Palette or (Ctrl+Shift+P)).`. Then select the Python: Select Interpreter command:

The command presents a list of available interpreters that VS Code can locate automatically (your list will vary; if you don't see the desired interpreter, see Configuring Python environments). From the list, select the virtual environment in your project folder that starts with `./env or .\env:`

Run Terminal: Create New Integrated Terminal (Ctrl+Shift+` )) from the Command Palette, which creates a terminal and automatically activates the virtual environment by running its activation script.

Note: On Windows, if your default terminal type is PowerShell, you may see an error that it cannot run activate.ps1 because running scripts is disabled on the system. The error provides a link for information on how to allow scripts. Otherwise, use Terminal: Select Default Shell to set "Command Prompt" or "Git Bash" as your default instead.

## Installing

In the virtual environment install the following:

```
pip install flask

pip install Flask-SQLAlchemy

pip install psycopg2


```

## Database

Open pgAdmin on your machine and create a new database 

On `app.py` include your database url on the DB_URL eg `postgresql://postgres:password@127.0.0.1:5432/databasename`. replace the *password* on the url with your own password and the *databasename* with your own database name

```
from flask import Flask,render_template,request,flash,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

# replace with your own postgres url
DB_URL = 'postgresql://postgres:password@127.0.0.1:5432/databasename'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] ='some-secret-string'

db = SQLAlchemy(app)

```

## Running the application

In the vscode terminal, run the app by entering `python3 -m flask run (macOS/Linux)` or `python -m flask run (Windows)`, which runs the Flask development server. The development server looks for app.py by default.









