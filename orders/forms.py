from django import forms
from django.db.models import fields
from.models import Contact_us


class Contact_usForm(forms.ModelForm):
    class Meta:
        model=Contact_us
        fields=("__all__")
