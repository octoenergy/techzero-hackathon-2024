import pandas as pd
import numpy as np
import argparse
import logging

import os

logger = logging.getLogger(__name__)


def load_carbon_intensity():
    df = pd.read_csv("./octopus_consumption.csv", parse_dates=True)[["Carbon Intensity (gCO2/kWh)"]]
    df['timestamp'] = df.index.to_series().dt.time.astype(str)
    carbon_intensity = (
        df
        .groupby('timestamp')
        .mean()
        .rename(columns={"Carbon Intensity (gCO2/kWh)": "carbon_intensity"})
        .reset_index()
    )
    return carbon_intensity


def half_hour_running_cost(usage:pd.DataFrame, tariffs:pd.DataFrame, usage_column='primaryValue', economy:str='Economy 5'):
    usage['timestamp_day'] = pd.to_datetime(usage['timestamp']).dt.time.astype(str)
    carbon_intensity = load_carbon_intensity()
    usage = (
        usage
        .merge(
            tariffs.loc[economy]
            .reset_index(drop=True)
            .rename(columns={'timestamp': 'timestamp_day'}),
            on='timestamp_day',
            how='left',
        )
        .merge(
            carbon_intensity
            .rename(columns={'timestamp': 'timestamp_day'}),
            on='timestamp_day',
            how='left',
        )
    )
    usage['cost'] = usage[usage_column] * usage['unit_price']
    usage['carbon_emission'] = usage[usage_column] * usage['carbon_intensity']
    return usage


def projected_yearly_cost_range_single_appliance(appliance:pd.Series, half_hour_cost:pd.DataFrame, economy:str='Economy 5'):
    upfront_cost = appliance['upfront_cost']
    running_cost = half_hour_cost['cost'].sum()
    maintenance_cost = np.array([float(x) for x in appliance['annual_maintenance_cost'].split("-")])

    lifespan = appliance['lifetime'].split("-")
    if len(lifespan) == 1:
        lifespan = np.array([int(lifespan[0]), int(lifespan[0])])
    else:
        lifespan = np.array([int(x) for x in lifespan])

    # if maintenance cost is a range, take the average
    if isinstance(maintenance_cost, np.ndarray):
        maintenance_cost = np.mean(maintenance_cost)

    lifetime_cost = upfront_cost + running_cost + maintenance_cost
    yearly_cost = lifetime_cost / lifespan[::-1]

    carbon_emission = half_hour_cost['carbon_emission'].sum() / 1000 / lifespan[::-1]
    yearly_maintenance_cost = maintenance_cost / lifespan[::-1]

    # normalise all ranges into a single value
    upfront_cost = np.mean(upfront_cost)
    yearly_maintenance_cost = np.mean(yearly_maintenance_cost)
    yearly_cost = np.mean(yearly_cost)
    carbon_emission = np.mean(carbon_emission)
    lifespan = np.mean(lifespan)

    return {
        'economic_type': economy,
        'upfront_cost': upfront_cost,
        'lifetime': lifespan,
        'yearly_maintenance_cost': yearly_maintenance_cost,
        'yearly_cost_range': yearly_cost,
        'yearly_carbon_emission': carbon_emission,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--economy', type=str, default='Economy 5')
    parser.add_argument('--loadcurve', type=str, default='business-1-appliance-loadcurves.csv')
    parser.add_argument('--output', type=str, default='business-1-utility-gas-costs.csv')
    parser.add_argument('--appliance_id', type=str, default=1)
    args = parser.parse_args()

    tariffs = pd.read_csv('economy_electricity_tariffs.csv').set_index('economy_type')
    load_curve = pd.read_csv(args.loadcurve)

    appliances = pd.read_csv('appliances.csv',)
    appliance = appliances.loc[int(args.appliance_id)]
    appliance_type = appliance['appliance']

    load_curve = load_curve[['business_id', 'mpxn', 'timestamp', 'total_consumption', appliance_type]]

    half_hour_cost = half_hour_running_cost(load_curve, tariffs, usage_column=appliance_type, economy=args.economy)
    half_hour_cost.to_csv(args.output, index=False)
    projected_yearly_cost = projected_yearly_cost_range_single_appliance(appliance, half_hour_cost, args.economy)
    yearly_cost_range = projected_yearly_cost['yearly_cost_range']
    yearly_carbon_emission_range = projected_yearly_cost['yearly_carbon_emission']

    print(appliance)
    print(f'Economy type: {args.economy}')
    print(f'Yearly cost range: {yearly_cost_range[0]:.2f}-{yearly_cost_range[1]:.2f}')
    print(f'Yearly Carbon emission range (kg): {yearly_carbon_emission_range[0]:.2f}-'
          f'{yearly_carbon_emission_range[1]:.2f}')


if __name__ == '__main__':
    main()
