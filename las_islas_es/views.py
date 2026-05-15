from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, ContactForm, CommentForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .models import CardText, Places, Comment


# Create your views here.
def index(request):
    return render(request, 'index.html')


def info(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been submitted")
            return redirect('index')
        else:
            messages.error(request, "Correct the areas below")
    return render(request, 'info.html', {'active_tab': 'info', 'form': form})


def register(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            messages.success(
                request, f"Account created for {user.username}! You can log in."
            )
            return redirect('index')
        else:
            messages.error(request, "Please correct the errors below.")

    return render(request, 'register.html',
                  {'active_tab': 'register', 'form': form})


def user_login(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"You are logged in as {user.username}")
            return redirect('index')
        else:
            messages.error(request, f"Check login details are correct")
    return render(request, 'login.html', {'active_tab': 'login', 'form': form})


def user_logout(request):
    return render(request, 'logout.html', {'active_tab': 'logout'})


def confirm_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')
    return render(request, 'confirm-logout.html', {'active_tab': 'confirm-logout'})


def destinations(request, pk):
    card = get_object_or_404(CardText, pk=pk)
    return render(request, 'destinations.html', {'active_tab': 'destinations',
                                                 'card': card})


def destinations_details(request, pk):
    card = get_object_or_404(CardText, id=pk)
    places = Places.objects.filter(card=card)

    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        place_id = request.POST.get('place_id')
        place = get_object_or_404(Places, id=place_id)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.places = place
            comment.save()
            return redirect('destinations-details', pk=card.pk)
        
    comments = Comment.objects.filter(places__card=card).order_by('created_at')
    return render(request, 'destinations-details.html',
                   {'active_tab': 'destinations-details',
                    'card': card,
                    'places': places,
                    'comments': comments,
                    'form': form})