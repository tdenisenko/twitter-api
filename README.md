# Twitter API App

## Installation
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Running
```bash
source env/bin/activate
python manage.py runserver
```

Note: For Windows use the commands below to activate the virtual environment

CMD:
```bat
.\env\Scripts\activate.bat
```
Powershell:
```ps1
.\env\Scripts\Activate.ps1
```

## Usage

### Get Tweets from Users

To get JSON output of latest tweets from a user:

`http://localhost:8000/users/<username>?limit=<n>`

For example:

http://localhost:8000/users/twitter?limit=5

### Get Tweets by Hashtag

To get JSON output of latest tweets that mentioned a hashtag:

`http://localhost:8000/hashtags/<hashtag>?limit=<n>`

For example:

http://localhost:8000/hashtags/python?limit=10

Parameter `limit` is optional and default limit size is 30.