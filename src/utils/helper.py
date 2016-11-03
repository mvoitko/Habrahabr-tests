"""
Created on Oct 30, 2016

@author: mvoitko
"""
import re
import csv
import locale
from datetime import datetime, timedelta

from src import config

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


def read_file(path=config.path_to_users, delimeter=','):
    """
    Check if email is in CSV file.
    :param path: path to csv file
    :param delimeter: delimeter in csv file
    :return rows: list of csv file rows [row0, row1, ...]
    """
    rows = []
    with open(path, 'r') as f:
        for row in csv.reader(f, delimiter=delimeter):
            rows.append(row)
    return rows


def whether_in_file(email, rows):
    """
    Check if email is in CSV file.
    :param email: str
    :param rows: list of csv file rows [row0, row1, ...]
    :param is_in_file: boolen
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
    :param rows: list of csv file rows [row0, row1, ...]
    :param key_column: int - column index
    :param value_column: int - column index
    :return user_dictionary: dict - dictionary {key:value}
    """
    user_dictionary = {}
    for row in rows:
        user_dictionary[row[key_column]] = row[value_column]
    return user_dictionary


def convert_date_string_for_parsing(date_string):
    """
    Convert date string in format .
    :param date_string: str - str with post timestamp
    :return : str - converted string for parsing
    """
    date_string_list = date_string.split(' ')
    date_string_list.remove(u'в')

    if date_string_list[0] == 'сегодня': # handling 'сегодня в 19:27' case
        date_string_list[0] = str(datetime.today().strftime('%d'))
        date_string_list[1] = str(datetime.today().strftime('%B'))
        date_string_list[2] = str(datetime.today().strftime('%Y'))

    elif date_string_list[0] == 'вчера':  # handling 'вчера в 19:27' case
        yesterday = datetime.today() - 1
        date_string_list[0] = str(yesterday.strftime('%d'))
        date_string_list[1] = str(yesterday.strftime('%B'))
        date_string_list[2] = str(yesterday.strftime('%Y'))

    else:
        if date_string_list[1] == 'мая':
            date_string_list[1] = 'май'
        if len(date_string_list) == 3:  # handling '28 октября в 19:27' case
            date_string_list.insert(2, str(datetime.today().year))

    date_string_list[1] = date_string_list[1][:3]
    print(' '.join(date_string_list))
    return ' '.join(date_string_list)


def parse_date(date_string, date_format="%d %b %Y %H:%M"):
    """
    Parse date from string to datetime object.
    :type date_string: str - str with post timestamp
    :type date_format: str - str with date format for parsing
    :return :datetime object
    """
    converted_string = convert_date_string_for_parsing(date_string)
    return datetime.strptime(converted_string, date_format)
    print(datetime.strptime(converted_string, date_format))

pattern_today = r'(сегодня)\s(в)\s[0-9]{1,2}:[0-9]{2}'
pattern_yesterday = r'(вчера)\s(в)\s[0-9]{1,2}:[0-9]{2}'
pattern_current_year = r'^([0-3]?[0-9])+\s([а-я]{3,8})\s[в]\s(\d{2}:\d{2})$'
pattern_full = r'^([0-3]?[0-9])+\s([а-я]{3,8})\s\d{4}\s[в]\s(\d{2}:\d{2})$'

def parse_today(date_string, date_format='%d %b %Y %H:%M'):
    converted_string = re.sub(r'(сегодня)\s(в)', date_string,
        str(datetime.today().strftime('%d %B %Y')))
    return datetime.strptime(converted_string, date_format)

def parse_yesterday(date_string, date_format='%d %b %Y %H:%M'):
    yesterday = datetime.today - timedelta(day=1)
    converted_string = re.sub(r'(вчера)\s(в)', date_string, yesterday.strftime('%d %B %Y'))
    return datetime.strptime(converted_string, date_format)

def parse_current_year(date_string, date_format='%d %b %Y %H:%M'):
    converted_string = re.sub(r'\s(в)', date_string, datetime.today.strftime('%Y'))
    return datetime.strptime(converted_string, date_format)

def parse_full(date_string, date_format='%d %b %Y %H:%M'):
    converted_string = date_string.remove(u'в ')
    return datetime.strptime(converted_string, date_format)