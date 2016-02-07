from django.contrib import admin

# Register your models here.

from .models import SlackInviteRequest


class SlackInviteRequestAdmin(admin.ModelAdmin):
    list_display = ('email', 'timestamp')

admin.site.register(SlackInviteRequest, SlackInviteRequestAdmin)