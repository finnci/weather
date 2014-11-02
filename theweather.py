print('hello!')
import socket
import unirest
import json
import requests
import time
import sys
import forecastio

#assign api keys & metric name
api_key = str(sys.argv[1])
hg_key = str(sys.argv[2])
metricName = str(sys.argv[3])

 #assign latitude, longitude and time to run
lat = sys.argv[4]
lng = sys.argv[5]
timetorun = sys.argv[6]

#initiate stuff
b = 0
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while b < timetorun:
	forecast = forecastio.load_forecast(api_key, lat, lng)
	current = forecast.currently()
	ctemp = current.temperature
	sock.sendto(hg_key + "." + metricName + " " + str(ctemp) + "\n", ("carbon.hostedgraphite.com", 2003))
	print b + "temp is ->" + ctemp
	b = b + 1
	time.sleep(60)


