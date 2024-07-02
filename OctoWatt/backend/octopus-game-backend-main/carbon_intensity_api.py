#!/usr/bin/env python3

import httpx
from datetime import datetime, timezone, timedelta
import numpy as np
from collections import Counter
from rich import print
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from weather import get_weather_data
from tariffs import date_to_index, get_tariff_data

'''
Usage
from carbon_intensity_api import get_aggregate_carbon_intensity_tariff_data
answer_dict = get_aggregate_carbon_intensity_tariff_data() 
Note : Currently we get the data for London
'''
def parse_generationmix(generationmix):
    fuel_list = []
    perc_list = []
    top_3_generation_mix = []
    for fuel_dict in generationmix:
        fuel_list.append(fuel_dict['fuel'])
        perc_list.append(fuel_dict['perc'])
    sorted_perc_list = np.argsort(perc_list)[::-1]
    for index in sorted_perc_list[:3]:
        top_3_generation_mix.append({'fuel':fuel_list[index],'perc':perc_list[index]})
    return top_3_generation_mix


def get_carbon_intensity_data(regionid=13):
    headers = {'Accept': 'application/json'}
    client = httpx.Client()
    midnight = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    tomorrow_end = midnight + timedelta(days=1, hours=3)
    request = client.get(f"https://api.carbonintensity.org.uk/regional/intensity/{midnight.isoformat()}/{tomorrow_end.isoformat()}/regionid/{regionid}", params={}, headers = headers)
    intensity_data = request.json().get('data').get('data')


    by_half_hour = [None] * 54
    for block in intensity_data:
        index = date_to_index(block['from'])
        intensity_value = max(block['intensity'].get('forecast',0), block['intensity'].get('actual',0))
        intensity_index = block['intensity'].get('index',None)
        top_3_generation_mix = parse_generationmix(block['generationmix'])
        if index is not None:
            date = datetime.fromisoformat(block['from'])
            midnight = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
            from_midnight = date - midnight
            buffer = from_midnight.days*48
            by_half_hour[index+buffer] = {'intensity_value':intensity_value,'intensity_index':intensity_index,'top_3_generation_mix': top_3_generation_mix}
    return by_half_hour

def get_aggregate_carbon_intensity_tariff_data(regionid=13, region_code='C', location_code=352613): # All point to London at the moment
    aggregate_carbon_intensity_tariff_data = {}
    carbonintensity = get_carbon_intensity_data(regionid=regionid)
    tariff_data = get_tariff_data(region_code=region_code)
    weather_data = get_weather_data(location_code)

    time_of_day_indexes = {'morning' : (14,24), 'afternoon': (24,34) , 'evening': (34,44) , 'night': (44,54)}
    max_tariff = 0
    peak_time_of_day = None
    for time_of_day, indexes in time_of_day_indexes.items():
        intensity_sum = 0
        intensity_index_list = []
        energy_source_list = []
        energy_contribution_sum = 0
        tariff_sum = 0
        sun_sum = 0
        wind_sum = 0

        count = 0
        for i in range(indexes[0],indexes[1]):
            if tariff_data[i] is not None:
                tariff_sum += tariff_data[i]
                count += 1
        average_tariff_cost = tariff_sum / count if count > 0 else None

        count = 0
        for i in range(indexes[0],indexes[1]):
            if weather_data[i] is not None:
                sun_sum += weather_data[i]['sun']
                wind_sum += weather_data[i]['wind']
            count += 1
        average_sun = sun_sum / count if count > 0 else None
        average_wind_speed = wind_sum / count if count > 0 else None

        count = 0
        for i in range(indexes[0],indexes[1]):
            intensity_sum += carbonintensity[i]['intensity_value']
            intensity_index_list.append(carbonintensity[i]['intensity_index'])
            if carbonintensity[i]['top_3_generation_mix'][0]['fuel'] != 'imports': # Interest in generated power rather than importsS
                energy_source_list.append(carbonintensity[i]['top_3_generation_mix'][0]['fuel'])
                energy_contribution_sum += carbonintensity[i]['top_3_generation_mix'][0]['perc']
            else:
                energy_source_list.append(carbonintensity[i]['top_3_generation_mix'][1]['fuel'])
                energy_contribution_sum += carbonintensity[i]['top_3_generation_mix'][1]['perc']
            count +=1

        average_intensity_value = intensity_sum / count 
        common_intensity_index = Counter(intensity_index_list).most_common(1)[0][0]
        common_energy_source = Counter(energy_source_list).most_common(1)[0][0]
        common_energy_source_contribution = int(energy_contribution_sum / count)
        aggregate_carbon_intensity_tariff_data[time_of_day] = {'average_carbon_intensity_value(gCO2/kWh)':average_intensity_value, 'common_intensity_index':common_intensity_index,
                                                                 'common_energy_source':common_energy_source, 'common_energy_source_contribution(%)': common_energy_source_contribution,
                                                                 'average_tariff':average_tariff_cost, 'peak': False, 'sunniness': average_sun, 'wind_speed': average_wind_speed }
        if average_tariff_cost is not None and average_tariff_cost > max_tariff:
            peak_time_of_day = time_of_day
            max_tariff = average_tariff_cost

    aggregate_carbon_intensity_tariff_data[peak_time_of_day]['peak'] = True
    return aggregate_carbon_intensity_tariff_data

# print(json.dumps(get_aggregate_carbon_intensity_tariff_data()))

hostName = "localhost"
serverPort = 8080

class GameServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(json.dumps(get_aggregate_carbon_intensity_tariff_data()), "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), GameServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
    