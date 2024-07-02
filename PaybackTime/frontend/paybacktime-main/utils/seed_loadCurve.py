import csv
import random
from datetime import datetime, timedelta

def parse_range(value):
    try:
        if '-' in value:
            low, high = map(int, value.split('-'))
            return (low + high) // 2  
        return int(value)
    except ValueError:
        return 0  

def read_appliances_from_csv(filename):
    appliances = {}
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        print("CSV columns:", reader.fieldnames)
        for row in reader:
            try:
                appliances[row['appliance']] = {
                    'Power': float(row['max_power']),
                    'Is_Gas': row['tag'].lower() == 'gas',
                    'Daily_Usage_Hours': 24,  
                    'Age_Years': 0,  
                    'Lifespan_Years': parse_range(row['lifetime']),
                    'Upfront_Cost': float(row['upfront_cost']),
                    'Warranty': parse_range(row['warranty']),
                    'Annual_Maintenance_Cost': parse_range(row['annual_maintenance_cost'].split('-')[0]),
                    'Avg_Input': float(row['avg_input']),
                    'Battery_Compatible': row['battery_compatible'] == '1'
                }
            except (KeyError, ValueError) as e:
                print(f"Error processing row: {e}")
                print("Row data:", row)
    return appliances

def generate_operating_hours(appliances):
    operating_hours = {}
    for appliance in appliances:
        operating_hours[appliance] = (0, 24)  # Assuming 24/7 operation for now
    return operating_hours

def get_random_consumption(power_level, max_power):
    levels = {
        'low': (0.1, 0.3),
        'moderate': (0.4, 0.6),
        'high': (0.7, 0.9),
    }
    min_val, max_val = levels[power_level]
    return round(random.uniform(min_val, max_val) * max_power, 2)

def get_season(date):
    month = date.month
    if 3 <= month < 6:
        return 'spring'
    elif 6 <= month < 9:
        return 'summer'
    elif 9 <= month < 12:
        return 'fall'
    else:
        return 'winter'

def generate_consumption_data(business_id, mpxn, start_date, end_date, appliances, operating_hours):
    consumption_data = []
    current_date = start_date
    total_power = sum(app['Power'] for app in appliances.values())

    patterns = {
        'winter': {
            'weekday': [(0, 4.5, 'high'), (5, 10.5, 'low'),(11, 13.5, 'moderate'), (14, 16.5, 'low'), (17, 21.5, 'moderate'), (22, 23.5, 'low')],
            'weekend': [(0, 4.5, 'high'),(5, 10.5, 'low'), (11, 21.5, 'moderate'), (22, 23.5, 'low')],
        },
        'spring': {
            'weekday': [(0, 4.5, 'high'),(5, 10.5, 'low'), (11, 13.5, 'moderate'), (14, 16.5, 'moderate'), (17, 21.5, 'moderate'), (22, 23.5, 'low')],
            'weekend': [(0, 4.5, 'high'),(5, 10.5, 'low'), (11, 21.5, 'moderate'), (22, 23.5, 'low')],
        },
        'summer': {
            'weekday': [(0, 4.5, 'high'),(5, 10.5, 'low'), (11, 13.5, 'moderate'), (14, 16.5, 'low'), (17, 21.5, 'moderate'), (22, 23.5, 'low')],
            'weekend': [(0, 4.5, 'high'),(5, 10.5, 'low'), (11, 13.5, 'moderate'), (14, 16.5, 'moderate'), (17, 21.5, 'moderate'), (22, 23.5, 'low')],
        },
        'fall': {
            'weekday': [(0, 4.5, 'high'),(5, 10.5, 'low'), (11, 13.5, 'moderate'), (14, 16.5, 'low'), (17, 21.5, 'moderate'), (22, 23.5, 'low')],
            'weekend': [(0, 4.5, 'high'),(5, 10.5, 'low'), (11, 21.5, 'moderate'), (22, 23.5, 'low')],
        },
    }

    while current_date <= end_date:
        season = get_season(current_date)
        is_weekday = current_date.weekday() < 5
        day_pattern = patterns[season]['weekday' if is_weekday else 'weekend']

        for start_hour, end_hour, power_level in day_pattern:
            start_time = current_date.replace(hour=int(start_hour), minute=int((start_hour % 1) * 60))
            end_time = current_date.replace(hour=int(end_hour), minute=int((end_hour % 1) * 60))

            while start_time < end_time:
                total_consumption = get_random_consumption(power_level, total_power)
                appliance_consumptions = {}

                for appliance, details in appliances.items():
                    device_start, device_end = operating_hours[appliance]
                    if device_start <= start_time.hour < device_end:
                        device_consumption = (details['Power'] / total_power) * total_consumption
                        appliance_consumptions[appliance] = round(device_consumption, 2)
                    else:
                        appliance_consumptions[appliance] = 0

                consumption_data.append({
                    'business_id': business_id,
                    'mpxn': mpxn,
                    'timestamp': start_time,
                    'total_consumption': total_consumption,
                    **appliance_consumptions
                })
                start_time += timedelta(minutes=30)

        current_date += timedelta(days=1)

    return consumption_data

def main():
    business_id = 1
    mpxn = '9876543210'
    start_date = datetime(2023, 7, 1)
    end_date = datetime.now()

    appliances = read_appliances_from_csv('appliances.csv')
    operating_hours = generate_operating_hours(appliances)

    consumption_data = generate_consumption_data(business_id, mpxn, start_date, end_date, appliances, operating_hours)

    column_order = ['business_id', 'mpxn', 'timestamp', 'total_consumption'] + list(appliances.keys())

    filename = f"business-{business_id}-new-appliance-loadcurves.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=column_order)
        writer.writeheader()
        writer.writerows(consumption_data)

    print(f'Data saved to {filename}')


main()