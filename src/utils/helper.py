"""
Created on Oct 28, 2016

@author: mvoitko
"""
import csv

from src.config import *


def whether_in_file(email, path=path_to_users):
    """
    Check if email is in CSV file.
    :type boolen:
    """
    is_in_file = False
    with open(path, 'rt') as f:
         reader = csv.reader(f, delimiter=',')
         for row in reader:
              if email == row[0]:
                  is_in_file = True
    return is_in_file

def form_user_dict(path=path_to_users):
    """
    Parse credentials from CSV file to dictionary.
    Iterator
    :type dict: {email:password}
    """
    with open(path, 'rt') as f:
        user_dictionary = {}
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            user_dictionary[row[0]] = row[1]
    return user_dictionary

def get_user_password(email, path=path_to_users):
    """
    Parse credentials from CSV file to dictionary.
    Generators
    :type dict: {email:password}
    """
    user_dictionary = {}
    with open(path, 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            user_dictionary[row[0]] = row[1]
    yield user_dictionary[email]