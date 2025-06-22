from django import forms
from .models import Contact
import re

class ContactForm(forms.ModelForm):
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput)
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' Enter Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ' Enter Your Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' Enter Your Phone'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': ' Enter Your Message', 'style': 'height: 250px;'}),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(r'^\+?\d{7,15}$', phone):
            raise forms.ValidationError("Enter a valid phone number.")
        return phone

  

    def clean_honeypot(self):
        data = self.cleaned_data.get('honeypot')
        if data:
            raise forms.ValidationError("Spam detected.")
        return data


    
