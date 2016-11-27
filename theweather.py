import socket
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
timecompare = 0
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while timecompare < timetorun:
    forecast = forecastio.load_forecast(api_key, lat, lng)
    current = forecast.currently()
    ctemp = current.temperature
    sock.sendto(hg_key + "." + metricName + " " + str(ctemp) + "\n",
                ("carbon.hostedgraphite.com", 2003))
    print str(timecompare) + "temp is ->" + str(ctemp)
    timecompare = timecompare + 1
    time.sleep(30) 
