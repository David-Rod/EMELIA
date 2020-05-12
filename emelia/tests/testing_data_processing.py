import unittest
import sys
sys.path.append('../')

# Importing should work if python within conda env is utilized, not machine
from data_processing import DataProcessor

# Use test ticket data files to initialize the class object
dp = DataProcessor('test_alarm.csv', 'test_ticketdata.csv')


class TestDataProcessing(unittest.TestCase):

    def test_get_associated_hex_vals(self):
        obs = dp.get_associated_hex_vals('1076556')

        self.assertFalse([], obs)
        self.assertIn('0x47E060D', obs[1])

    def test_list_creation(self):
        list_of_alarms = dp.make_alarm_hex_master_set()
        list_of_ids = dp.make_incident_id_master_set()

        id_list = ['1076535', '1076543', '1076544', '1076548', '1076552',
                   '1076553', '1076554', '1076555', '1076556']
        alarm_list = ['0x47E060D', '0x47E1006', '0x47E100E', '0x47E042D',
                      '0x47E0822']

        self.assertEqual(list_of_alarms, sorted(alarm_list))
        self.assertEqual(list_of_ids, sorted(id_list))

        self.assertIsInstance(list_of_alarms, list)
        self.assertIsInstance(list_of_ids, list)

    def test_get_id_hex_set(self):
        obs = dp.get_alarm_file_incident_ids()
        exp = ['1076535', '1076543', '1076544', '1076548', '1076552',
               '1076553', '1076554', '1076555', '1076556']

        self.assertListEqual(obs, sorted(exp))

        self.assertNotIn('NULL', obs)
        self.assertNotIn('1076545', obs)

        self.assertIsInstance(obs, list)

    def test_remove_tickets_without_labels(self):
        id_label_feature_list = dp.create_id_label_feature_list()
        obs = dp.remove_tickets_without_labels(id_label_feature_list)

        self.assertFalse([], obs)

        self.assertNotIn('NULL', obs[0])

        self.assertIn('0x47E060D', obs[0][1])
        self.assertIn('Network Fault', obs[0][2])

    def test_encode_hex_values(self):
        dp = DataProcessor('test_alarm.csv', 'test_ticketdata.csv')
        id_label_feature_list = dp.get_hex_codes()

        obs = dp.encode_hex_values(id_label_feature_list[4])
        exp = [0, 0, 1, 0, 0]

        self.assertEqual(obs, exp)


if __name__ == '__main__':
    unittest.main()
