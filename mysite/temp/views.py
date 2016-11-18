from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from django.template import loader
import json, requests

from .models import Sensor, Feed

# where all the stuff for the web app should be located

def index(request):
    sensor_list = Sensor.objects.order_by('-sensor_name')
    template = loader.get_template('temp/index.html')
    context = {
        'sensor_list': sensor_list,
    }
    output = "test"
    return render(request, 'temp/index.html', context)

def getdat(request):
    json_data = open('temp/static/temp/demodata.json')
    print 'in getdat'
    #data1 = json.load(json_data) # error here
    hm = {}
    ol = {}
    vf = {}
    pp = {}
    print 'load data'
    data = json.load(json_data)
    print 'loaded data is: ', data

    json_data.close()
    return JsonResponse(data, safe=False)
    ########################################
    # sending authorization and getting keys

    #prepare dictionary
    auth = {"email": "chris.carper@atelierten.com", "password": "A10green"}

    #convert dictionary to json
    json_data = json.dumps(auth)

    #make post request for authorization
    #if successful, req will be authorization token
    req = requests.post('https://cloud.kierantimberlake.com/pointelist/api/api-token-auth/',
            data=json_data,
            headers={'content-type': 'application/json'})

    #convert from json to dictionary
    json_load = req.json()

    #make request for data
    #this specific request would take the last ten results from chart 93
    req = requests.get('https://cloud.kierantimberlake.com/pointelist/api/sensors',
            headers={'content-type': 'application/json', 'cookie': "token=" + json_load['token']})

    #convert from json
    load = req.json()
    
    ######################################
    # parse the data, and establish sensors and feeds

    for s in load:
        print s

    ######################################
    # 

    









    return HttpResponse(template.render(context, request))