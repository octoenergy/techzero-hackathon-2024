#!/usr/bin/env python3

import os
import json
import httpx

def summary(three_hours):
  # https://www.metoffice.gov.uk/services/data/datapoint/code-definitions
  weather_type = three_hours['W']
  if weather_type == '1':    # Sunny Day
    sun = 2
  elif weather_type == '3':  #  Partly cloudy
    sun = 1
  else:
    sun = 0

  wind = int(three_hours['S'])
  temp = int(three_hours['T'])
  return { "sun": sun, "wind": wind, "temp": temp }

# three hourly forecast multiplied up to half hours for consistency with other data sources
def get_weather_data(location_code=352613):
  api_key = os.environ['DATAPOINT_API_KEY']

  headers = {'Accept': 'application/json'}
  client = httpx.Client()
  request = client.get(f"http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/{location_code}?res=3hourly&key={api_key}", params={}, headers = headers)
  data = request.json()

  by_half_hour = [None] * 54
  # next 24 hours
  forecast = data['SiteRep']['DV']['Location']['Period'][0]['Rep']
  for three_hours in forecast:
    weather = summary(three_hours)
    start = int(three_hours['$']) // 30
    for i in range(start, start + 6):
      by_half_hour[i] = weather
  # add til next day 3am...
  til3 = data['SiteRep']['DV']['Location']['Period'][1]['Rep'][0]
  weather = summary(til3)
  for i in range(48, 48 + 6):
    by_half_hour[i] = weather
  return by_half_hour
