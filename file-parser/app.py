import sys
import os
from utils.parser import parse_json, parse_csv
from utils.file_validators import validate_json_file, validate_csv_file

keys = []  # List of keys
data = []  # List of all parsed data

total_row_count = 0  # Total row count
combined_data = []  # List of all data
combined_unique_data = []  # List of unique data
common_keys = []  # List of common keys

paths = sys.argv  # List of paths to files

for path in paths:

    if os.path.isfile(path):
        # Print filename
        print("File found: " + path.split("/")[-1])

        # Get extension
        extension = path.split(".")[-1]

        # Validate and parse file
        if (extension == "json" and validate_json_file(path)):
            parsed_data = parse_json(path)
            data.append(parsed_data)
            keys.append(parsed_data[0].keys())

        elif (extension == "csv" and validate_csv_file(path)):
            parsed_data = parse_csv(path)
            data.append(parsed_data)
            keys.append(parsed_data[0].keys())

        else:
            print("File invalid or extension not supported\n")

    else:
        print('No such file: ' + path + '\n')


# Get the common keys for comparison
if len(keys):
    # Find common keys
    common_keys = set.intersection(*map(set, keys))

    if len(common_keys):
        # Print common keys
        print("Common keys: " + str(common_keys))
    else:
        print("Data not similar to compare")

else:
    print("No valid files found")

# Make comparisons between data using common keys
if len(common_keys):
    for data_set in data:
        for data_point in data_set:
            combined_data.append(dict((k, data_point[k]) for k in common_keys))

    for data_point in combined_data:
        if data_point not in combined_unique_data:
            combined_unique_data.append(data_point)

    total_row_count = len(combined_data)
    unique_row_count = len(combined_unique_data)

    # write to output files
    with open("combined_data.json", "w") as f:
        f.write(str(combined_unique_data))

    print("Total data count: " + str(total_row_count))
    print("Unique data count: " + str(unique_row_count))

else:
    print("No common keys found in data")
