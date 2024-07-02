import pandas as pd

# import property ownership data. downloaded from https://use-land-property-data.service.gov.uk/datasets/ccod
london_ccod_data = pd.read_csv('/Users/luke/Downloads/CCOD_FULL_2024_06.csv', low_memory=False)

# download non-domestic EPC data from https://epc.opendatacommunities.org/non-domestic/search
EPC_data_stub = '/Users/luke/Downloads/all-non-domestic-certificates/'
# select subset of 14 boroughs to work with
chosen_boroughs = ['CITY OF LONDON', 'CAMDEN', 'HACKNEY', 'HAMMERSMITH AND FULHAM', 'ISLINGTON', 'LEWISHAM', 'SOUTHWARK', 'GREENWICH', 'NEWHAM', 'TOWER HAMLETS', 'WESTMINSTER', 'KENSINGTON AND CHELSEA', 'WANDSWORTH', 'LAMBETH']
# locate accompanying folders within EPC data download
chosen_borough_path_extensions = ['non-domestic-E09000001-City-of-London/', 'non-domestic-E09000007-Camden/', 'non-domestic-E09000012-Hackney/', 'non-domestic-E09000013-Hammersmith-and-Fulham/', 'non-domestic-E09000019-Islington/', 'non-domestic-E09000023-Lewisham/', 'non-domestic-E09000028-Southwark/', 'non-domestic-E09000011-Greenwich/', 'non-domestic-E09000025-Newham/', 'non-domestic-E09000030-Tower-Hamlets/', 'non-domestic-E09000033-Westminster/', 'non-domestic-E09000020-Kensington-and-Chelsea/', 'non-domestic-E09000032-Wandsworth/', 'non-domestic-E09000022-Lambeth/']

# filter property ownership data for chosen boroughs
chosen_borough_mask = london_ccod_data['District'].isin(chosen_boroughs)
borough_ccod_data = london_ccod_data[chosen_borough_mask]

# collate EPC data for chosen boroughs
borough_EPC_data = pd.DataFrame()
borough_counter = 0
for i in range(len(chosen_borough_path_extensions)):
    EPC_file_path = EPC_data_stub + chosen_borough_path_extensions[i] + 'certificates.csv'
    if borough_counter == 0:
        borough_EPC_data = pd.read_csv(EPC_file_path)
    else:
        new_EPC_data = pd.read_csv(EPC_file_path, header=None)
        new_EPC_data.columns = borough_EPC_data.columns  # Set the column names to match the first DataFrame
        borough_EPC_data = pd.concat([borough_EPC_data, new_EPC_data], ignore_index=True)
    borough_counter += 1

# rename EPC address column to match property ownership address column
borough_EPC_data.rename(columns={'ADDRESS': 'Matching Address'}, inplace=True)

borough_ccod_data['Postcode'] = borough_ccod_data['Postcode'].astype(str)
borough_ccod_data['Property Address'] = borough_ccod_data['Property Address'].astype(str)

# remove London and postode from property ownership address string to better match EPC address string
for i in range(1, len(borough_ccod_data)):
    postcode = borough_ccod_data.iloc[i, borough_ccod_data.columns.get_loc('Postcode')]
    just_postcode = ', ' + postcode
    just_postcode_with_london = ', London ' + postcode
    postcode_with_brackets = ', (' + postcode + ')'
    postcode_with_london_and_brackets = ', London (' + postcode + ')'
    postcode_with_brackets_no_comma = '(' + postcode + ')'

    address = borough_ccod_data.iloc[i, borough_ccod_data.columns.get_loc('Property Address')]
    matching_address = address.replace(just_postcode, '')
    matching_address = matching_address.replace(just_postcode_with_london, '')
    matching_address = matching_address.replace(postcode_with_brackets, '')
    matching_address = matching_address.replace(postcode_with_london_and_brackets, '')
    matching_address = matching_address.replace(postcode_with_brackets_no_comma, '')

    borough_ccod_data.loc[borough_ccod_data.index[i], 'Matching Address'] = matching_address

# merge the EPC and property ownership data sets on the address column
merged_borough_EPC_and_ccod_data = pd.merge(borough_ccod_data, borough_EPC_data, on=['Matching Address'], how='inner')

# merged_borough_EPC_and_ccod_data.rename(columns={'Postcode': 'Postcode'}, inplace=True)
# merged_borough_EPC_and_ccod_data.drop(columns=['Postcode_y'])

# Convert 'FLOOR_AREA' to numeric so that it can be ranked. Change errors to NaN
merged_borough_EPC_and_ccod_data['FLOOR_AREA'] = pd.to_numeric(merged_borough_EPC_and_ccod_data['FLOOR_AREA'], errors='coerce')

# Sort the DataFrame by 'Postcode' and 'FLOOR_AREA' to work with unique postcodes and enable picking large floor_area for each postcode
merged_borough_EPC_and_ccod_data.sort_values(by=['Postcode', 'FLOOR_AREA'], inplace=True, na_position='last', ascending=False)

# Group by 'Postcode' and select the first entry within each group
merged_borough_EPC_and_ccod_data = merged_borough_EPC_and_ccod_data.groupby('Postcode').first().reset_index()

# import mapping between EPC industry type and ofgem industry type. import ofgem industry electricity intensity (kWh / m2 / year)
property_type_map = pd.read_csv('property_type_mapping.csv')

# append ofgem industry type and electricity intensity
merged_borough_EPC_and_ccod_data = pd.merge(merged_borough_EPC_and_ccod_data,property_type_map,on='PROPERTY_TYPE',how='left')

# calculate annual consumption
merged_borough_EPC_and_ccod_data['Consumption (kWh)'] = merged_borough_EPC_and_ccod_data['FLOOR_AREA'] * merged_borough_EPC_and_ccod_data['Energy intensity']

# export to csv
merged_borough_EPC_and_ccod_data.to_csv('merged_borough_EPC_and_ccod_data.csv', index=False)