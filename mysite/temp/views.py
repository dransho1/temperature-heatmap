from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Sensor, Feed

def index(request):
    sensor_list = Sensor.objects.order_by('-sensor_name')
    template = loader.get_template('temp/index.html')
    context = {
        'sensor_list': sensor_list,
    }
    return HttpResponse(template.render(context, request))