# RESTful Service for Geocoding

##### This program take an address as input and returns the Lattitude and Longitude as the output. 

## How to Run:

Assuming you are running in a Mac environment

1. Download the code in YOUR_DIRECTORY
2. $cd YOUR_DIRECTORY
3. $ virtualenv flask
4. $ flask/bin/pip install flask
5. $ flask/bin/pip install requests
6. Make sure you have the right permission for the service $sudo chmod a+x geocoding.py
7. $ ./geocoding.py

This should run the service in localhost port 5000

## How to User the Service API:

Paste below link in your browser

#### http://localhost:5000/geocode/api/v1.0/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA

You should see an output like below

#### {
  #### "Latitude": 37.4224082, 
  #### "Longitude": -122.0856086
#### }
