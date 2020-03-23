import unittest
import data_processing
import numpy as np

def list_strict_equal (list_one, list_two):
    for item in list_one:
        item_location = list_one.index(item)
        if (item != list_two[item_location]):
            return False

    return True

class MyTest(unittest.TestCase):
    # Tests the creation of the alarm hex master set
    def test_make_alarm_hex_master_set(self):
        master_list = ['30914', '67686', '50622', '36065', '20603', '65428', '84563', '23510', '75065', '60039', '90540', '46457', '7353', '38977', '65266', '6984', '89453', '23086', '89583', '76909', '3892', '16898', '53811' ] # master test array
        master_list.sort() # sort the master test array
        empty_list = [] # empty array
        result = data_processing.make_alarm_hex_master_set() # test the function call
        self.assertEqual(len(result), len(master_list)) # the resulting list should have the same length as the master list
        self.assertFalse(len(result) == 25) # the resulting length should not be equal to the input length
        self.assertEqual(result, master_list) # check to ensure that no values are missing
        self.assertFalse(result == empty_list) # the resulting list should not be empty
        self.assertTrue(list_strict_equal(master_list, result)) # the resulting array should be sorted

    def test_get_alarm_file_incident_ids(self):
        incident_list = ['844959', '63955', '472910', '55762', '820447', '645022', '961690', '468249', '686822', '65014', '279819', '770915', '335436', '975290', '634412', '653117', '842937', '794241', '892720', '765948', '851897', '791273', '807302', '938463' ]
        incident_list.sort() # sort the incident test array
        empty_list = [] # empty array
        output = data_processing.get_alarm_file_incident_ids() # test the function call
        self.assertEqual(len(output), len(incident_list)) # the resulting list should have the same length as the incident list
        self.assertFalse(len(output) == 25) # the resulting length should not be equal to the input length
        self.assertEqual(output, incident_list) # check to ensure that no values are missing
        self.assertFalse(output == empty_list) # the resulting list should not be empty
        self.assertTrue(list_strict_equal(incident_list, output)) # the resulting array should be sorted

    def test_get_id_hex_set(self):
        incident_matching_list = ['63955', '472910', '55762', '820447', '645022', '961690', '468249', '686822', '65014', '279819', '770915', '335436', '975290', '634412', '653117', '842937', '794241', '892720', '765948', '851897', '791273', '807302', '938463']
        incident_matching_list.sort() # sort the incident matching test array
        empty_list = [] # empty array
        output = data_processing.get_id_hex_set() # test the function call
        self.assertEqual(len(output), len(incident_matching_list)) # the resulting list should have the same length as the incident matching list
        self.assertEqual(output, incident_matching_list) # check to ensure that no values are missing
        self.assertFalse(output == empty_list) # the resulting list should not be empty
        self.assertTrue(list_strict_equal(incident_matching_list, output)) # the resulting array should be sorted

    def test_make_incident_id_to_alarm_hex_list(self):
        incident_id_with_hex_list = [['279819', ['90540']], ['335436', ['7353']], ['468249', ['23510']], ['472910', ['50622']], ['55762', ['36065']], ['634412', ['65266']], ['63955', ['30914', '67686']], ['645022', ['65428']], ['65014', ['60039']], ['653117', ['6984']], ['686822', ['75065']], ['765948', ['76909']], ['770915', ['46457']], ['791273', ['16898']], ['794241', ['23086']], ['807302', ['53811']], ['820447', ['20603']], ['842937', ['89453']], ['851897', ['3892']], ['892720', ['89583']], ['938463', []], ['961690', ['84563']], ['975290', ['38977']]]
        empty_list = [] # empty array
        output = data_processing.make_incident_id_to_alarm_hex_list() # test the function call
        self.assertEqual(len(output), len(incident_id_with_hex_list)) # the resulting list should have the same length as the incident to hex list
        self.assertEqual(output, incident_id_with_hex_list) # check to ensure that no values are missing
        self.assertFalse(output == empty_list) # the resulting list should not be empty
        self.assertTrue(list_strict_equal(incident_id_with_hex_list, output)) # the resulting array should be sorted

    def test_encoding_functions(self): # encode_hex_values(arr), zerolistmaker(n), and encode_ticket_hex_codes() work together
        one_hot_encode_test_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        empty_list = [] # empty array
        output = data_processing.encode_ticket_hex_codes() # test the function call
        self.assertEqual(len(output), len(one_hot_encode_test_list)) # the resulting list should have the same length as one hot encoded list
        self.assertEqual(output, one_hot_encode_test_list) # check to ensure that no values are missing
        self.assertFalse(output == empty_list) # the resulting list should not be empty
        self.assertTrue(list_strict_equal(one_hot_encode_test_list, output)) # the resulting array should be sorted

    #def test_get_event_cause_val(self): Do I need to test this one?

if __name__ == '__main__':
    unittest.main()