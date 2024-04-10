import pandas as pd
import numpy as np
import math

# Read the CSV file
df = pd.read_csv('./data/pac_waves_filtered.csv')

# Filter out values of 99
filtered_df = df[df['APD'] != 99]

# Convert 'APD' column to numeric type
filtered_df = pd.to_numeric(filtered_df['APD'], errors='coerce')

# Define the ranges for APD
wavelength_ranges = [(68.0, 69.0), (83.5, 84.5), (100.5, 101.5), (134.5, 135.5), (168.25, 169.25)]
apd_ranges = []
for range in wavelength_ranges:
    temp_vals = []
    for value in range:
        temp_vals.append(math.sqrt((value * 2 * math.pi) / 9.81))
    apd_ranges.append((temp_vals[0], temp_vals[1]))

ratios = [0.500, 0.625, 0.750, 1, 1.25]
# Calculate the average WVHT for each range
for i, (range_min, range_max) in enumerate(apd_ranges):
    filtered_df = df[(df['APD'] >= range_min) & (df['APD'] < range_max)]
    # print(filtered_df['WVHT'])
    average_wvht = filtered_df['WVHT'].mean() / 2
    print(f"Average Wave Amplitude when Ratio is ~{ratios[i]}: {average_wvht}")