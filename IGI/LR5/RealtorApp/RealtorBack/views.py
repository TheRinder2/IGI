from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import CommentForm, OfferRentForm, OfferImmForm
from .models import New, FAQ, Vacancion, Rent, Discount, Contact, Comment, Time, Report, Immovables, RequestRent, RequestImm
from datetime import datetime
from django.db.models import Sum, Count
import requests
import pytz
import calendar
from loguru import logger


def about(request):
    return render(request, 'about.html')


def get_weather_data(lat, lon, api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_random_joke():
    url = 'https://official-joke-api.appspot.com/random_joke'

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None


def index(request):
    order = request.GET.get('order', 'asc')  # Получение параметра сортировки из запроса
    elements = Rent.objects.all()
    if order == 'desc':
        elements = Rent.objects.all().order_by('-cost')
    else:
        elements = Rent.objects.all().order_by('cost')
    let = 53.893009
    lon = 27.567444
    api_key = '866a6fbfa627aefa1cdbbcbfcb2e3e90'
    data = []
    data1 = []
    try:
        data = get_weather_data(let, lon, api_key)
        data1 = get_random_joke()
        logger.debug('Api correct')

    except:
        logger.warning('Api warning')

    context = {
        'data': data,
        'data1': data1,
        'elements': elements,
        'order': order,
    }

    return render(request, 'main.html', context)



def registration(request):
    return render(request, 'registration.html')


def news(request):
    new = New.objects.all()
    return render(request, 'news.html', {'new': new})


def faq(request):
    posts = FAQ.objects.all()
    return render(request, 'faq.html', {'posts': posts})


def contacts(request):
    data = Contact.objects.all()
    return render(request, 'contacts.html', {'Contact': data})


def policy(request):
    return render(request, 'policy.html')


def vacancies(request):
    vacancion = Vacancion.objects.all()
    return render(request, 'vacancies.html', {'vacancion': vacancion})

@login_required
def feedback(request):

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            logger.debug('Feedback posted')
        else:
            logger.debug('Rent form not valid')

    else:
        form = CommentForm()

    context = {
        'form': form,
        'comments': reversed(Comment.objects.all()),
    }
    return render(request, 'feedback.html', context=context)


def discount(request):
    discounts = Discount.objects.all()
    return render(request, 'discounts.html', {'discounts': discounts})


def offersRent(request):
    cost = 0
    if request.method == 'POST':
        formrent = OfferRentForm(request.POST)
        if formrent.is_valid():
            selected_ids = map(int, formrent.cleaned_data['options'])
            selected_records = Rent.objects.filter(id__in=selected_ids)
            cost = selected_records.aggregate(total_cost=Sum('cost'))['total_cost']
            logger.debug('Rent accepted')

            for i in selected_records:
                RequestRent.objects.create(rent=i, user=request.user, ready=False)
    else:
        formrent = OfferRentForm()
    content = {
        'form': formrent,
        'rents': Rent.objects.all(),
        'totalcost': cost
    }
    return render(request, 'requestRent.html', content)

def offersImm(request):
    cost = 0
    if request.method == 'POST':
        formimm = OfferImmForm(request.POST)
        if formimm.is_valid():
            selected_ids = map(int, formimm.cleaned_data['options'])
            selected_records = Immovables.objects.filter(id__in=selected_ids)
            cost = selected_records.aggregate(total_cost=Sum('cost'))['total_cost']

            for i in selected_records:
                RequestImm.objects.create(imm=i, user=request.user, ready=False)
    else:
        formimm = OfferImmForm()
    content = {
        'form': formimm,
        'imms': Immovables.objects.all(),
        'totalcost': cost
    }
    return render(request, 'requestImm.html', content)


def userTime(request):

    utc_now = datetime.utcnow().replace(tzinfo=pytz.utc)

    user_timezone = pytz.timezone('Europe/Moscow')
    user_time = utc_now.astimezone(user_timezone)

    data = Time.objects.all().values('name', 'created_at', 'updated_at')

    data_list = []
    for item in data:
        created_at_utc = item['created_at']
        updated_at_utc = item['updated_at']
        item['created_at_user'] = created_at_utc.astimezone(user_timezone).strftime('%d/%m/%Y')
        item['created_at_utc'] = created_at_utc.strftime('%d/%m/%Y')
        item['updated_at_user'] = updated_at_utc.astimezone(user_timezone).strftime('%d/%m/%Y')
        item['updated_at_utc'] = updated_at_utc.strftime('%d/%m/%Y')
        data_list.append(item)

    cal = calendar.HTMLCalendar(calendar.SUNDAY)
    calendar_html = cal.formatmonth(user_time.year, user_time.month)
    logger.debug('User calendar OK')

    context = {
        'user_timezone': user_timezone,
        'user_time': user_time.strftime('%d/%m/%Y %H:%M:%S'),
        'utc_time': utc_now.strftime('%d/%m/%Y %H:%M:%S'),
        'data_list': data_list,
        'calendar_html': calendar_html,
    }

    return render(request, 'time.html', context)


def employee(request):
    # if request.method == 'POST':
    #     text = request.POST.get('comment')
    #     if text != '':
    #         Report.objects.create(text=text, userId=int(request.session.get('user_id')))
    # jobs = Job.objects.all()
    # requests = Request.objects.all()
    #
    # most_frequent = Request.objects.values('JobId').annotate(count=Count('JobId')).order_by('-count').first()
    #
    # most_frequent_id = most_frequent['JobId'] if most_frequent else None
    # most_frequent_count = most_frequent['count'] if most_frequent else 0
    #
    # context = {
    #     'jobs': jobs,
    #     'requests': requests,
    #     'most_frequent_id': most_frequent_id,
    #     'most_frequent_count': most_frequent_count,
    # }
    return render(request, 'employee.html')
