import csv
# import pandas as pd
# from sklearn.preprocessing import OneHotEncoder, LabelEncoder
'''
import numpy as np
import tensorflow as tf
from tensorflow import keras

from sklearn.compose import ColumnTransformer
'''


# This function iterates through the alarm data to create a master set of alarm
# code values. This set will be used as input for the NN
def make_alarm_hex_master_set():
    alarm_hex_master = set()

    with open('alarm.csv', encoding='utf8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            if row[3] != "NULL":
                alarm_hex_master.add(row[3])

    return sorted(alarm_hex_master)


# This function iterates through the ticket data file to create set of incident
# ID values that will be used to get corresponding hex values
def make_incident_id_master_set():
    incident_id_master = set()

    with open('ticketdata.csv', encoding='utf8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            if row[0] != "NULL":
                incident_id_master.add(row[0])

    return sorted(incident_id_master)


# Function that creates a set of the incident ID's in the alarm file
def get_alarm_file_incident_ids():
    result_set = set()

    with open('alarm.csv', encoding='utf8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            result_set.add(row[0])

    return sorted(result_set)


# Function will iterate through the set of incident ID's in the alarm file and
# the incident ID's in the ticket file. If there is a match, it is added to the
# set. The set is a union of ID's in both files
def get_id_hex_set():
    result_set = set()
    ticket_id_set = make_incident_id_master_set()
    incident_id_in_alarm_file = get_alarm_file_incident_ids()
    for item in ticket_id_set:
        for value in incident_id_in_alarm_file:
            if item == value:
                result_set.add(str(item))
    return sorted(result_set)


# Function associates all related alarm values for an incident ID. Store the
# result in a list
def get_associated_hex_vals(id_val):
    id_and_hex_list = []
    id_and_hex_list.append(str(id_val))
    hex_val_set = set()
    with open('alarm.csv', encoding='utf8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            if str(id_val) in row and row[3] != 'NULL':
                hex_val_set.add(str(row[3]))
        id_and_hex_list.append(sorted(hex_val_set))

    return id_and_hex_list


# This will create a 2-D matrix with incident ids mapped to corresponding
# alarm hex values
def make_incident_id_to_alarm_hex_list():
    result_list = []
    set_of_ids = get_id_hex_set()

    for values in set_of_ids:
        result_list.append(get_associated_hex_vals(values))

    return result_list


# Function that will add the labels(class values) to a list that contains
# ID and hex codes. Returns list containing ID's, features, and labels
# (Example: [id, [hex_vals], [labels]]
def create_id_label_feature_list():
    id_hex_list = make_incident_id_to_alarm_hex_list()
    ticket_data_list = create_ticket_data_list()
    for data in id_hex_list:
        for ticket in ticket_data_list:
            end = len(ticket)
            start = end - 6
            if data[0] == ticket[0]:
                data.append(ticket[start:end])

    return id_hex_list


# Function iterates through the ticket data in a given csv file and stores the
# ticket data in an array
def create_ticket_data_list():
    ticket_data = []
    with open('ticketdata.csv', encoding='utf8') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            ticket_data.append(row)

    return ticket_data


# Function that OneHot encodes the values in the list of data that contains
# ticketID, hex vals, label vals
'''
def one_hot_encode(ticket_arr, hex_vals):
    hex_list = sort(list(hex_vals))
    one_hot_hex_list= []
    temp_list = []
    for ticket_label in ticket_arr:
        for hex_val in hex_list[2]:
            print("Ticket Label: " + str(type(ticket_label)))
            print("Hex Val: " + str(type(hex_val)))
            if ticket_label == hex_val:
                temp_list.append(1.0)
            else:
                temp_list.append(0.0)
            one_hot_hex_list.append(temp_list)
            temp_list = []
    return one_hot_hex_list
    # TODO: implement OneHot encoding of my dataset
'''


def write_to_file(data, filename):
    with open(filename, 'w') as result_file:
        try:
            for row in data:
                result_file.write("%s\n" % row)
        except Exception:
            raise ValueError("Failed to write to file")


write_to_file(create_id_label_feature_list(), 'result_file.txt')
