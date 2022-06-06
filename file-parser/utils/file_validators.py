import json
import csv


def validate_json_file(file):
    # Validates JSON file
    try:
        with open(file, 'r') as f:
            json.load(f)
        return True
    except:
        return False


def validate_csv_file(file):
    # Validates CSV file
    try:
        with open(file, 'r') as f:
            csv.DictReader(f)
        return True
    except:
        return False
