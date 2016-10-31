"""
Created on Oct 30, 2016

@author: mvoitko
"""
import csv

from src.config import *


def read_file(path=path_to_users, delimeter=','):
    """
    Check if email is in CSV file.
    :type list: [row0, row1, ...]
    """
    rows = []
    with open(path, 'r') as f:
        for row in csv.reader(f, delimiter=delimeter):
            rows.append(row)
    return rows

file_content = read_file()


def whether_in_file(email, rows=file_content):
    """
    Check if email is in CSV file.
    :type boolen:
    """
    is_in_file = False
    for row in rows:
        if email == row[0]:
            is_in_file = True
            break
    return is_in_file


def form_dict_from_file(key_column=0, value_column=1,
                        rows=file_content):
    """
    Parse credentials from CSV file to dictionary.
    :type dict: {email:password}
    """
    user_dictionary = {}
    for row in rows:
        user_dictionary[row[key_column]] = row[value_column]
    return user_dictionary

credentials = form_dict_from_file()
usernames = form_dict_from_file(0, 2)

def get_user_credentials(email):
    """
    Parse credentials from CSV file to dictionary.
    Generators
    :type dict: {email:password}
    """
    for row in rows:
        yield {row[0], row[1]}
