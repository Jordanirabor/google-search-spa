## Introduction

This is a Google search clone SPA powered by JavaScript's Vue and Python's flask.

## Requirements
* Python
* Virtualenv 
* Flask

## Getting started
1. Clone the project to your machine ```[git clone https://github.com/Jordanirabor/google-search-spa]```
2. Navigate into the diretory ```[cd google-search-spa]```
3. Source the virtual environment ```[source .venv/bin/activate]```
4. Install the dependencies ```[pip install flask]```
5. Navigate into the Vue project directory ```[cd spa]```
5. Install Vue and the Node dependencies ```[npm install]```

## Run the application
You will need to have two terminals pointed to the appropraite directories to run the backend and frontend servers for this application.
1. Run this command to start the backend server in the ```[google-search-spa]``` directory: ```[python app.py]``` (You have to run this command while you are sourced into the virtual environment)
2. Run this command to start the Vue frontend server in the ```[google-search-spa/spa]``` directory: ```[npm start]``` (This will build and start the Vue frontend on the URL adddress [localhost:8080](http://localhost:8080))

## Built With

* [Vuejs](https://vuejs.org/) - This is a Progressive JavaScript framework
* [Python](https://www.python.org/) - This is a programming language that lets you work quickly and integrate systems more effectively
* [Flask](http://flask.pocoo.org/) - This is a microframework for Python based on Werkzeug, Jinja 2 and good intentions