from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from RealtorBack.models import RequestRent, RequestImm
from .forms import UserRegisterForm, UserEditForm
from .models import User
from loguru import logger


def register(request):
    if request.method == 'POST':
        logger.debug('User register POST')

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data.get('phone')[0])
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user=user)
            logger.debug("User registration OK")
            return redirect('home')
    else:
        logger.debug('User register GET')
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context=context)


def profile(request):
    logger.debug('User profile')

    user = User.objects.filter(user=request.user)[0]
    reqrent = RequestRent.objects.filter(user=request.user)
    reqimm = RequestImm.objects.filter(user=request.user)
    context = {
        'usernow': user,
        'reqrent': reqrent,
        'reqimm': reqimm
    }
    return render(request, 'user/profile.html', context=context)


def profileedit(request):

    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            logger.debug('User edited')
            context = {
                'form': form
            }
            return render(request, 'user/profile.html', context=context)
        else:
            logger.debug('Edit form not valid')

    else:
        form = UserEditForm()

    context = {
        'form': form
    }
    return render(request, 'user/profileedit.html', context=context)
