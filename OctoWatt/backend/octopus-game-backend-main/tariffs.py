#!/usr/bin/env python3
import os
import httpx
from datetime import datetime, timezone, timedelta

def date_to_index(iso_date):
  date = datetime.fromisoformat(iso_date)
  midnight = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
  from_midnight = date - midnight
  if from_midnight.days < 0:
    return None
  return int(from_midnight.seconds / 60 / 30)


def get_tariff_data(region_code='C'):
    api_key = os.environ['OCTOPUS_API_KEY']
    auth = httpx.BasicAuth(username=api_key, password="")
    client = httpx.Client()
    midnight = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    tomorrow_start =  midnight + timedelta(days=1)
    tomorrow_end = tomorrow_start + timedelta(hours=3)
    tariff_url = f"https://api.octopus.energy/v1/products/AGILE-FLEX-22-11-25/electricity-tariffs/E-1R-AGILE-FLEX-22-11-25-{region_code}/standard-unit-rates/"
    response = client.get(tariff_url,params={"period_from": midnight.isoformat(), "period_to": tomorrow_end.isoformat()},auth=auth)
    # Type of Contract :  Cap stays at £1 per unit but new formula only deducts 17.9p from higher unit prices, https://energy-stats.uk/octopus-agile-east-midlands/
    # Tariff code is of the format T"E-1R-$PRODUCT_CODE-C" where PRODUCT_CODE here is AGILE-FLEX-22-11-25 and C is region (London)
    # To change region, please use https://en.m.wikipedia.org/wiki/Meter_Point_Administration_Number

    data = response.json()
    results = data.get('results')
    by_half_hour = [None] * 54

    for block in results:
        index = date_to_index(block['valid_from'])
        date = datetime.fromisoformat(block['valid_from'])
        midnight = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
        from_midnight = date - midnight
        buffer = from_midnight.days*48
        if index is not None:
            by_half_hour[buffer+index] = block['value_inc_vat']
    return by_half_hour