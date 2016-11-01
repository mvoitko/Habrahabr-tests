"""
Created on Oct 30, 2016

@author: mvoitko
"""
import csv
from datetime import datetime
import locale

from src import config

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

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

def capitilize(word):
    """
    Capitilize credentials from CSV file to dictionary.
    :param date_string: str - str with post timestamp
    :return : str - converted string for parsing
    """
    return word[0].upper() + word[1:]


def convert_date_string_for_parsing(date_string):
    """
    Cobvert date string in format .
    :param date_string: str - str with post timestamp
    :return : str - converted string for parsing
    """
    date_string_list = date_string.split(' ')
    date_string_list.remove(u'в')
    # date_string_list[1] = capitilize(date_string_list[1])

    if date_string_list[0] == 'сегодня': # handling 'сегодня в 19:27' case
        date_string_list[0] = str(datetime.today().strftime('%d'))
        date_string_list[1] = str(datetime.today().strftime('%B'))
        date_string_list[2] = str(datetime.today().strftime('%Y'))

    elif date_string_list[0] == 'вчора': # handling 'вчера в 19:27' case
        yesterday = datetime.today() - 1
        date_string_list[0] = str(yesterday.strftime('%d'))
        date_string_list[1] = str(yesterday.strftime('%B'))
        date_string_list[2] = str(yesterday.strftime('%Y'))

    else:
        if date_string_list[1] == 'Мая':
            date_string_list[1] = 'Mай'
        if len(date_string_list) == 3:  # handling '28 октября в 19:27' case
            date_string_list.insert(2, str(datetime.today().year))

    if date_string_list[0] == 1: # handling 1 digit day case
        date_string_list[0] += '0'

    date_string_list[1] = date_string_list[1][:3]
    print(datetime.today().strftime('%d %b %Y %H:%M'))
    print(' '.join(date_string_list))
    return ' '.join(date_string_list)

def parse_date(date_string, date_format="%d %b %Y %H:%M"):
    """
    Parse credentials from CSV file to dictionary.
    :type date_string: str - str with post timestamp
    :type date_format: str - str with date format for parsing
    """
    converted_string = convert_date_string_for_parsing(date_string)
    return datetime.strptime(converted_string, date_format)
    print (datetime.strptime(converted_string, date_format))

    '01 Ноябрь 2016 15:19'
    '17 Июля 2015 19:21'

    print(parse_date('17 Июля 2015 19:21', '%d %B %Y %H:%M'))