"""
Created on Oct 30, 2016

@author: mvoitko
"""
import csv

from src import config


def read_file(path=config.path_to_users, delimeter=','):
    """
    Check if email is in CSV file.
    :type list: [row0, row1, ...]
    """
    rows = []
    with open(path, 'r') as f:
        for row in csv.reader(f, delimiter=delimeter):
            rows.append(row)
    return rows


def whether_in_file(email, rows):
    """
    Check if email is in CSV file.
    :type boolen:
    """
    is_in_file = False
    for row in rows:
        if email.lower() == row[0].lower():
            is_in_file = True
            break
    return is_in_file


def form_dict_from_file(rows, key_column=0, value_column=1):
    """
    Parse credentials from CSV file to dictionary.
    :type dict: {email:password}
    """
    user_dictionary = {}
    for row in rows:
        user_dictionary[row[key_column]] = row[value_column]
    return user_dictionary

def get_user_credentials(email, rows):
    """
    Parse credentials from CSV file to dictionary.
    Generators
    :type dict: {email:password}
    """
    for row in rows:
        yield {row[0], row[1]}
