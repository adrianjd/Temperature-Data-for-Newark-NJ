import csv
from datetime import datetime

import matplotlib.pyplot as plt

def get_weather_data(filename, dates, highs, lows):
    # Get date, high and low temperatures from file.
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # This is just to see what the column names are; comment out.
        """for index, column_header in enumerate(header_row):
            print(index, column_header)"""

        date_index = header_row.index('DATE')
        high_index = header_row.index('TMAX')
        low_index = header_row.index('TMIN')
        

        for row in reader:
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                high = int(row[high_index])
                low = int(row[low_index])
            except ValueError:
                print(f"Temperature data missing for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
        # Checking what the highest and lowest temp values are.
        print(f"The lowest recorded temperature was {min(lows)} degrees Fahrenheit.")
        print(f"The highest recorded temperature was {max(highs)} degrees Fahrenheit.")
                

# Weather data for Newark, NJ
# Python project should be opened in same folder as csv file
filename = 'newark_2021.csv' 
dates, highs, lows = [], [], []
get_weather_data(filename, dates, highs, lows)

# Plot weather.
plt.style.use('fivethirtyeight')
fig, ax = plt.subplots(figsize=(15, 8))
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Highlight the lowest temperature, first instance
y_min = min(lows)
lows_pos = lows.index(y_min)
x_min = dates[lows_pos]
ax.scatter(x_min, y_min, c='blue', edgecolors='none', s=100)
plt.annotate(f'{y_min} °F\n{x_min}', xy=(x_min, y_min), xytext=(x_min, (y_min-12))

# Highlight the highest temperature
y_max = max(highs)
highs_pos = highs.index(y_max)
x_max = dates[highs_pos]
ax.scatter(x_max, y_max, c='red', edgecolors='none', s=100)
plt.annotate(f'{y_max} °F\n{x_max}', xy=(x_max, y_max), xytext=(x_max, {y_max+5}))

# Format plot, change title where appropriate
title = "Daily High and Low Temperatures - 2021\nNewark, New Jersey"
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (°F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(-10, 130)

plt.show()
