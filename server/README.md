# REST server
A Python REST server for debugging REST APIs.

## Proposal
I am new to REST APIs so I need a way of playing with them and debugging. This will be a REST server made following the [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

Once this is useable, I might convert it to a Python package using my [Python Template](https://github.com/TR33HGR/python-template).

## installed packages
- Flask 3.0.3
- Flask-WTF 1.2.1

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