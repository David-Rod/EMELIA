import csv
# import pandas as pd

'''
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
'''
# data = pd.read_csv('ticketdata/alarm.csv')
# alarm_values = pd.DataFrame()


def make_alarm_hex_master_set():
    alarm_hex_master = set()

    with open('alarm.csv', encoding='utf8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            if row[3] != "NULL":
                alarm_hex_master.add(row[3])

    return alarm_hex_master


def make_incident_id_master_set():
    incident_id_master = set()

    with open('ticketdata.csv', encoding='utf8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            if row[0] != "NULL":
                incident_id_master.add(row[0])

    return incident_id_master


def get_alarm_file_incident_ids():
    incident_id_master = set()

    with open('alarm.csv', encoding='utf8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            incident_id_master.add(row[0])

    return incident_id_master


def get_id_hex_set():
    result_set = set()
    ticket_id_set = make_incident_id_master_set()
    incidents_in_alarm_file = get_alarm_file_incident_ids()
    for item in ticket_id_set:
        for value in incidents_in_alarm_file:
            if item == value:
                result_set.add(item)

    return result_set


def get_associated_hex_vals(id_val):
    id_and_hex_list = []
    id_and_hex_list.append(id_val)
    with open('alarm.csv', encoding='utf8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            if str(id_val) in row:
                id_and_hex_list.append(row[3])

    return id_and_hex_list


# This will create a 2-D matrix with incident ids mapped to corresponding
# alarm hex values

def make_incident_id_to_alarm_hex_list():
    result_list = []
    set_of_ids = get_id_hex_set()
    '''
    with open('alarm.csv', encoding='utf8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            if row[0] in set_of_ids:
                result_list.append(get_associated_hex_vals(row[0]))

    '''
    for values in set_of_ids:
        result_list.append(get_associated_hex_vals(values))

    return sorted(result_list)


result = make_incident_id_to_alarm_hex_list()


with open('result_file.txt', mode='w') as result_file:
    for item in result:
        result_file.write("%s\n" % item)

for items in result:
    print(str(items) + "\n")
