## TelegramLogger

TelegramLogger is a telegram bot that logs the conversation to a database. The bot has 3 simple commands

* `/start` which enables the logging for the conversation
* `/stop` which interrupts the logging for the conversation
* `/chatid` which return ad identifier for the conversation

TelegramLogger provide two different ways to read the data stored in the database:

 1. Through an API endpoint, which accept POST requests containing form-data. The minimum required parameter is the
    `chat_id`. Optional parameters are the `user_id` and the `date`. The endpoint can be found at the address
    /chat-messages

 2. Through a user interface (which uses the above API endpoint) which can be found at the root url of the project.

### Setup

Clone the repository

```git clone https://github.com/stefanomunarini/telegram_logger.git```

`cd` into the project directory and create a virtual environment.

Install all the requirements

```pip install -r requirements.txt```

Create a postgres database and name it `telegram_logger`

Run the initial migrations

```python manage.py migrate```

Run the server

```python manage.py runserver```