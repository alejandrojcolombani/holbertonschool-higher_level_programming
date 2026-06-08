#!/usr/bin/env python3
"""Module that converts CSV data to JSON."""

import csv
import json


def convert_csv_to_json(filename):
    """Convert a CSV file to JSON and save it as data.json."""
    try:
        with open(filename, "r", encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

        return True

    except FileNotFoundError:
        return False
