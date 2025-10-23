# pages/forms.py
from django import forms
from .models import ContactMessage, FeedbackMessage

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


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackMessage
        fields = ['name', 'email', 'subject', 'message', 'rating']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'you@example.com'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Brief subject of your feedback'}),
            'message': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Please share your detailed feedback...'}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
        }
