from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from RealtorBack.models import RequestRent, RequestImm
from .forms import UserRegisterForm, UserEditForm
from .models import User
from loguru import logger
from django.contrib.auth.models import User as sistemUser

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

    workerrent = []
    for i in RequestRent.objects.all():
        if i.rent.worker == request.user:
            workerrent.append(i)

    workerimm = []
    for i in RequestImm.objects.all():
        if i.imm.worker == request.user:
            workerimm.append(i)

    context = {
        'usernow': user,
        'reqrent': reqrent,
        'reqimm': reqimm,
        'workerrent': workerrent,
        'workerimm': workerimm
    }
    print(workerrent)
    print(workerimm)
    return render(request, 'user/profile.html', context=context)

def cart(request):

    logger.debug('Cart')
    user = User.objects.filter(user=request.user)[0]
    reqrent = RequestRent.objects.filter(user=request.user)
    reqimm = RequestImm.objects.filter(user=request.user)

    context = {
        'usernow': user,
        'reqrent': reqrent,
        'reqimm': reqimm,
    }
    return render(request, 'user/cart.html', context=context)


def cartPaid(request):

    logger.debug('Cart Paid')
    user = User.objects.filter(user=request.user)[0]
    #TODO PAIMENT
    RequestRent.objects.all().delete()
    RequestImm.objects.all().delete()


    context = {
        'usernow': user,
    }
    return render(request, 'user/cartPaid.html', context=context)

def cartItemDelete(request):
    logger.debug('Cart item del')
    try:
        id = int(request.GET.get('id'))
        isRent = (request.GET.get('isRent') == "True")
    except:
        logger.debug('Exception on delete')

    if isRent:
        print(RequestRent.objects.filter(user=request.user)[id])
        RequestRent.objects.filter(user=request.user)[id].delete()
    else:
        RequestImm.objects.filter(user=request.user)[id].delete()
    return redirect('cart')


def profileedit(request):

    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            logger.debug('User edited')
            return redirect('profile')
        else:
            logger.debug('Edit form not valid')

    else:
        form = UserEditForm()

    context = {
        'form': form
    }
    return render(request, 'user/profileedit.html', context=context)


def profiledelete(request):

    # Todo
    
    return render(request, 'user/profileDelete.html')
