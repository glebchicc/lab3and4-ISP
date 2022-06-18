from django.contrib.auth import authenticate, login, logout
from django.forms import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .forms import CityChooseForm, UserRegistrationForm, LoginForm
from .models import show_buses


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CityChooseForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if form.cleaned_data['select'] != form.cleaned_data['select2']:
                return HttpResponseRedirect(
                    '/route/' + form.cleaned_data['select'] + '-' + form.cleaned_data['select2'])

    else:
        form = CityChooseForm()

    return render(request, 'hello/city_select.html', {'form': form})


def borisov_minsk(request):
    if request.user.is_authenticated:
        nearest_buses = []
        for bus in show_buses():
            if bus.find_short_departure() == "Борисов":
                nearest_buses.append(bus)
        return render(request, 'hello/borisov-minsk.html', {'nearest_buses': nearest_buses})
    else:
        return HttpResponseRedirect('/login/')



def minsk_borisov(request):
    if request.user.is_authenticated:
        nearest_buses = []
        for bus in show_buses():
            if bus.find_short_departure() == "Минск":
                nearest_buses.append(bus)
        return render(request, 'hello/minsk-borisov.html', {'nearest_buses': nearest_buses})
    else:
        return HttpResponseRedirect('/login/')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'hello/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'hello/register.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return forms.ValidationError('Данный аккаунт деактивирован.')
            else:
                return forms.ValidationError('Неправильный логин или пароль.')
    else:
        form = LoginForm()
    return render(request, 'hello/login.html', {'form': form})


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponse("Не зашел")
