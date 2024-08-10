# REST server
A Python REST server for debugging REST APIs.

## Proposal
I am new to REST APIs so I need a way of playing with them and debugging. This will be a REST server made following the [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

Once this is useable, I might convert it to a Python package using my [Python Template](https://github.com/TR33HGR/python-template).

## installed packages
- Flask 3.0.3
- Flask-WTF 1.2.1
- Flask-SQLAlchemy 3.1.1
- Flask-Migrate 4.0.7
- Flask-Login 0.6.3
- Email-Validator 2.2.0
- PyHamcrest 2.1.0

## disabled lints
### pylint
- C0114 missing module docstring
- C0115 missing class docstring
- C0116 missing function docstring

### flake8

### pep8

## Running the server
### Prerequisites
Flask requires you to define a `FLASK_APP` environment variable. I recommend creating a `.env` file and using `python-dotenv`:

- install `python-dotenv` package:
    ```
    pip install python-dotenv
    ```

- create a `.env` file in this folder and add:
    ```
    FLASK_APP=main.py
    ```

### Running
To run the app in developer mode, run:
```
flask run
```

### Shell
To open a shell env for playing with things, you can run:
```
flask shell
```

### Debugging
To run flask in debug mode, either:

-
    ```
    export FLASK_DEBUG=1
    ```

- or add to your `.env` file
    ```
    FLASK_DEBUG=1
    ```

### Error emails
When the app is not in debug mode, it is possible to have it email you when an error occurs.

To make this happen you must define a `MAIL_SERVER`:
- in your shell
    ```
    export MAIL_SERVER=<example.com>
    ```

- or add to your `.env` file
    ```
    MAIL_SERVER=<example.com>
    ```

You also have access to:
- `MAIL_PORT`, default 25
- `MAIL_USE_TLS`, `false` if undefined
- `MAIL_USERNAME`
- `MAIL_PASSWORD`

#### Debugging
You can debug this feature using the SMTP debugging server `aiosmtpd`.

Simply install:
```
pip install aiosmtpd
```

then run:
```
aiosmtpd -n -c aiosmtpd.handlers.Debugging -l localhost:8025
```

and define some variables:
```
export MAIL_SERVER=localhost
export MAIL_PORT=8025
```

## Building
### Database
This app currently has a database for users. Every time the structure of that database changes you will need to rebuild.

To rebuild, run:
```
flask db migrate -m "<some description of the change>"
flask db upgrade
```

#### Clearing the database
You can clear the database by taking advantage of the migration support.

Simply run:
```
flask db downgrade base
flask db upgrade
```

## Testing
To run unit tests, simply run:
```
py -m unittest
```

To specify what test file you want to run, pass it as a module, i.e.:
```
py -m unittest app.tests.test_module
```