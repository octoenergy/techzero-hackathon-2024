import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

carbon_df = pd.read_csv('../data/carbon_intensity_example_out.csv', parse_dates=['PeriodFrom', 'PeriodTo'], date_parser=lambda x: pd.to_datetime(x, format='%Y-%m-%dT%H:%MZ'))
carbon_df.set_index('PeriodFrom', inplace=True)
carbon_df['CarbonIntensityRolling'] = carbon_df['CarbonIntensity'].astype(float).rolling(window=100).mean()
carbon_df['Asset_load'] = 1
print(carbon_df)

# Plotting
fig, ax1 = plt.subplots(figsize=(10, 6))

# Scatter plot for Price_moving_avg on the primary y-axis
color = 'tab:blue'
ax1.set_xlabel('Timestamp')
ax1.set_ylabel('Carbon Intensity', color=color)
ax1.plot(carbon_df.index, carbon_df['CarbonIntensityRolling'], marker='o', linestyle='-', color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_xticklabels(carbon_df.index, rotation=45)

# Create a secondary y-axis for Asset_load
ax2 = ax1.twinx()  
color = 'tab:red'
ax2.set_ylabel('Asset Load')
ax2.plot(carbon_df.index, carbon_df['Asset_load'], color=color)
ax2.tick_params(axis='y')

# Title and layout
plt.title('Carbon Intensity vs Asset Load')
fig.tight_layout()

old_arr = carbon_df['Asset_load'].tolist()
prices = carbon_df['CarbonIntensityRolling'].tolist()
new_arr = old_arr

window_size = 200
for i in range(0, len(old_arr)-window_size, 10):
    prices_subset = prices[i:i+window_size]
    min_value = min(prices_subset)
    min_index = prices_subset.index(min_value) + i
    new_arr[i] -= 1
    new_arr[min_index] += 1

carbon_df['New_asset_load'] = new_arr
carbon_df['New_asset_load_rolling'] = carbon_df['New_asset_load'].rolling(window=100).mean()

ax2.plot(carbon_df.index, carbon_df['New_asset_load_rolling'], color='green')

# ax2.plot(carbon_df.index, carbon_df['CarbonIntensity'], color=color)


carbon_df.to_csv('../data/carbon_intensity.csv')
plt.show()
plt.savefig('../img/carbon_intensity_vs_asset_load.png')
