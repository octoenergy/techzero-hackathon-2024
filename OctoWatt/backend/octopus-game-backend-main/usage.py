#!/usr/bin/env python3

import os
import logging
from python_graphql_client import GraphqlClient
from datetime import datetime, timezone, timedelta

def date_to_index(iso_date, offset_days=0):
  date = datetime.fromisoformat(iso_date)
  midnight = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=offset_days)
  from_midnight = date - midnight
  if from_midnight.days != 0:
    return None
  return int(from_midnight.seconds / 60 / 30)

class OctopusUsage:
  def __init__(self, debug=False):
    if debug:
      logging.basicConfig(level=logging.DEBUG)

    self.client = GraphqlClient(endpoint="https://api.octopus.energy/v1/graphql/")
    self.api_key = os.environ['OCTOPUS_API_KEY']
    self.account_number = os.environ['OCTOPUS_ACCOUNT']
    #print(api_key)
    self.init_headers()

  def init_headers(self):
    auth = """
      mutation obtainKrakenToken($input: ObtainJSONWebTokenInput!) {
        obtainKrakenToken(input: $input) {
          token
          payload
          refreshToken
          refreshExpiresIn
        }
      }
    """
    variables = { "input": { "APIKey": self.api_key } }
    data = self.client.execute(query=auth, variables=variables)
    #print(data)
    token = data['data']['obtainKrakenToken']['token']
    self.headers = { "Authorization": token }
    #print(token)


  def home_mini_usage(self):
    query = """
      query OctocareUsageInfo($accountNumber: String!) {
        octocareUsageInfo(accountNumber: $accountNumber) {
          meterDeviceId
          propertyAddressLine1
        }
      }
    """
    variables = { "accountNumber": self.account_number }
    data = self.client.execute(query=query, variables=variables, headers=self.headers)
    #print(data)
    if 'errors' in data:
      return None
    meter_device_id = data['data']['octocareUsageInfo']['meterDeviceId']
    print(f"Home mini: {meter_device_id}")

    query = """
      query SmartMeterTelemetry(
        $deviceId: String!,
        $start: DateTime,
        $end: DateTime
      ) {
        smartMeterTelemetry(
          deviceId: $deviceId
          grouping: HALF_HOURLY
          start: $start
          end: $end
        ) {
          readAt
          consumptionDelta
          demand
        }
      }
    """
    # HALF_HOURLY, FIVE_MINUTES, TEN_SECONDS, ONE_MINUTE
    midnight = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)

    variables = { "deviceId": meter_device_id, "start": (midnight - timedelta(days=1)).isoformat(), "end": midnight.isoformat() }
    data = self.client.execute(query=query, variables=variables, headers=self.headers)
    #print(data)

    by_half_hour = [None] * 48

    results = data['data']['smartMeterTelemetry']
    for block in results:
      index = date_to_index(block['readAt'], offset_days=-1)
      if index is not None:
        by_half_hour[index] = float(block['consumptionDelta'])

    #print(by_half_hour)
    return by_half_hour


  def mpan_usage(self):
    query = """
      query Properties(
        $accountNumber: String!,
        $active: Boolean
      ) {
        properties(
          accountNumber: $accountNumber,
          active: $active
        ) {
          electricityMeterPoints {
            mpan
          }
        }
      }
    """
    variables = { "accountNumber": self.account_number, "active": True }
    data = self.client.execute(query=query, variables=variables, headers=self.headers)
    mpan = data['data']['properties'][0]['electricityMeterPoints'][0]['mpan']
    print(f"MPAN: {mpan}")

    query = """
      query MeterPoints(
        $mpan: ID,
        $startAt: DateTime!
      ) {
        meterPoints(
          mpan: $mpan
        ) {
          status
          meters {
            consumption(
              grouping: HALF_HOUR,
              startAt: $startAt,
              timezone: "Europe/London",
              first: 48
            ) {
              edgeCount
              edges {
                node {
                  value
                  startAt
                }
              }
              totalCount
            }
          }
        }
      }
    """
    midnight = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)

    variables = { "mpan": mpan, "startAt": (midnight - timedelta(days=1)).isoformat()}
    data = self.client.execute(query=query, variables=variables, headers=self.headers)
    #print(data)

    by_half_hour = [None] * 48

    results = data['data']['meterPoints']['meters'][0]['consumption']['edges']
    for block in results:
      index = date_to_index(block['node']['startAt'], offset_days=-1)
      if index is not None:
        by_half_hour[index] = float(block['node']['value'])

    #print(by_half_hour)
    return by_half_hour


usage = OctopusUsage()
by_half_hour = usage.home_mini_usage()
if by_half_hour is None:
  by_half_hour = usage.mpan_usage()

print(by_half_hour)
