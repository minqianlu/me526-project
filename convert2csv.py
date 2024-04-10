import csv

# Define input and output file paths
input_file = "./data/pac_waves.txt"
output_file = "./data/pac_waves.csv"

# Function to convert the input text file to CSV and write it to a CSV file
def convert_to_csv(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = infile.readlines()
        writer = csv.writer(outfile)
        # Skip header lines
        data_start_index = 0
        for index, line in enumerate(reader):
            if not line.startswith('#'):
                data_start_index = index
                break

        # Write CSV header
        header = ['YY', 'MM', 'DD', 'hh', 'mm', 'WDIR', 'WSPD', 'GST', 'WVHT', 'DPD', 'APD', 'MWD', 'PRES', 'ATMP', 'WTMP', 'DEWP', 'VIS', 'TIDE']
        writer.writerow(header)

        # Write data to CSV
        for line in reader[data_start_index:]:
            row = line.strip().split()
            writer.writerow(row)

# Call the function to convert to CSV and write to file
convert_to_csv(input_file, output_file)
