# code for accessing the kt web server
import json, requests, time


def get_data():
    # page for loading KT data (similar to getdata request for API)
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
    ts = time.time()


    # .../api/samples?chart=243  --> North side, all data forever. last stamp most recent
    # .../api/samples?chart=96   --> South side

    # sensors?fields[]=feeds
    # sensors?fields[]=serial
    # samples?chart=243
    # channels?fields[]=lastsampledata
    # feeds?fields[]=channels
    # feeds?fields[]=name
    # projects/96/
    # samples?channel=1&last=10
    req = requests.get('https://cloud.kierantimberlake.com/pointelist/api/feeds?fields[]=name',
            headers={'content-type': 'application/json', 'cookie': "token=" + json_load['token']})

    #convert from json
    load = req.json()
    #return load
    #print load    ######################################
    #t = load["t"]
    #print json.dumps(load, sort_keys=True, indent=4, separators=(',',': '))

    # channel 2700 == feed 1147 == "Feed16_3B65911F00000052" == sensor 945 == "3B65911F00000052"

    # try hard-coded sample
    #channel 2700
    #feed 1147
    #last data is 24.3125 at 1481852400   --> checks out
    req = requests.get('https://cloud.kierantimberlake.com/pointelist/api/samples?channel=2700&last=10',
            headers={'content-type': 'application/json', 'cookie': "token=" + json_load['token']})

    #convert from json
    load = req.json()
    #return load
    #print load    ######################################
    #t = load["t"]
    data = load["samples"]
    #print json.dumps(data, sort_keys=True, indent=4, separators=(',',': '))
    # parse the data, and establish sensors and feeds
    #for sensor in load:
    #    print sensor #prints sensors
    ######################################
    # make a dictionary of sensors & temperature, sensors & humidity.
    # need to create a model for each sensor, set sensor model internal temperature
    sensors = {}
    #for point in data:
        #if not point["channel"] in sensors:
            #sensors[point["channel"]] = [point["d"]]
        #else:
            #sensors[point["channel"]].append(point["d"])
    last = data[0]
    lastTemp = last["d"]
    #print json.dumps(last, sort_keys=True, indent=4, separators=(',',': '))
    print lastTemp



#get_data()