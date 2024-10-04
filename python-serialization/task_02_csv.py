#!/usr/bin/python3
"""Module that is reading data from one format
(CSV) and converting it into another
format (JSON) using serialization techniques"""


import csv
import json


def convert_csv_to_json(csv_file, json_file="data.json"):
    """Method that converts csv data to json easy readinf file,
     using DictReader to read csv data as a dictionnary """
    data = {}
    with open(csv_file, encoding="utf-8") as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
            """iterating each rows"""
            keys = rows['name']
            """sets a primary key for each rows"""
            data[keys] = rows
            """stocks each rows as values in dictionnary"""

    with open(json_file, mode="w", encoding="utf-8")as jsonf:
        json.dump(data, jsonf)
