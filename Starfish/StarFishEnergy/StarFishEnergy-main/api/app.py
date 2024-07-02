import json
import datetime
import requests
import openmeteo_requests
import requests_cache
import pandas as pd
import modal
from modal import App, web_endpoint
import retry_requests

app = App("starfish", image=modal.Image.debian_slim().pip_install(
    "requests",
    "openmeteo_requests",
    "requests_cache",
    "pandas",
    "retry_requests"
))


@app.function()
@web_endpoint(method="GET")
def get_coords(postcode: str):
    # Return latitude and longitude for a UK postcode
    request_body = f"https://api.postcodes.io/postcodes/{postcode}"
    location = requests.get(request_body)
    longitude = location.json()['result']['longitude']
    latitude = location.json()['result']['latitude']
    return {"latitude": latitude, "longitude": longitude}


def __weather_parser(latitude: float, longitude: float, days: int):
    openmeteo = openmeteo_requests.Client()
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": ["temperature_2m", "cloud_cover", "rain"],
        "forecast_days": days
    }
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]
    # Process hourly data. The order of variables needs to be the same as requested.
    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
    hourly_cloud_cover = hourly.Variables(1).ValuesAsNumpy()
    hourly_rain = hourly.Variables(2).ValuesAsNumpy()

    hourly_data = {"date": pd.date_range(
        start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
        end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
        freq=pd.Timedelta(seconds=hourly.Interval()),
        inclusive="left"
    ), "temperature_2m": hourly_temperature_2m, "cloud_cover": hourly_cloud_cover, "rain": hourly_rain}
    hourly_dataframe = pd.DataFrame(data=hourly_data).set_index('date')
    result = hourly_dataframe.to_json(orient="index")
    parsed = json.loads(result)
    return parsed


def __weather(latitude: float, longitude: float, days: int):
    result = __weather_parser(latitude, longitude, days)
    return result


@app.function()
@web_endpoint(method="GET")
def get_weather(latitude: float, longitude: float, days: int):
    result = __weather_parser(latitude, longitude, days)
    return result


def __battery_capacity():
    # Example could work with the Tesla powerwall API client https://github.com/jrester/tesla_powerwall?tab=readme-ov-file#readme
    # charge = powerwall.get_energy()
    # capacity = powerwall.get_capacity()
    charge = 12  # kWh
    capacity = 13  # kWh
    if charge / capacity > 0.7:
        status = 'high'
    else:
        status = 'low'
    return status


def __weather_rating(weather_json):
    weather_df = pd.DataFrame(weather_json).T
    if weather_df["cloud_cover"].describe(include='all').loc['50%'] > 0.65:
        rating = 'bad'
    else:
        rating = 'good'
    return rating


@app.function()
@web_endpoint(method="GET")
def seller(current_consumption, current_generation, latitude, longitude, days):
    weather = __weather_rating(__weather(latitude, longitude, days))
    battery_status = __battery_capacity()
    # Dummy trading suggestions
    if current_consumption < current_generation:
        trade = 1
        hint = ''
    else:
        trade = 0
        hint = 'Usage is below generation capacity.'
    if trade == 1:
        if weather == 'bad' and battery_status == 'low':
            trade = 0
            hint = "Charging batteries, not selling."
        if weather == 'good' and battery_status == 'high':
            trade = 1
            hint = 'Selling energy at 15p/kWh.'
        if weather == 'bad' and battery_status == 'high':
            trade = 1
            hint = 'Selling energy at 15p/kWh.'
    response = {"trade":trade, "hint": hint}
    return response


def __sun(latitude, longitude):
    location = requests.get(f'https://api.sunrisesunset.io/json?lat={latitude}&lng={longitude}')
    sunrise = datetime.datetime.strptime(location.json()["results"]["sunrise"], "%I:%M:%S %p")
    sunset = datetime.datetime.strptime(location.json()["results"]["sunset"], "%I:%M:%S %p")
    return {"sunrise": sunrise, "sunset" : sunset}


@app.function()
@web_endpoint(method="GET")
def behaviour(latitude, longitude):
    weather = __weather_rating(__weather(latitude, longitude, days=1))
    sun_times = __sun(latitude, longitude)
    if sun_times["sunrise"].time() <= datetime.datetime.now().time() <= sun_times["sunset"].time():
        daylight = 1
    else:
        daylight = 0
    if weather == 'good' and daylight == 1:
        hint = 'Perfect time to use energy.'
    if weather == 'bad' and daylight == 1:
        hint = 'Consider waiting for weather to improve before using lots of energy.'
    if daylight == 0:
        hint = 'Running from grid and battery power.'
    return hint


@app.function()
@web_endpoint(method="GET")
def get_tariff():
# Get data from Octopus API, and reformat for ApexCharts
    url = "https://api.octopus.energy/v1/products/AGILE-FLEX-22-11-25/electricity-tariffs/E-1R-AGILE-FLEX-22-11-25-C/standard-unit-rates/?period_from=2024-06-26T00:00Z&period_to=2024-07-02T01:29Z"
    response = requests.get(url)
    data = response.json()
    tariff_df = pd.DataFrame(data['results'])
    # tariff_df["time"] = pd.to_datetime(tariff_df["valid_from"], format="%Y-%m-%dT%H:%M:%SZ")
    tariff_df["time"] = pd.to_datetime(tariff_df["valid_from"])
    df_select = tariff_df[["value_inc_vat", "time"]]
    result = {'x':list(df_select["time"].astype(int) // 10**9),'y':list(df_select["value_inc_vat"])}
    new_dict_x = []
    new_dict_y = []
    for elem in result['x']:
        new_dict_x.append(elem)
    for elem in result['y']:
        new_dict_y.append(elem)
    zipped = zip(new_dict_x,new_dict_y)
    storage_list = []
    for x,y in zipped:
        dictionary = {'x': x, 'y': y}
        storage_list.append(dictionary)
    return storage_list

