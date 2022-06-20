from django.contrib.auth import authenticate, login, logout
from django.forms import forms
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect
import logging
import asyncio
from asgiref.sync import sync_to_async

logger = logging.getLogger(__name__)

from .forms import CityChooseForm, UserRegistrationForm, LoginForm, BusForm
from .models import show_buses, generate_buses, Bus


def index(request):
    logger.info("Main page")
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
    logger.info("Borisov-Minsk buses page")
    if request.user.is_authenticated:
        nearest_buses = []
        if show_buses().count() < 3:
            generate_buses()
        for bus in show_buses():
            if bus.find_short_departure() == "Борисов":
                nearest_buses.append(bus)
        return render(request, 'hello/borisov-minsk.html', {'nearest_buses': nearest_buses})
    else:
        return HttpResponseRedirect('/login/')


def minsk_borisov(request):
    logger.info("Minsk-Borisov buses page")
    if request.user.is_authenticated:
        nearest_buses = []
        if show_buses().count() < 3:
            generate_buses()
        for bus in show_buses():
            if bus.find_short_departure() == "Минск":
                nearest_buses.append(bus)
        return render(request, 'hello/minsk-borisov.html', {'nearest_buses': nearest_buses})
    else:
        return HttpResponseRedirect('/login/')


def register(request):
    logger.info("Registration page")
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
    logger.info("Login page")
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
                    raise forms.ValidationError('Данный аккаунт деактивирован.')
            else:
                raise forms.ValidationError('Неправильный логин или пароль.')
    else:
        form = LoginForm()
    return render(request, 'hello/login.html', {'form': form})


def user_logout(request):
    logger.info("Logout page")
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect('/')


def bus_list(request):
    if request.user.is_superuser:
        logger.info("Admin list page")
        if show_buses().count() < 3:
            generate_buses()
        context = Bus.objects.order_by("departure_time")
        return render(request, "hello/bus_list.html", {'bus_list': context})


def bus_form(request, id=0):
    if request.user.is_superuser:
        if request.method == "GET":
            if id == 0:
                form = BusForm()
            else:
                bus = Bus.objects.get(pk=id)
                form = BusForm(instance=bus)
                logger.info('Bus updated')
            return render(request, "hello/bus_form.html", {'form': form})
        else:
            if id == 0:
                form = BusForm(request.POST)
            else:
                bus = Bus.objects.get(pk=id)
                form = BusForm(request.POST, instance=bus)
            if form.is_valid():
                logger.info('Bus created')
                form.save()
            return redirect('/crud/list')
    else:
        return HttpResponseNotFound()


def async_delete(request, id):
    asyncio.run(async_bus_delete(id))
    return redirect('/crud/list')


@sync_to_async
def bus_delete(request, id):
    bus = Bus.objects.get(pk=id)
    bus.delete()


async def async_bus_delete(id):
    task1 = asyncio.create_task(bus_delete(id))
    task2 = asyncio.create_task(delete_print_log(id))
    await asyncio.gather(task1, task2)


@sync_to_async
def delete_print_log(id):
    logger.info("Delete bus page ", id)
