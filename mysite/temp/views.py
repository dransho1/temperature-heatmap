from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views import View
import json, requests
import pprint

from .models import Sensor, Feed

import kt

# where all the stuff for the web app should be located
class HomeView(View):
    def get(self, request):
        sensor_list = Sensor.objects.order_by('-sensor_name')
        template = loader.get_template('temp/index.html')
        context = {
            'sensor_list': sensor_list,
        }
        output = "test"
        return HttpResponse(template.render(context, request))

    def getdat(self, request):
        json_data = open('temp/static/temp/demodata.json')
        data = json.load(json_data)
        json_data.close()
        return JsonResponse(data, safe=False)

    def getmore(self, request):
        testTemp = kt.get_data()
        r = 0
        t = 70
        #for i in data:
            #Sensor_instance = Sensor.objects.create(sensor_name=r)
        #context = {
            #'data': data,
        #}
        return render(request, 'temp/index.html', {'data': testTemp})