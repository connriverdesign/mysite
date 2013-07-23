from django.shortcuts import render
from django.http import HttpResponse
import datetime


def hours_ahead(request, hours_offset):
    hour_offset = int(hours_offset)
    next_time = datetime.datetime.now() + datetime.timedelta(hours=hour_offset)
    return render(request, 'hours_ahead.html', {'hour_offset': hour_offset, 'next_time': next_time})


def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})


def hello(request):
    return HttpResponse("Hello world!")