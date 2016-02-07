from django import forms

from .models import SlackInviteRequest

class SlackInviteForm(forms.ModelForm):
    class Meta:
        model = SlackInviteRequest
        fields = '__all__'

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'field', 'id':'slack-email', 'placeholder': "Enter Your Email Address" }),
        required=True,
        error_messages={'invalid': 'You already requested an invite.', 'required': "Please enter an email address."})
