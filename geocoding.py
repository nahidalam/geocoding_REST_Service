#!flask/bin/python

'''
Author: Nahid Alam
Retrieves Lattitude, Longitude from an address.
RESTful service using Python
'''

from flask import Flask, jsonify
from flask import make_response
from flask import abort
from flask import request
#from urllib.parse import quote
import os
import sys
import json
from pprint import pprint
import requests
from CONFIG import *

app = Flask(__name__)


#This function calls Google Maps or HERE API to find the geocoding data in JSON format
#backup = 0 means using default service, i.e. Google Maps API
#backup = 1 means using HERE API service
def findGeoData(addr, backup):
    addrURL = addr.replace(' ', '+')
    #addrURL = quote(addr)
    if backup == 0:
        #calling Google Maps API
        url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + addrURL + '&key=' + APIKey
    else:
        url = 'https://geocoder.cit.api.here.com/6.2/geocode.json?searchtext='+addrURL+'&app_id='+ MY_APP_ID+ '&app_code='+ MY_APP_CODE+'&gen=8'

    json_data = requests.get(url).json()
    return json_data



#RESTful Service interface
@app.route('/')
def index():
    return "Geocoding RESTful Service"

@app.route('/geocode/api/v1.0/json',methods=['GET'])
def getLatLng():
    if 'address' in request.args:
        addr = request.args['address']
        json_data = findGeoData(addr, 0)

        if json_data['results'] == None: #If Google Maps API is not working, work with HERE API
            json_data_HERE = findGeoData(addr, 1)
            latHERE = json_data_HERE['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Latitude']
            lngHERE = json_data_HERE['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Longitude']
            return jsonify({'Latitude':latHERE, 'Longitude':lngHERE})
        else:
            lat = json_data['results'][0]['geometry']['location']['lat']
            lng = json_data['results'][0]['geometry']['location']['lng']
            return jsonify({'Latitude':lat, 'Longitude':lng})

    else: #URL format invalid
        return make_response(jsonify({'Invalid URI': 'To retrieve lat-lng, paste URL in http://localhost:5000/geocode/api/v1.0/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA format'}), 404)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
