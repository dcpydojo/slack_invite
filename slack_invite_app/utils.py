import requests as r
import os

def slack_api_invite_request(email, SLACK_TOKEN, SLACK_URL):
    '''
    param :email: user email requesting slack invite

    returns dictionary confirming invite worked ({u'ok': True})
    '''
    data = {
        'email': email,
        'token': SLACK_TOKEN,
        'set_active': True,
    }

    c = r.post(
        '%s/api/users.admin.invite' % SLACK_URL,
        params=data
    ).json()

    return c


if __name__ == '__main__':
    pass
