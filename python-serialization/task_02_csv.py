#!/usr/bin/python3
"""Module that is reading data from one format
(CSV) and converting it into another
format (JSON) using serialization techniques"""


import csv
import json


def convert_csv_to_json(csv_file, json_file="data.json"):
    """Method that converts csv data to json easy reading file,
    using DictReader to read csv data as a dictionnary

    args:
        csv_file: path to CSV file provided to converting data
        json_file: path to JSON file provided
        where data will be converted. data.json by default

    Returns:
        bool: returns True if conversion is a succes or
        False if there is an error

    Raises:
        FileNotFoundError and OSError
    """

    data = []
    try:
        with open(csv_file, encoding="utf-8") as csvf:
            csvReader = csv.DictReader(csvf)

            for rows in csvReader:
                """iterating each rows"""
                data.append(rows)
                """appends each rows to  data list of dictionnary"""

    except FileNotFoundError:
        print("Error: {} not found".format(csv_file))
        return False

    except OSError as e:
        print("Error while reading csv file {} ".format(e))
        return False

    try:
        with open(json_file, mode="w", encoding="utf-8") as jsonf:
            json.dump(data, jsonf, indent=4)
            return True

    except OSError as e:
        print("json file writing error : {}".format(e))
        return False
