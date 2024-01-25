# Asynchronous FastAPI Application for SQL Database 

Codes are scripted and tested on Apple M2 silicon machine.

```shell
python3 --version  # Python 3.10.13
```

## Environment

Clear existing virtual environment if needed, and then create one.

```shell
if [ -d $PWD/venv ]; then
  rm -rf $PWD/venv
fi

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Project

This project implements simple async FastAPI application `asyncsql` that sends request to manage post and corresponding comments. 

```text
asyncsql/
|-- __init__.py
|-- database.py
|-- models
|   |-- __init__.py
|   |-- comments.py
|   `-- posts.py
|-- schemas
|   |-- __init__.py
|   |-- comments.py
|   `-- posts.py
|-- routers
|   |-- __init__.py
|   |-- comments.py
|   `-- posts.py
`-- app.py
```

* `database.py` : operations that have to be done in DB side(ex. creating session)
* `models` : codes to define ORM according to data model for the application 
* `schemas` : those models redefined as pydantic base model for data validation
* `routers` : package of modules where endpoints for each entity are defined 
* `app.py` : actual FastAPI application that utilizes components defined above
