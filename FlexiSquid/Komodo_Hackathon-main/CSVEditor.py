import pandas as pd
import numpy as np
from datetime import datetime, timedelta

MainData = pd.read_csv('data\output_dataframe.csv') 
Carbon = pd.read_csv('data\carbon_intensity_example_out.csv') 

# display  
print("Original 'output_dataframe.csv' CSV MainData: \n") 
print(MainData) 
  
# drop function which is used in removing or deleting rows or columns from the CSV files 
MainData.drop('Period from', inplace=True, axis=1) 
MainData.drop('Period to', inplace=True, axis=1) 
MainData.drop('Price_moving_avg', inplace=True, axis=1) 
  
# display  
print("\nCSV MainData after deleting the columns :\n") 
print(MainData)

# Define the start and end date
start_date = datetime(2024, 6, 2)
end_date = datetime(2024, 7, 2)

# Generate a list of datetime objects at 30 minute intervals
num_intervals = int((end_date - start_date).total_seconds() / 1800) + 1  # 1800 seconds = 30 minutes
timestamps = [start_date + timedelta(minutes=30*x) for x in range(num_intervals)]

# Convert datetime objects to Unix timestamps
unix_timestamps = [int(t.timestamp()) for t in timestamps]

MainData.insert(0, 'unix_timestamp', unix_timestamps[:len(MainData)])  # Ensure it matches the length of the existing DataFrame

# Adding Carbon Intensity

CarbonIntensity = Carbon['CarbonIntensity']
MainData['Carbon Intensity'] = CarbonIntensity



# Date range
Start_Row: 1152
End_Row: 1440
Date_Range = MainData.iloc[1152:1440]
'''
A = First 48 Carbon Data points
B = Lowest 48 Carbon Data points
C = Cost of A
D = Cost of B

E = First 48 Price Points 
F = Lowest 48 Price Points
G = Emissions of F
H = Emissions of G
'''
# Calculating Emissions Savings
'''
CarbonThreshold = 100

carbon_filtered_rows = MainData[MainData['Carbon Intensity'] < CarbonThreshold].head(48)

Carbon_filtered_sum = carbon_filtered_rows['Carbon Intensity'].sum()

Carbon_First_48 = MainData['Carbon Intensity'].head(48).sum()                       

print("Sum of Emissions for first 48 rows with Intensity < threshold:", Carbon_filtered_sum)
print("Sum of Emissions for first 48 rows without threshold:", Carbon_First_48)
'''

B = Date_Range.nsmallest(48, 'Carbon Intensity')
B_sum = B['Carbon Intensity'].sum()
D = B['Agile Import price (p/kWh)'].sum()
A  = Date_Range.head(48)
A_sum = A['Carbon Intensity'].sum()
C = A['Agile Import price (p/kWh)'].sum()

CostSavings = C - D
CostSavingsPounds = CostSavings/100


print("Sum of Carbon Intensity for the lowest 48 rows within the defined range:", B_sum)
print("Sum of Carbon Intensity for the first 48 rows within the defined range:", A_sum)
print("Cost saved by optimising for Carbon Emission:", CostSavings)

# Calculating Cost Savings
F = Date_Range.nsmallest(48, 'Agile Import price (p/kWh)')
F_sum = F['Agile Import price (p/kWh)'].sum()
G = F['Carbon Intensity'].sum()
E = Date_Range.head(48)
E_Sum = E['Agile Import price (p/kWh)'].sum()
H = E['Carbon Intensity'].sum()
CarbonSavings = H - G
CarbonSavingsKG = CarbonSavings/1000


print("Sum of Carbon Intensity for the lowest 48 rows within the defined range:", F_sum)
print("Sum of Carbon Intensity for the first 48 rows within the defined range:", E_Sum)
print("Cost saved by optimising for Carbon Emission:", CarbonSavings)

# Adding Savings calculations to CSV. PLEASE CHANGE TO MAKE THIS DYNAMIC. 

MainData['Carbon Optimised Emission'] = B_sum/1000
MainData['Carbon Unoptimised Emission'] = A_sum/1000
MainData['Carbon Optimised Cost Savings'] = CostSavingsPounds

MainData['Price Optimised Cost'] = F_sum/100
MainData['Price Unoptimised Cost'] = E_Sum/100
MainData['Price Optimised Emission Savings'] = CarbonSavingsKG

# Save to CSV

MainData.to_csv('data\GrafanaData.csv', index=False)
