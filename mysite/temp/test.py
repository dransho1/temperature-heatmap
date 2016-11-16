from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import json, requests

class Pls():
    def feeds(self):
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
        req = requests.get("https://cloud.kierantimberlake.com/pointelist/api/projects?name=South side",
                headers={'content-type': 'application/json', 'cookie': "token=" + json_load['token']})

        #convert from json
        load = req.json()
        
        ######################################
        # parse the data, and establish sensors and feeds

        #print load

        q = load.get("projects") # dict( list[dict] )
        q = q[0] # now have inner projcet dictionary
        print q.get("feeds")
        #data = load['sensors'] # gets all the sensor-specific data
        #print data
        """for sensor in data:
            print sensor.get('serial') # prints out all serials!

        for s in data:
            print s.get('feeds')"""

    def sensors(self):

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
        req = requests.get("https://cloud.kierantimberlake.com/pointelist/api/sensors",
                headers={'content-type': 'application/json', 'cookie': "token=" + json_load['token']})

        #convert from json
        load = req.json()

        data = load["sensors"]
        for s in data:
            print s.get('serial')


        for s in data:
            print s.get('feeds')

        data = load.get('sensors')[11:]
        print data

p = Pls()
p.feeds()
p.sensors()





