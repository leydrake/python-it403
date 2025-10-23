from django.shortcuts import render
# pages/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


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

