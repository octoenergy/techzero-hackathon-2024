import pandas as pd

user_appliances_df = pd.read_csv("uploads/user_upload.csv")
predefined_appliances_df = pd.read_csv("./appliances.csv")


def get_specific_matches(potential_matches, name_string, user_appliance):
    return potential_matches[
        (potential_matches['name'].str.contains(name_string, case=False))
        & (potential_matches['daily_usage_hours'] == user_appliance['daily_usage_hours'])
    ]


def match_appliances(user_appliances, predefined_appliances):
    matched_appliances = []

    for _, user_appliance in user_appliances.iterrows():
        potential_matches = predefined_appliances[predefined_appliances['tag'] == user_appliance['tag']]
        if user_appliance['name'] == "Ideal Logic2 C35 35kW Combination Boiler Natural Gas ErP" :
            # specific_match = potential_matches[
            #     (potential_matches['name'].str.contains("tepeo", case=False)) &
            #     (potential_matches['Daily_Usage_Hours'] == user_appliance['Daily_Usage_Hours'])
            # ]
            name_string = "tepeo"
            specific_match = get_specific_matches(potential_matches, name_string, user_appliance)
            if not specific_match.empty:
                matched_appliances.append({
                    'User Appliance': user_appliance.to_dict(),
                    'Matched Appliance': specific_match.iloc[0].to_dict(),
                    'Match Found': True
                })
            else:
                matched_appliances.append({
                    'User Appliance': user_appliance.to_dict(),
                    'Matched Appliance': None,
                    'Match Found': False
                })
        elif user_appliance['name'] == "Blue Seal G570":
            # specific_match = potential_matches[
            #     (potential_matches['name'].str.contains("Blue Seal E31D4 Electric Convection Oven Turbofan 95 Litre Digital - CE088", case=False)) &
            #     (potential_matches['Daily_Usage_Hours'] == user_appliance['Daily_Usage_Hours'])
            # ]
            name_string = "Blue Seal E31D4 Electric Convection Oven Turbofan 95 Litre Digital - CE088"
            specific_match = get_specific_matches(potential_matches, name_string, user_appliance)
            if not specific_match.empty:
                matched_appliances.append({
                    'User Appliance': user_appliance.to_dict(),
                    'Matched Appliance': specific_match.iloc[0].to_dict(),
                    'Match Found': True
                })
            else:
                matched_appliances.append({
                    'User Appliance': user_appliance.to_dict(),
                    'Matched Appliance': None,
                    'Match Found': False
                })
        elif user_appliance['name'] == "Blue Seal G570":
            name_string = "Blue Seal E31D4 Electric Convection Oven Turbofan 95 Litre Digital - CE088"
            specific_match = get_specific_matches(potential_matches, name_string, user_appliance)
            if not specific_match.empty:
                matched_appliances.append({
                    'User Appliance': user_appliance.to_dict(),
                    'Matched Appliance': specific_match.iloc[0].to_dict(),
                    'Match Found': True
                })
            else:
                matched_appliances.append({
                    'User Appliance': user_appliance.to_dict(),
                    'Matched Appliance': None,
                    'Match Found': False
                })
        else:
            if not potential_matches.empty:
                matched_appliances.append({
                    'User Appliance': user_appliance.to_dict(),
                    'Matched Appliance': potential_matches.iloc[0].to_dict(),
                    'Match Found': True
                })
            else:
                matched_appliances.append({
                    'User Appliance': user_appliance.to_dict(),
                    'Matched Appliance': None,
                    'Match Found': False
                })

    matched_appliances_df = pd.DataFrame(matched_appliances)
    return matched_appliances_df

matched_appliances_df = match_appliances(user_appliances_df, predefined_appliances_df)
# print(matched_appliances_df)
