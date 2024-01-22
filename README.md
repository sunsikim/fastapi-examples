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
|-- app.py
|-- database.py
|-- models.py
`-- schemas.py
```

* [models.py](https://github.com/sunsikim/fastapi-examples/blob/sql/asyncsql/models.py) : codes to define ORM according to data model required to implement the application 
* [schemas.py](https://github.com/sunsikim/fastapi-examples/blob/sql/asyncsql/schemas.py) : those models redefined as pydantic base model for data validation
* [database.py](https://github.com/sunsikim/fastapi-examples/blob/sql/asyncsql/database.py) : utility functions to implement actions of database during connection
* [app.py](https://github.com/sunsikim/fastapi-examples/blob/sql/asyncsql/app.py) : actual FastAPI application that utilizes components defined above