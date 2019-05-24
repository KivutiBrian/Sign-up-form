# Sign-Up-Form

This is simple sign up form with backend(using Flask) and a database(using PostgreSQL)

## Getting started

These instructions will get you a copy of the project up and running on your local machine for development.

### Prerequisites

To get started you need the following

```
Python installed on your local machine
PostgresSQL installed on your local machine

Flask
Flask-SQLAlchemy
Psycopg2
```

### Creating an environment

You need a virtual environment to manage the dependancies

Open your terminal/cmd and cd to the project folder.
In that that folder create a virtual environment called `env`

#windows

`python -m venv env`

#linux/macOS

`python3 -m venv env`

### Activate the environment

Before you work on the project, activate the corresponding environment:

On the terminal/cmd, open the project in VSCODE `code .`

In vs code open command palette `(View > Command Palette or (Ctrl+Shift+P)).`. Then select the Python: Select Interpreter command:

The command presents a list of available interpreters that VS Code can locate automatically (your list will vary; if you don't see the desired interpreter, see Configuring Python environments). From the list, select the virtual environment in your project folder that starts with `./env or .\env:`

Run Terminal: Create New Integrated Terminal (Ctrl+Shift+` )) from the Command Palette, which creates a terminal and automatically activates the virtual environment by running its activation script.

Note: On Windows, if your default terminal type is PowerShell, you may see an error that it cannot run activate.ps1 because running scripts is disabled on the system. The error provides a link for information on how to allow scripts. Otherwise, use Terminal: Select Default Shell to set "Command Prompt" or "Git Bash" as your default instead.








