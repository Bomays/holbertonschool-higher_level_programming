#!/usr/bin/python3
"""Module that is reading data from one format
(CSV) and converting it into another
format (JSON) using serialization techniques"""


import csv
import json
import os


def convert_csv_to_json(csv_file, json_file="data.json"):
    """Method that converts csv data to json easy reading file,
     using DictReader to read csv data as a dictionnary """
    if not os.path.exists(csv_file):
        print("Error: {} not found".format(csv_file))
        return False

    data = {}
    try:
        with open(csv_file, encoding="utf-8") as csvf:
            csvReader = csv.DictReader(csvf)

            for rows in csvReader:
                """iterating each rows"""
                keys = rows['name']
                """sets a primary key for each rows"""
                data[keys] = rows
                """stocks each rows as values in dictionnary"""

    except (OSError) as e:
        print("Error while readind {} ".format(e))
        return False
    
    try:
        with open(json_file, mode="w", encoding="utf-8")as jsonf:
            json.dump(data, jsonf, indent=4)
            return True

    except (OSError) as e:
        print("json file writing error : {}".format(e))
        return False
