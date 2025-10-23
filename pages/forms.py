# pages/forms.py
from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'you@example.com'}),
            # 'phone': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
            'message': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Type your message here...'}),
        }
