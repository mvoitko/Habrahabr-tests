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

pattern_today = '(сегодня)\s(в)\s[0-9]{1,2}:[0-9]{2}'
pattern_yesterday = '(вчера)\s(в)\s[0-9]{1,2}:[0-9]{2}'
pattern_current_year = '^([0-3]?[0-9])+\s([а-я]{3,8})\s[в]\s(\d{2}:\d{2})$'
pattern_full = '^([0-3]?[0-9])+\s([а-я]{3,8})\s\d{4}\s[в]\s(\d{2}:\d{2})$'


def read_file(path=config.path_to_users, delimeter=','):
    """
    Check if email is in CSV file.
    :param path: path to csv file
    :param delimeter: delimeter in csv file
    :return: rows: list of csv file rows [row0, row1, ...]
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
    :return: is_in_file: boolen
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
    :return: user_dictionary: dict - dictionary {key:value}
    """
    user_dictionary = {}
    for row in rows:
        user_dictionary[row[key_column]] = row[value_column]
    return user_dictionary


def parse_today(date_string, date_format='%d %b %Y %H:%M'):
    """
    Parse date string to datetime object.
    Example:
    date_string: 'сегодня в 13:30'
    :type date_string: str - str with post timestamp
    :type date_format: str - str with date format for parsing
    :return: datetime object
    """
    converted_string = re.sub('(сегодня)\s(в)', date_string,
                              str(datetime.today().strftime('%d %B %Y')))
    month_re = re.search('([а-я]{3,8})', converted_string, re.IGNORECASE)
    month = month_re.group(0)
    converted_string = converted_string.replace(month, month[:3])
    return datetime.strptime(converted_string, date_format)


def parse_yesterday(date_string, date_format='%d %b %Y %H:%M'):
    """
    Parse date string to datetime object.
    Example:
    date_string: 'вчера в 09:11'
    :type date_string: str - str with post timestamp
    :type date_format: str - str with date format for parsing
    :return: datetime object
    """
    yesterday = datetime.today() - timedelta(day=1)
    converted_string = re.sub('(вчера)\s(в)', date_string,
                                yesterday.strftime('%d %B %Y'))
    month_re = re.search('([а-я]{3,8})', converted_string, re.IGNORECASE)
    month = month_re.group(0)
    converted_string = converted_string.replace(month, month[:3])
    return datetime.strptime(converted_string, date_format)


def parse_current_year(date_string, date_format='%d %b %Y %H:%M'):
    """
    Parse date string to datetime object.
    Example:
    date_string: '1 марта в 06:59'
    :type date_string: str - str with post timestamp
    :type date_format: str - str with date format for parsing
    :return: datetime object
    """
    converted_string = re.sub('\s(в)', date_string,
                              datetime.today().strftime('%Y'))
    month_re = re.search('([а-я]{3,8})', converted_string, re.IGNORECASE)
    month = month_re.group(0)
    converted_string = converted_string.replace(month, month[:3])
    if u'мая' in converted_string:
        converted_string = converted_string.replace(u'мая', u'май')
    return datetime.strptime(converted_string, date_format)


def parse_full(date_string, date_format='%d %b %Y %H:%M'):
    """
    Parse date string to datetime object.
    Example:
    date_string: '17 ноября 2015 в 12:01'
    :type date_string: str - str with post timestamp
    :type date_format: str - str with date format for parsing
    :return: datetime object
    """
    converted_string = date_string.replace('в ', '')
    month_re = re.search('([а-я]{3,8})', converted_string, re.IGNORECASE)
    month = month_re.group(0)
    converted_string = converted_string.replace(month, month[:3])
    if u'мая' in converted_string:
        converted_string = converted_string.replace(u'мая', u'май')
    return datetime.strptime(converted_string, date_format)


def format_month(date_string, month_regexp='([а-я]{3,8})'):
    """
    Format month in string for parsing.
    :type date_string: str - str with post timestamp
    :return: converted_string: str - with formatted month
    """
    month_re = re.search(month_regexp, date_string, re.IGNORECASE)
    month = month_re.group(0)
    converted_string = date_string.replace(month, month[:3])
    if u'мая' in converted_string:
        converted_string = converted_string.replace(u'мая', u'май')
    return converted_string
