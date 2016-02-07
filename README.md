# Django Slack Invite App - Heroku Ready

### Based Upon [Heroku Django 1.9 Template](https://github.com/heroku/heroku-django-template)

## Features

- All the heroku-django-template goodness... Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Email validation - only accepts fully formed email addresses
- Checks for Multiple Invite Requests - will only send out one invite per email
- Django logs all invite requests -  All are timestamped and easily accessible from admin.

## How to Use

To use this project, follow these steps:

In slack_invite_app.settings, add your Slack information:

    SLACK_URL = '' ### your slack team url (ex: dcpythondojo.slack.com)
    SLACK_TEAM_NAME = '' ### your community or team name to display on join page.
    SLACK_TOKEN = '' ### access token of slack. You can generate it in https://api.slack.com/web#auth. You should generate the token in admin user, not owner. If you generate the token in owner user, missing_scope error will be occurred.

## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master

    $ heroku run python manage.py migrate

## To Create a Superuser to log into the Admin

    $ heroku run python manage.py createsuperuser

## Optional Advanced - Set Your Slack Token Directly in Heroku

    $ heroku config:set SLACK_TOKEN=[Put your slack token here]




