#!/usr/bin/env python

from commands import getoutput
import re, urllib2, webbrowser
import json as simplejson

API_Key = "AIzaSyABpjWBoXU27z9UH-U-ce58-R6MnV20bKs"
query = "https://www.googleapis.com/geolocation/v1/geolocate?key=" + API_Key

# bash command to grab the neighboring wifi data around the laptop
path2WiFi = '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport scan'

# regular expression to match MAC address
macMatch = '([a-fA-F0-9]{2}[:|\-]?){6}'
count = 0

# running network WiFi scan
print "[+] Scanning network"
neighborWiFi = getoutput(path2WiFi)
neighborWiFi = neighborWiFi.split('\n')

# cleaning up bad data  
for line in neighborWiFi:
    a = re.compile(macMatch).search(line)
    if a:
        count +=1
    else:
        neighborWiFi.pop(count)

print "[+] Creating HTML request"
test = { "macAddress": "01:23:45:67:89:AB", "signalStrength": -65 }
locationRequest={
	"version":"1.1.0",
	"request_address":False, 
	"wifiAccessPoints":[ test ]} 

for x in neighborWiFi:
    a = re.compile(macMatch).search(x.split()[1])
    b = re.compile(macMatch).search(x.split()[2])
    if a:
        tempDict = {"mac_address":x.split()[1].replace(":","-"),"signal_strength":abs(int(x.split()[2]))}
        locationRequest["wifiAccessPoints"].append(tempDict)
    elif b:
        tempDict = {"mac_address":x.split()[2].replace(":","-"),"signal_strength":abs(int(x.split()[3]))}
        locationRequest["wifiAccessPoints"].append(tempDict)

print "[+] Sending the request to Google"
data = simplejson.JSONEncoder().encode(locationRequest)
#print repr(data)
response = urllib2.urlopen(query, data).read()
#print url_request
output = simplejson.loads(response)
#   print repr(output)

# prints out the latitude and longitute data returned from Google and opens browser to visually location MAC
print "[+] Google Map"
print "http://maps.google.com/maps?q="+str(output["location"]["latitude"])+","+str(output["location"]["longitude"])
googleMapWebpage = query+str(output["location"]["latitude"])+","+str(output["location"]["longitude"])
webbrowser.open(googleMapWebpage)

