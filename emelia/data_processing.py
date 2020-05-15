import csv
import numpy as np


class DataProcessor:

    # Class member arrays that store labels available for each classification
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

    # Constructor that accepts alarm and ticket file to initialize object
    def __init__(self, alarm_file, ticket_file):
        self.alarm_file = alarm_file
        self.ticket_file = ticket_file

    def make_alarm_hex_master_set(self):
        '''
        Function iterates through the alarm data to create a master set of
        alarm code values. This set will aid in formatting input to be used
        for the learning model.

                Returns: sorted set
        '''

        alarm_hex_master = set()

        with open(self.alarm_file, encoding='utf8') as csv_file:
            csv_reader = csv.reader(csv_file)
            # Skip first row in the file
            next(csv_reader)
            for row in csv_reader:
                if row[3] != "NULL" and row[3] != 'alarm_type_hex':
                    alarm_hex_master.add(row[3])

        return sorted(alarm_hex_master)

    def make_incident_id_master_set(self):
        '''
        This function iterates through the ticket data file to create set of
        incident ID values that will be used to get corresponding hex values.

                Returns: sorted set
        '''

        incident_id_master = set()

        with open(self.ticket_file, encoding='utf8') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for row in csv_reader:
                if row[0] != "NULL":
                    incident_id_master.add(row[0])

        return sorted(incident_id_master)

    def zerolistmaker(self, n):
        '''
        Returns list of zeros that has a length of argument 'n'.

                Parameters:
                    n: (int) number of values that determine length of
                       resulting array
        '''

        listofzeros = [0] * n

        return listofzeros

    def get_alarm_file_incident_ids(self):
        '''
        Function that creates a set of the incident ID's from the incident ID's
        in the alarm file.

                Returns: sorted set
        '''
        result_set = set()

        with open(self.alarm_file, encoding='utf8') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for row in csv_reader:
                result_set.add(row[0])

        return sorted(result_set)

    def get_id_hex_set(self):
        '''
        Function will iterate through the set of incident ID's in the alarm
        file and the incident ID's in the ticket file. If there is a match, it
        is added to the set. The set is a union of ID's in both files.

                Returns: sorted set
        '''

        result_set = set()
        ticket_id_set = self.make_incident_id_master_set()
        incident_id_in_alarm_file = self.get_alarm_file_incident_ids()
        for item in ticket_id_set:
            for value in incident_id_in_alarm_file:
                if item == value:
                    result_set.add(str(item))

        return sorted(result_set)

    def get_associated_hex_vals(self, identifier):
        '''
        Function associates all related alarm values for an incident ID. Store
        the result in a list.

                Returns: ID and hex list

                Parameters:
                    identifier: incident ID value to associate with
                                corresponding hex values
        '''

        id_and_hex_list = []
        id_and_hex_list.append(str(identifier))
        hex_val_set = set()

        with open(self.alarm_file, encoding='utf8') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for row in csv_reader:
                if str(identifier) in row and row[3] != 'NULL':
                    hex_val_set.add(str(row[3]))
            id_and_hex_list.append(sorted(hex_val_set))

        return id_and_hex_list

    def make_incident_id_to_alarm_hex_list(self):
        '''
        Function creates a 2-D matrix with incident ID's mapped to
        corresponding alarm hex values.

                Returns: 2-D matrix of associated hex values
        '''
        result_list = []
        set_of_ids = self.get_id_hex_set()

        for values in set_of_ids:
            result_list.append(self.get_associated_hex_vals(values))

        return result_list

    def check_for_valid_labels(self, row):
        '''
        Function to ensure that all the label options for a ticket do not
        contain NULL as a value. Helper function for create_ticket_data_list().

                Returns: none if the counter equals greater than zero,
                         otherwise returns row of data

                Parameters:
                    row: row of values that in 2-D matrix of associated ticket
                         to alarm data
        '''

        null_counter = 0
        end = len(row)
        start = end - 6
        for label in row[start:end]:
            if label == 'NULL':
                null_counter += 1
        # If none of the labels are a NULL value
        if null_counter == 0:
            return row

    def create_ticket_label_list(self):
        '''
        Function iterates through the ticket data in a given csv file and
        stores the ticket data in an array. If the row_value is None, it will
        not add that data.

                Returns: (list) ticket data
        '''

        ticket_data = []
        with open(self.ticket_file, encoding='utf8') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                row_value = self.check_for_valid_labels(row)
                if row_value is not None and len(row_value) > 2:
                    ticket_data.append(row)

        return ticket_data

    def create_id_label_feature_list(self):
        '''
        Function that will add the classification labels to a list that
        contains ID and hex codes.

                Returns: (list) incident ID's, hex values, and labels
        '''

        id_hex_list = self.make_incident_id_to_alarm_hex_list()
        ticket_label_list = self.create_ticket_label_list()

        for data in id_hex_list:
            for ticket in ticket_label_list:
                end = len(ticket)
                start = end - 6
                if data[0] == ticket[0]:
                    data.append(ticket[start:end])

        return id_hex_list

    def remove_tickets_without_labels(self, arr):
        '''
        Ensures that all rows contain label values.

                Returns: (list) rows that have valid labels associated
                         with each ticket

                Parameters:
                    arr: row of data in 2-D matrix of data in function above
        '''

        ticket_id_hex_arr = []
        for ticket in arr:
            if len(ticket) > 2:
                ticket_id_hex_arr.append(ticket)

        return ticket_id_hex_arr

    def get_hex_codes(self):
        '''
        Gets the hex codes in the master array at index 1.

                Returns: (list) all of the hex values for each ticket
        '''

        ticket_arr = self.create_id_label_feature_list()
        valid_ticket_with_labels = \
            self.remove_tickets_without_labels(ticket_arr)
        result_list = []

        for values in valid_ticket_with_labels:
            hex_vals = values[1]
            result_list.append(hex_vals)

        return result_list

    def encode_hex_values(self, arr):
        '''
        This function will accept array of values and returns an array of 0
        and 1 depending on the hex value present position in the array. The
        length will be same as length of alarm master set.

                Returns: (list) of encoded values containing 1's or 0's

                Parameters:
                    arr: array of values from get_hex_codes() function
        '''
        hex_list = list(self.make_alarm_hex_master_set())
        list_len = len(hex_list)
        temp_list = self.zerolistmaker(list_len)
        for index in range(len(hex_list)):
            if hex_list[index] in arr:
                temp_list[index] = 1

        return temp_list

    def encode_ticket_hex_codes(self):
        '''
        Function iterates through each hex_arr in get_hex_codes and will encode
        the data as an array of 0 and 1 for each ticket
        (calls encode_hex_values). Result is a list the length of all
        alarm hex values that are encoded for each ticket.

                Returns: (list) encoded hex codes for all tickets
        '''

        result_list = []
        for hex_arr in self.get_hex_codes():
            result_list.append(self.encode_hex_values(hex_arr))

        return result_list

    def get_label_options(self):
        '''
        Function accesses values in the master array at index 2, and makes a
        result list that contains all of the label options for each ticket. The
        result is the list of options related to the shared tickets.

                Returns: (list) values that contain label values for tickets
        '''

        invalid_ticket_arr = self.create_id_label_feature_list()
        ticket_arr = self.remove_tickets_without_labels(invalid_ticket_arr)
        result_list = []

        for values in ticket_arr:
            label_vals = values[2]
            result_list.append(label_vals)

        return result_list

    def encode_labels(self, arr, value):
        '''
        Function encodes arr at the specified index.

                Returns: (list) encoded array the length of the specified label
                         array

                Parameters:

                    arr: array of labels (label option) in the master array
                         of data
                    value: index position within arr
        '''

        list_len = len(arr)
        temp_list = self.zerolistmaker(list_len)
        for option in range(len(arr)):
            if value == arr[option]:
                temp_list[option] = 1
            else:
                temp_list[option] = 0

        return temp_list

    def get_encoded_label_value(self, arr, pos):
        '''
        Function retrieves value of specific index inside the label array,
        within the array of [incident ID, [hex_vals], [label option]].

                Returns: (list) containing encoded values.

                Parameters:
                    arr: array of labels (label option) in the master array
                         of data
                    pos: index position within arr
        '''

        index_val = pos
        option_list = self.get_label_options()
        result_list = []

        for values in option_list:
            result_list.append(self.encode_labels(arr,
                               values[index_val]))

        return result_list

    def write_to_file(self, data, filename):
        '''
        Function accepts list of data and filename to write output. Result is
        the creation of file in the current directory with data.

                Parameters:
                    data: list of data to write to filename
                    filename: name of the file to store resulting data
        '''

        with open(filename, 'w') as result_file:
            try:
                for row in data:
                    result_file.write("%s\n" % row)
            except Exception:
                raise ValueError("Failed to write to file. File may be empty.")

    def convert_array_to_np_array(self, data):
        '''
        Converts list of input data to numpy array of type int. Returns array
        as numpy array.

                Parameters:
                    data: list containing data corrsesponding to each ticket
        '''
        numpy_array = np.array(data)
        numpy_array = numpy_array.astype(int)

        return numpy_array
