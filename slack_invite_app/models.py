from __future__ import unicode_literals

from django.db import models

# Create your models here.


class SlackInviteRequest(models.Model):
    """
    User-uploaded image file
    """
    email = models.EmailField('Emails requested', unique=True)
    timestamp = models.TimeField('Time requested', auto_now_add=True)
    
    def __unicode__(self):
        return self.email