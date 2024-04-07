# Define input and output file paths
import csv


input_file = "waves.csv"
output_file = "waves_filtered.csv"

# Function to extract selected columns and write them to a new file
def extract_selected_columns(input_file, output_file):
    selected_columns = ["WSPD", "WVHT", "APD"]
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=selected_columns)
        writer.writeheader()
        for row in reader:
            selected_data = {col: row[col] for col in selected_columns}
            writer.writerow(selected_data)

# Call the function to extract selected columns and write to file
extract_selected_columns(input_file, output_file)