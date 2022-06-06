import json
import csv


def parse_csv(file):
    # Parses CSV file
    with open(file, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)


def parse_json(file):
    # Parses JSON file
    with open(file, 'r') as f:
        return json.load(f)
