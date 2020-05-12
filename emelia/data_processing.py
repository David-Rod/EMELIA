import csv
import numpy as np


class DataProcessor:

    event_cause_vals = ['Random System Fault', 'Network Fault',
                        'Upgrade/Maintenance', 'Design Understanding',
                        'Design Problem', 'Environment or External', 'Induced',
                        'Informational', 'Documentation']
    detection_method = ['Polling', 'Trap', 'Call in/Email', 'GD Initiated']
    restore_method = ['GD Field Fix', 'CCC Fix', 'Non-GD Fix', 'Auto Fix',
                      'Not Applicable']
    fix_classification = ['HW Replaced', 'Configuration', 'HW Serviced/Reset',
                          'SW Restart', 'Not Applicable', 'Undetermined']
    subsystem = ['Network', 'DF LOBs & Caller Position',
                 'Workstation/Server HW', 'DSC & V4 HW/SW', 'RF Hardware',
                 'Infrastructure', 'Peripherals', 'Encrypted Comms',
                 'Archive Subsystem', 'CG IA', 'No Subsystem']
    relevance = ['Equipment', 'Coast Guard', 'Disaster']

    def __init__(self, alarm_file, ticket_file):
        self.alarm_file = alarm_file
        self.ticket_file = ticket_file

    # This function iterates through the alarm data to create a master set of
    # alarm code values. This set will be used as input for the NN
    def make_alarm_hex_master_set(self):
        alarm_hex_master = set()

        with open(self.alarm_file, encoding='utf8') as csv_file:
            csv_reader = csv.reader(csv_file)
            # Skip first row in the file
            next(csv_reader)
            for row in csv_reader:
                if row[3] != "NULL" and row[3] != 'alarm_type_hex':
                    alarm_hex_master.add(row[3])

        return sorted(alarm_hex_master)

    # This function iterates through the ticket data file to create set of
    # incident ID values that will be used to get corresponding hex values
    def make_incident_id_master_set(self):
        incident_id_master = set()

        with open(self.ticket_file, encoding='utf8') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for row in csv_reader:
                if row[0] != "NULL":
                    incident_id_master.add(row[0])

        return sorted(incident_id_master)

    # Returns list of 0's that has a length of n
    def zerolistmaker(self, n):
        listofzeros = [0] * n

        return listofzeros

    # Function that creates a set of the incident ID's in the alarm file
    def get_alarm_file_incident_ids(self):
        result_set = set()

        with open(self.alarm_file, encoding='utf8') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for row in csv_reader:
                result_set.add(row[0])

        return sorted(result_set)

    # Function will iterate through the set of incident ID's in the alarm file
    # and the incident ID's in the ticket file. If there is a match, it is
    # added to the set. The set is a union of ID's in both files
    def get_id_hex_set(self):
        result_set = set()
        ticket_id_set = self.make_incident_id_master_set()
        incident_id_in_alarm_file = self.get_alarm_file_incident_ids()
        for item in ticket_id_set:
            for value in incident_id_in_alarm_file:
                if item == value:
                    result_set.add(str(item))

        return sorted(result_set)

    # Function associates all related alarm values for an incident ID. Store
    # the result in a list
    def get_associated_hex_vals(self, id_val):
        id_and_hex_list = []
        id_and_hex_list.append(str(id_val))
        hex_val_set = set()
        with open(self.alarm_file, encoding='utf8') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for row in csv_reader:
                if str(id_val) in row and row[3] != 'NULL':
                    hex_val_set.add(str(row[3]))
            id_and_hex_list.append(sorted(hex_val_set))

        return id_and_hex_list

    # This will create a 2-D matrix with incident ids mapped to corresponding
    # alarm hex values
    def make_incident_id_to_alarm_hex_list(self):
        result_list = []
        set_of_ids = self.get_id_hex_set()

        for values in set_of_ids:
            result_list.append(self.get_associated_hex_vals(values))

        return result_list

    # Function to ensure that all the label options for a ticket are not NULL
    # This function returns none if the counter equals the number of labels
    # Helper function for create_ticket_data_list()
    def check_for_valid_labels(self, row_values):
        null_counter = 0
        end = len(row_values)
        start = end - 6
        for label in row_values[start:end]:
            if label == 'NULL':
                null_counter += 1
        # If none of the labels are a NULL value
        if null_counter == 0:
            return row_values

    # Function iterates through the ticket data in a given csv file and stores
    # the ticket data in an array. If the row_value is None, it will not add
    # that data. This should still work for create_id_label_feeature_list(),
    # since that function is dependent on the return from this function
    def create_ticket_label_list(self):
        ticket_data = []
        with open(self.ticket_file, encoding='utf8') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                row_value = self.check_for_valid_labels(row)
                if row_value is not None and len(row_value) > 2:
                    ticket_data.append(row)

        return ticket_data

    # Function that will add the labels(class values) to a list that contains
    # ID and hex codes. Returns list containing ID's, features, and labels
    # (Example: [id, [hex_vals], [labels]]
    def create_id_label_feature_list(self):
        id_hex_list = self.make_incident_id_to_alarm_hex_list()
        ticket_label_list = self.create_ticket_label_list()
        for data in id_hex_list:
            for ticket in ticket_label_list:
                end = len(ticket)
                start = end - 6
                if data[0] == ticket[0]:
                    data.append(ticket[start:end])

        return id_hex_list

    def remove_tickets_without_labels(self, ticket_array_values):
        ticket_id_hex_label_arr = []
        for ticket in ticket_array_values:
            if len(ticket) > 2:
                ticket_id_hex_label_arr.append(ticket)

        return ticket_id_hex_label_arr

    # Gets the hex codes in the master array at index 1, and makes a result
    # list that contains all of the hex values for each ticket
    def get_hex_codes(self):
        ticket_arr = self.create_id_label_feature_list()
        valid_ticket_with_labels = \
            self.remove_tickets_without_labels(ticket_arr)
        result_list = []
        # for values in ticket_arr:
        for values in valid_ticket_with_labels:
            hex_vals = values[1]
            result_list.append(hex_vals)

        return result_list

    # This function will accept the array of values, from get_hex_codes, and
    # return an array of 0 and 1 depending on the hex values present in the
    # array. The length will be same as length of alarm master set
    def encode_hex_values(self, data_arr):
        hex_list = list(self.make_alarm_hex_master_set())
        list_len = len(hex_list)
        temp_list = self.zerolistmaker(list_len)
        for index in range(len(hex_list)):
            if hex_list[index] in data_arr:
                temp_list[index] = 1

        return temp_list

    # Iterates through each hex_arr in get_hex_codes and will encode the data
    # as an array of 0 and 1 for each ticket, creates list the length of all
    # alarm hex values that are encoded for each ticket shared between tables
    def encode_ticket_hex_codes(self):
        result_list = []
        for hex_arr in self.get_hex_codes():
            result_list.append(self.encode_hex_values(hex_arr))

        return result_list

    # Gets all of the values from the master array at index 2, and makes a
    # result list that contains all of the label options for each ticket. The
    # result is the list of options related to the shared tickets
    def get_label_options(self):
        invalid_ticket_arr = self.create_id_label_feature_list()
        ticket_arr = self.remove_tickets_without_labels(invalid_ticket_arr)
        result_list = []
        for values in ticket_arr:
            label_vals = values[2]
            result_list.append(label_vals)

        return result_list

    # Encodes event cause and returns an array the length of event_cause_vals
    def encode_labels(self, label_arr, value):
        list_len = len(label_arr)
        temp_list = self.zerolistmaker(list_len)
        for option in range(len(label_arr)):
            if value == label_arr[option]:
                temp_list[option] = 1
            else:
                temp_list[option] = 0

        return temp_list

    # Target the specific index value inside the label array, within the array
    # of incident ID, [hex_vals], [label option] --> This retrieves event cause
    # labels
    def get_encoded_label_value(self, label_arr, label_index_pos):
        index_val = label_index_pos
        option_list = self.get_label_options()
        result_list = []
        for values in option_list:
            result_list.append(self.encode_labels(label_arr,
                               values[index_val]))

        return result_list

    # Takes in a data set and writes that set, line by line, to the filename
    def write_to_file(self, data, filename):
        with open(filename, 'w') as result_file:
            try:
                for row in data:
                    result_file.write("%s\n" % row)
            except Exception:
                raise ValueError("Failed to write to file. File may be empty.")

    # Converts list of input data to numpy array of type int
    def convert_array_to_np_array(self, input_data):
        numpy_array = np.array(input_data)
        numpy_array = numpy_array.astype(int)

        return numpy_array
