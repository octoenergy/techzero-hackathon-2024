import json

import pandas as pd
import numpy as np

from utils.running_cost import half_hour_running_cost, projected_yearly_cost_range_single_appliance


from utils.parse_and_match import match_appliances


def main():
    tariffs = pd.read_csv("economy_electricity_tariffs.csv").set_index('economy_type')

    user_appliances_df = pd.read_csv("uploads/user_upload.csv")
    predefined_appliances_df = pd.read_csv("./appliances.csv")
    matched_appliances_df = match_appliances(user_appliances_df, predefined_appliances_df)

    out = dict()

    for _, appliance in matched_appliances_df.iterrows():
        # old:
        user_appliance = pd.Series(appliance["User Appliance"])
        economy = 'Economy 5'
        user_app_load_curve = pd.read_csv("business-1-old-appliance-loadcurves.csv")
        user_half_hour_cost = half_hour_running_cost(user_app_load_curve, tariffs,
                                                     usage_column=user_appliance['appliance'], economy=economy)
        user_applicance_cost = projected_yearly_cost_range_single_appliance(user_appliance, user_half_hour_cost,
                                                                            economy=economy)

        # new
        updated_appliance = pd.Series(appliance["Matched Appliance"])
        economy = 'Octopus Agile'
        updated_appliance_load_curve = pd.read_csv("business-1-new-appliance-loadcurves.csv")
        updated_half_hour_cost = half_hour_running_cost(updated_appliance_load_curve, tariffs,
                                                        usage_column=updated_appliance['appliance'], economy=economy)

        updated_appliance_cost = projected_yearly_cost_range_single_appliance(updated_appliance, updated_half_hour_cost,
                                                                              economy=economy)

        out[appliance["User Appliance"]["appliance"]] = {
            'current': user_applicance_cost,
            'recommended': updated_appliance_cost,
        }

    for app, costs in out.items():
        out[app]['savings'] = dict()
        for key, current in costs['current'].items():

            recommended = costs['recommended'][key]
            try:
                # map to floats
                current = float(current)
                recommended = float(recommended)
                out[app]['savings'][key] = current - recommended
            except ValueError:
                out[app]['savings'][key] = 'N/A'

    return out

if __name__ == "__main__":
    print(json.dumps(main(), indent=4))
