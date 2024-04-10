# Define input and output file paths
import csv
import numpy as np
import pandas as pd
import math

input_file_pac = "./data/pac_waves_filtered.csv"

ship_velocity = 8.74556;


# Read the filtered CSV containing only APD column
df_pac = pd.read_csv(input_file_pac)

# Filter out values of 99
filtered_df_pac = df_pac[df_pac['APD'] != 99]

# Average out the APD values
average_apd_pac = filtered_df_pac['APD'].mean()
print(filtered_df_pac['WSPD'].mean())
average_wavelength_pac = (9.81 * average_apd_pac ** 2) / (2 * np.pi)
avg_v_pac = average_wavelength_pac/average_apd_pac
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Average Period Pacific: ", average_apd_pac, "s")
print("Average Wave Length Pacific: ", average_wavelength_pac, "m")
print("Average Velocity Pacific: ", avg_v_pac, "m/s")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Ship Velocity: ", ship_velocity, "m/s")
# Assumes ship is going into the waves
rel_vel = avg_v_pac + ship_velocity;
print("Relative Velocity: ", rel_vel, "m/s")
adj_period = average_wavelength_pac/(avg_v_pac + ship_velocity)
print("Adjusted Wave Period: ", adj_period, "s")
# 5 days, in seconds
num_waves = (5 * 24 * 60 * 60)/adj_period
print("Number of Waves in 1 trip (5 days): ", num_waves, "waves")


