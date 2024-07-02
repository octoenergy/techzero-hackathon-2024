import csv
from datetime import datetime, timedelta

def generate_tariff_data(start_date, end_date, peak_price, off_peak_price, economy_type):
    data = []
    current_date = start_date
    off_peak_hours = 5.5 if economy_type == 'Economy 5' else 7.5
    off_peak_intervals = off_peak_hours * 2 

    while current_date <= end_date:
        for period in range(1, 49):
            timestamp = datetime(2023, 7, 1, 0, 00) + timedelta(minutes=30 * period)  
            if (economy_type == 'Economy 5' and 0 <= period < off_peak_intervals) or \
               (economy_type == 'Economy 7' and 0 <= period < off_peak_intervals):
                unit_price = off_peak_price
            else:
                unit_price = peak_price
            data.append({
                'timestamp': timestamp.strftime('%H:%M:%S'),
                'unit_price': unit_price,
                'economy_type': economy_type
            })
        current_date += timedelta(days=1)
    
    return data

def main():
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 1, 1)
    peak_price = 0.288  
    off_peak_price = 0.08988  

    economy_5_data = generate_tariff_data(start_date, end_date, peak_price, off_peak_price, 'Economy 5')
    economy_7_data = generate_tariff_data(start_date, end_date, peak_price, off_peak_price, 'Economy 7')

    fieldnames = ['timestamp', 'unit_price', 'economy_type']

    with open('economy_tariffs.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(economy_5_data + economy_7_data)

    print('Data saved to economy_tariffs.csv')

main()