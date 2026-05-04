from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')


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
