Weather
=======

This program monitors the current temperature at a given location over a period of time at user defined intervals.

This is made with the intent of generating data for graphing on hostedgraphite.com and makes use of the weather api and python wrapper found at: https://github.com/ZeevG/python-forecast.io

theweather.py takes 5 command line arguments (for now)

1 - This must be your api key for https://developer.forecast.io/

2 - This must be your api key for hostedgraphite.com

3 - This is whatever name you want to name this specific metric

4 - This is the latitude

5 - Longitude

6 - amount of time in hours you want this to run .. will actually run for half the time

Run command looks like this:
python theweather.py "forecast.io key" "hostedgrapite key" "name of your metric" "latitude" "longitude" "timetorun"

To Do:
======

1. add catch for if intenet connection is lost (like always happens on silly eircom's wifi)
2. add changeable interval time