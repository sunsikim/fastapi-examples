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
