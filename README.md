# Flask RESTx Template

## Create Virtual Environment

```bash
python3 -m venv venv
```

## Activate Virtual Environment

```bash
source venv/bin/activate
```

## Install Required Packages

```bash
pip install -r requirements.txt
```

## Run Application

```bash
python manage.py run
```

## Test

You can visit [http://127.0.0.1:5000/docs](http://127.0.0.1:5000/docs) to check if things are okay or not.

## Database migration

step1: Activate your venv

step2: `export FLASK_APP=src/__init__.py`

step3: 
```bash
flask db stamp head  # To set the revision in the database to the head.
flask db migrate -m "<migration message (optional)>"  # To detect automatically all the changes.
flask db upgrade  # To apply all the changes.
```
