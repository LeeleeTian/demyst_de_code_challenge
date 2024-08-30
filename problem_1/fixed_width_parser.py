import csv
import json

# Load the spec.json
with open('spec.json', 'r') as file:
    spec = json.load(file)

column_names = spec["ColumnNames"]
offsets = list(map(int, spec["Offsets"]))
fixed_width_encoding = spec["FixedWidthEncoding"]
delimited_encoding = spec["DelimitedEncoding"]
include_header = spec["IncludeHeader"].lower() == "true"

# Generate a fixed-width file
def generate_fixed_width_file(data, output_file):
    with open(output_file, 'w', encoding=fixed_width_encoding) as fw_file:
        if include_header:
            header = ''.join([f"{name:<{offset}}" for name, offset in zip(column_names, offsets)])
            fw_file.write(header + '\n')
        for row in data:
            line = ''.join([f"{str(value)[:offset]:<{offset}}" for value, offset in zip(row, offsets)])
            fw_file.write(line + '\n')

# Parse the fixed-width file and generate a CSV
def parse_fixed_width_to_csv(input_file, output_file):
    with open(input_file, 'r', encoding=fixed_width_encoding) as fw_file, \
         open(output_file, 'w', newline='', encoding=delimited_encoding) as csv_file:
        
        csv_writer = csv.writer(csv_file)
        
        if include_header:
            next(fw_file)  # Skip header in fixed-width file
            csv_writer.writerow(column_names)  # Write header to CSV
        
        for line in fw_file:
            parsed_row = []
            index = 0
            for offset in offsets:
                parsed_row.append(line[index:index+offset].strip())
                index += offset
            csv_writer.writerow(parsed_row)

# Generate fixed-width file
generate_fixed_width_file('input_data.txt', 'output_fixed_width.txt')

# Parse fixed-width file to CSV
parse_fixed_width_to_csv('output_fixed_width.txt', 'output.csv')
