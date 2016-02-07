from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic.edit import ModelFormMixin
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from .models import SlackInviteRequest
from .forms import SlackInviteForm
from .utils import slack_api_invite_request
# Create your views here.

import os
from .settings import SLACK_TOKEN, SLACK_URL, SLACK_TEAM_NAME

slack_context = {
    'SLACK_TOKEN' : os.environ.get('SLACK_TOKEN', SLACK_TOKEN),
    'SLACK_URL': os.environ.get('SLACK_URL', SLACK_URL),
    'SLACK_TEAM_NAME': os.environ.get('SLACK_TEAM_NAME', SLACK_TEAM_NAME),
    }

if '' in slack_context.values(): ### in one value isn't set
    raise ImproperlyConfigured('slack_invite_app.settings: Set all values here or with heroku:config.')

class SlackInvite(CreateView):
    """docstring for SlackInvite """
    template_name = 'slack_inviter.html'
    form_class = SlackInviteForm
    success_url = reverse_lazy('slack_invite_success')
    model = SlackInviteRequest

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            email = form.cleaned_data['email']
            slack_api_invite_request(email, SLACK_TOKEN, SLACK_URL)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        """
        If an object has been supplied, inject it into the context with the
        supplied context_object_name name.
        """
        context = {}
        if self.object:
            context['object'] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        context.update(slack_context)

        return super(ModelFormMixin, self).get_context_data(**context)

class SlackSuccess(TemplateView):
    """docstring for SlackSuccess"""
    template_name = 'slack_success.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context.update(slack_context)
        return self.render_to_response(context)
        


