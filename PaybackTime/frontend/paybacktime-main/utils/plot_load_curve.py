import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_load_curve(file_path):
    df = pd.read_csv(file_path)

    df['timestamp'] = pd.to_datetime(df['timestamp'])

    df['half_hour_period'] = df['timestamp'].dt.floor('30min').dt.time

    average_consumption = df.groupby('half_hour_period').mean()

    average_consumption.reset_index(inplace=True)
    average_consumption['half_hour_period'] = pd.to_datetime(average_consumption['half_hour_period'].astype(str))

    
    plt.figure(figsize=(14, 7))

    appliances = ['total_consumption', 'boiler', 'electric_radiator', 'cooler_freezer', 'oven', 'microwave', 'vrf_system', 'split_system']

    for appliance in appliances:
        sns.lineplot(data=average_consumption, x='half_hour_period', y=appliance, label=appliance)

    plt.title('Average Consumption by Half-Hourly Period for Each Appliance')
    plt.xlabel('Time of Day')
    plt.ylabel('Average Consumption (kWh)')
    plt.xticks(rotation=45)
    plt.legend(title='Appliance')
    plt.grid(True)
    plt.tight_layout()
    return plt
