import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Read the filtered CSV containing only APD column
df = pd.read_csv("./data/pac_waves_filtered.csv")

# Filter out values of 99
filtered_df = df[df['APD'] != 99]

# Convert 'APD' column to numeric type
filtered_df = pd.to_numeric(filtered_df['APD'], errors='coerce')

# Apply the formula to every value in the APD column to get wave length
transformed_values = [(9.81 * value ** 2) / (2 * np.pi) for value in filtered_df]

transformed_df = pd.DataFrame(transformed_values, columns=['Transformed_APD'])

# To plot wave period instead, plot filtered_df['APD'] instead of transformed_df['Transformed_APD'

# Calculate statistical measurements
mean_apd = transformed_df['Transformed_APD'].mean()
std_apd = transformed_df['Transformed_APD'].std()
median_apd = transformed_df['Transformed_APD'].median()
percentile_25 = np.percentile(transformed_df['Transformed_APD'], 25)
percentile_75 = np.percentile(transformed_df['Transformed_APD'], 75)


# Plot APD values as a distribution
hist, bins, _  = plt.hist(transformed_df['Transformed_APD'], bins=500, edgecolor='black')
print(bins)
plt.xlabel('Average Wave Length (Meters)')
plt.ylabel('Frequency')
plt.title('Pacific Ocean Average Wave Length Distribution')

# SPECIFC TO WAVE LENGTH
# Find the three most frequent bins with x values over 67.5
top_bins = [(bin_val, bin_freq) for bin_val, bin_freq in zip(bins, hist) if bin_val > 67.5]
top_bins.sort(key=lambda x: x[1], reverse=True)
top_bins = top_bins[:5]

# Find all bins where the starting number is 101
freq_bins_625 = [(bin_val, bin_freq) for bin_val, bin_freq in zip(bins, hist) if 84 < bin_val < 85]

# Add labels to the three most frequent bins
plt.text(0.65, 0.9, "Most Frequent Bins close to 0.625:", fontsize=10, transform=plt.gca().transAxes, ha='right')
for i, (bin_val, bin_freq) in enumerate(freq_bins_625):
    # plt.text(bin_val, bin_freq, f"{bin_freq}", ha='center', va='bottom')
    plt.text(0.65, 0.85 - i * 0.05, f"Bin Value: {bin_val:.2f}, Frequency: {bin_freq}", fontsize=8,
             transform=plt.gca().transAxes, ha='right')
    
# Find all bins where the starting number is 101
freq_bins_75 = [(bin_val, bin_freq) for bin_val, bin_freq in zip(bins, hist) if 100.5 < bin_val < 101.5]

# Annotate the plot with the frequency of all bins starting with 101 --> 101.25 is 0.75 * 135 where 135 is ship length
plt.text(0.9, 0.9, "Most Frequent Bins close to 0.75:", fontsize=10, transform=plt.gca().transAxes, ha='right')
for i, (bin_val, bin_freq) in enumerate(freq_bins_75):
    plt.text(0.9, 0.85 - i * 0.05, f"Bin Value: {bin_val:.2f}, Frequency: {bin_freq}", fontsize=8,
             transform=plt.gca().transAxes, ha='right')
    
# Find all bins where the starting number is 84 --> 84.375 is 0.625 * 135 where 135 is ship length
freq_bins_100 = [(bin_val, bin_freq) for bin_val, bin_freq in zip(bins, hist) if 133.5 < bin_val < 134.5]

# Annotate the plot with the frequency of all bins starting with 101
plt.text(0.65, 0.65, "Most Frequent Bins close to 1:", fontsize=10, transform=plt.gca().transAxes, ha='right')
for i, (bin_val, bin_freq) in enumerate(freq_bins_100):
    plt.text(0.65, 0.6 - i * 0.05, f"Bin Value: {bin_val:.2f}, Frequency: {bin_freq}", fontsize=8,
             transform=plt.gca().transAxes, ha='right')
    
# Find all bins where the starting number is 84 --> 84.375 is 0.625 * 135 where 135 is ship length
freq_bins_125 = [(bin_val, bin_freq) for bin_val, bin_freq in zip(bins, hist) if 168.25 < bin_val < 169.25]

# Annotate the plot with the frequency of all bins starting with 101
plt.text(0.9, 0.65, "Most Frequent Bins close to 1.25:", fontsize=10, transform=plt.gca().transAxes, ha='right')
for i, (bin_val, bin_freq) in enumerate(freq_bins_125):
    plt.text(0.9, 0.6 - i * 0.05, f"Bin Value: {bin_val:.2f}, Frequency: {bin_freq}", fontsize=8,
             transform=plt.gca().transAxes, ha='right')


# Annotate the plot with statistical measurements
plt.text(0.75, 0.35, f"Mean: {mean_apd:.2f}", transform=plt.gca().transAxes)
plt.text(0.75, 0.30, f"Standard Deviation: {std_apd:.2f}", transform=plt.gca().transAxes)
plt.text(0.75, 0.25, f"Median: {median_apd:.2f}", transform=plt.gca().transAxes)
plt.text(0.75, 0.20, f"25th Percentile: {percentile_25:.2f}", transform=plt.gca().transAxes)
plt.text(0.75, 0.15, f"75th Percentile: {percentile_75:.2f}", transform=plt.gca().transAxes)

plt.grid(True)
plt.show()