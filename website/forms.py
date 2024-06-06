from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Message


class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'mobile', 'message']
        labels = {
            'name': _('Name'),
            'mobile': _('Mobile Number'),
            'message': _('Message'),
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
