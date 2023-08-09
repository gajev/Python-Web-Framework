from django import forms

from diary.partners.models import PartnerUser


class PartnerUserForm(forms.ModelForm):
    class Meta:
        model = PartnerUser
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'profile_picture']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'phone_number': 'Mobile',
            'email': 'Email',
            'profile_picture': 'Enter URL',
        }
