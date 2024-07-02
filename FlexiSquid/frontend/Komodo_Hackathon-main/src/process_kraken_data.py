import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file
df = pd.read_csv('../data/agile-half-hour-actual-rates-02-06-2024_01-07-2024.csv', parse_dates=['Period from', 'Period to'], date_parser=lambda x: pd.to_datetime(x, format='%d/%m/%Y %H:%M'))
df['Price_moving_avg'] = df['Agile Import price (p/kWh)'].astype(float).rolling(window=100).mean()
df['Asset_load'] = 1


# Set the timestamp column as the index
df.set_index('Period from', inplace=True)

print('-'*20)
print(df.shape)
print('-'*20)

# Plotting
fig, ax1 = plt.subplots(figsize=(10, 6))

# Scatter plot for Price_moving_avg on the primary y-axis
color = 'tab:blue'
ax1.set_xlabel('Timestamp')
ax1.set_ylabel('Price (p/kWh)', color=color)
ax1.scatter(df.index, df['Price_moving_avg'], marker='o', linestyle='-', color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_xticklabels(df.index, rotation=45)

# Create a secondary y-axis for Asset_load
ax2 = ax1.twinx()  
color = 'tab:red'
ax2.set_ylabel('Asset Load')  
ax2.plot(df.index, df['Asset_load'], color=color)
ax2.tick_params(axis='y')

# Title and layout
plt.title('Price (p/kWh) Changes Over Time and Asset Load')
fig.tight_layout()  

old_arr = df['Asset_load'].tolist()
prices = list(np.random.rand(len(old_arr)))
prices = df['Agile Import price (p/kWh)'].tolist()
new_arr = old_arr

window_size = 200
for i in range(0, len(old_arr)-window_size, 10):
    prices_subset = prices[i:i+window_size]
    min_value = min(prices_subset)
    min_index = prices_subset.index(min_value) + i
    new_arr[i] -= 1
    new_arr[min_index] += 1

df['New_asset_load'] = new_arr
df['New_asset_load_rolling'] = df['New_asset_load'].rolling(window=100).mean()

df.to_csv('../data/output_dataframe.csv')

ax2.plot(df.index, df['New_asset_load_rolling'], color='green')

print(df[400:420])

plt.show()
plt.savefig('../img/energy_pricing_vs_asset_load.png')


