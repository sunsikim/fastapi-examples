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

This project implements simple asynchronous FastAPI application `asyncsql` that sends request to manage post and corresponding comments. 

```text
asyncsql/
|-- __init__.py
|-- models
|   |-- __init__.py
|   |-- comments.py
|   `-- posts.py
|-- schemas
|   |-- __init__.py
|   |-- comments.py
|   `-- posts.py
|-- database.py
|-- routers
|   |-- __init__.py
|   |-- comments.py
|   `-- posts.py
`-- app.py
```

* `models` : codes to define ORM according to data model for the application 
* `schemas` : those models redefined as pydantic base model for data validation
* `database.py` : operations that have to be done in DB side(ex. creating session)
* `routers` : package of modules where endpoints for each entity are defined 
* `app.py` : actual FastAPI application that utilizes components defined above

General order of FastAPI application implementation using async SQL database

1. Define data models(`models`) and data validation schemas(`schemas`)
1. Define async methods for DB utilization(`database.py`)
1. Implement application to be applied on each entitiy as a router(`routers`)
1. Combine routers as a FastAPI application(`app.py`)

Key concepts covered in this demo can be briefly summarized as below.

* Data Validation : what Pydantic does to make sure the right type of data is flowing in and out
* Dependency Injection : programming scheme to decide and create objects on runtime
* SQLAlchemy : ORM-style syntax to correctly define relationship between tables

The application can be tried out by executing following command. 

```shell
uvicorn asyncsql.app:app
```
