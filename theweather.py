print('hello!')
import socket
import unirest
import json
import requests
import time
import sys
import forecastio


api_key = str(sys.argv[1])
hg_key = str(sys.argv[2])
metricName = str(sys.argv[3])

lat = 53.3478
lng = 6.2597

b = 0
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while b < 120:
	forecast = forecastio.load_forecast(api_key, lat, lng)
	current = forecast.currently()
	ctemp = current.temperature
	sock.sendto(hg_key + "." + metricName + " " + str(ctemp) + "\n", ("carbon.hostedgraphite.com", 2003))
	print b
	b = b + 1
	time.sleep(60)


