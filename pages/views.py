from django.shortcuts import render
# pages/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import ContactForm, FeedbackForm


# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # saves to the DB
            messages.success(request, "✅ Message sent successfully!")
            return redirect('contact')  # PRG: prevents duplicate form submissions
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactForm()

    return render(request, "contact.html", {'form': form})

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # saves to the DB
            messages.success(request, "✅ Feedback sent successfully! Thank you for your input.")
            return redirect('feedback')  # PRG: prevents duplicate form submissions
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = FeedbackForm()

    return render(request, "feedback.html", {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Account created successfully! You can now log in.")
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})

