import unittest
import data_processing

class TestDataProcessing(unittest.TestCase):

    alarm = 'testalarm.csv'

    ticket = 'testticket.csv'


    def test_make_alarm_hex_master_set(self):

        alarm_hex_master_set = data_processing.make_alarm_hex_master_set(self.alarm)

        alarm_hex_master_set_int = set(map(lambda x:int(x), alarm_hex_master_set))

        # check length 
        self.assertEqual(23, len(alarm_hex_master_set_int))

        # check max value
        self.assertEqual(3892, min(alarm_hex_master_set_int))

        # check min value
        self.assertEqual(90540, max(alarm_hex_master_set_int))


    def test_make_incident_id_master_set(self):

        incident_id_master_set = data_processing.make_alarm_hex_master_set(self.ticket)

        # check length 
        self.assertEqual(41, len(incident_id_master_set))

        # check exsitance 1
        self.assertTrue('STATION - CHANNEL ISLANDS HARBOR' in incident_id_master_set)

        # check exsitance 2
        self.assertTrue('RFF - ROBERTSDALE' in incident_id_master_set)

        # check exsitance 3
        self.assertTrue('STATION - RIO VISTA' in incident_id_master_set)


    def test_get_alarm_file_incident_ids(self):

        alarm_file_incident_ids = data_processing.get_alarm_file_incident_ids(self.alarm)

        alarm_file_incident_ids_int = list(map(lambda x:int(x), alarm_file_incident_ids))

        # check length 
        self.assertEqual(24, len(alarm_file_incident_ids_int))

        # check max value
        self.assertEqual(1, min(alarm_file_incident_ids_int))

        # check min value
        self.assertEqual(24, max(alarm_file_incident_ids_int))


    def test_get_id_hex_set(self):

        id_hex_set = data_processing.get_id_hex_set(self.alarm, self.ticket)

        self.assertEqual([], id_hex_set)


    def test_get_associated_hex_vals(self):
        
        # normal case
        self.assertEqual(['1', ['30914']],data_processing.get_associated_hex_vals(1, self.alarm))
        # NULL case
        self.assertEqual(['24', []],data_processing.get_associated_hex_vals(24, self.alarm))


    def test_make_incident_id_to_alarm_hex_list(self):

        incident_id_to_alarm_hex_list = data_processing.make_incident_id_to_alarm_hex_list(self.alarm, self.ticket)

        self.assertEqual([], incident_id_to_alarm_hex_list)


    def test_create_id_label_feature_list(self):
        
        id_label_feature_list = data_processing.create_id_label_feature_list(self.alarm, self.ticket)

        self.assertEqual([], id_label_feature_list)


    def test_create_ticket_data_list(self):

        ticket_data_list = data_processing.create_ticket_data_list(self.ticket)

        # check length 
        self.assertEqual(49, len(ticket_data_list))

        ticket_data_list_rff = set(map(lambda x:x[3], ticket_data_list))

        # check exsitance 1
        self.assertTrue('STATION - CHANNEL ISLANDS HARBOR' in ticket_data_list_rff)

        # check exsitance 2
        self.assertTrue('RFF - ROBERTSDALE' in ticket_data_list_rff)

        # check exsitance 3
        self.assertTrue('STATION - RIO VISTA' in ticket_data_list_rff)


    def test_get_hex_codes(self):

        hex_codes = data_processing.get_hex_codes(self.alarm,self.ticket)

        self.assertEqual([], hex_codes)


    def test_encode_hex_values(self):

        hex_list = ['16898', '20603', '23086', '23510', '30914', '36065', 
          '3892', '38977', '46457', '50622', '53811', '60039', '65266', '65428',
          '67686', '6984', '7353', '75065', '76909', '84563', '89453', '89583', '90540']

        hex_values = data_processing.encode_hex_values(hex_list, self.alarm)

        # check length
        self.assertEqual(len(hex_list), len(hex_values))

        # check encoding
        self.assertFalse(0 in hex_values)


    def test_encode_ticket_hex_codes(self):

        ticket_hex_codes = data_processing.encode_ticket_hex_codes(self.alarm, self.ticket)

        self.assertEqual([], ticket_hex_codes)


    def test_get_label_options(self):

        label_options = data_processing.get_label_options(self.alarm, self.ticket)

        self.assertEqual([], label_options)


    def test_encode_event_cause_options(self):
        
        encoded_event_cause_options_0 = data_processing.encode_event_cause_options('Random System Fault')

        # check place 0
        self.assertEqual([1, 0, 0, 0, 0, 0, 0, 0, 0],  encoded_event_cause_options_0)

        encoded_event_cause_options_3 = data_processing.encode_event_cause_options('Design Understanding')

        # check place 3
        self.assertEqual([0, 0, 0, 1, 0, 0, 0, 0, 0],  encoded_event_cause_options_3)


    def test_get_event_cause_val(self):

        event_cause_val = data_processing.get_event_cause_val(self.alarm, self.ticket)

        self.assertEqual([], event_cause_val)

    # Tests the creation of the alarm hex master set
    # def test_make_alarm_hex_master_set(self):
    #     result = data_processing.make_alarm_hex_master_set() # function call
    #     self.assertEqual(len(result), 74) # the resulting list should have a length of 7
    #     self.assertFalse(result == 1583) # the resulting length should not be equal to the input length ​
    #     test_list1 = ['0x10009', '0x10703', '0x10F69', '0x47E016B', '0x47E0228', '0x47E02FE', '0x47E0310', '0x47E0319', '0x47E0320', '0x47E0323', '0x47E0324', '0x47E0326', '0x47E0329', '0x47E0330', '0x47E0339', '0x47E0349', '0x47E035D', '0x47E035F', '0x47E0360', '0x47E0361', '0x47E042D', '0x47E048C', '0x47E0560', '0x47E05FD', '0x47E05FF', '0x47E060D', '0x47E0616', '0x47E0690', '0x47E06C6', '0x47E06CB', '0x47E06D9', '0x47E06DB', '0x47E06DE', '0x47E06E0', '0x47E06E1', '0x47E06E2', '0x47E07B9', '0x47E07C6', '0x47E07CF', '0x47E07DC', '0x47E07DD', '0x47E07E1', '0x47E07E6', '0x47E07E9', '0x47E07EA', '0x47E07F2', '0x47E07F5', '0x47E07FA', '0x47E0812', '0x47E0822', '0x47E0854', '0x47E0857', '0x47E0859', '0x47E1006', '0x47E1007', '0x47E1008', '0x47E100C', '0x47E100D', '0x47E100E', '0x47E1013', '0x47E1014', '0x47E102D', '0x47E102E', '0x47E102F', '0x47E1030', '0x47E1045', '0x47E1046', '0x47E1047', '0x47E1049', '0x47E104E', '0x47E1052', '0x47E1058', '0x47E105A', '0x47E15FB' ]# test array
    #     test_list1.sort() # sort the test array
    #     self.assertEqual(result, test_list1) # the resulting list should contain 6 unique hex codes and an empty string
    #     test_list2 = [] # empty array
    #     self.assertFalse(result == test_list2) # the resulting list should not be empty

    # # Tests the creation of the alarm hex master set
    # def test_make_alarm_hex_master_set(self):
    #     result = data_processing.make_incident_id_master_set() # function call
    #     self.assertEqual(len(result), 2820) # the resulting list should have a length of 2820 ​
    #     test_list1 = ['1072402', '1072403', '1072405', '1072439', '1072446', '1072447', '1072461', '1072462', '1072500', '1072528', '1072529', '1072537', '1072563', '1072566', '1072568', '1072580', '1072580A', '1072581', '1072600', '1072601', '1072602', '1072603', '1072607', '1072611', '1072616', '1072619', '1072621', '1072654', '1072660', '1072661', '1072663', '1072668', '1072671', '1072677', '1072679', '1072682', '1072699', '1072701', '1072702', '1072703', '1072704', '1072705', '1072706', '1072707', '1072709', '1072709A', '1072709B', '1072732', '1072750', '1072770', '1072773', '1072780', '1072841', '1072848', '1072850', '1072870', '1072874', '1072877', '1072880', '1072881', '1072882', '1072898', '1072900', '1072903', '1072905', '1072907', '1072915', '1072926', '1072927', '1072932', '1072933', '1072937', '1072939', '1072941', '1072943', '1072945', '1072951', '1072953', '1072957', '1072970', '1072977', '1073018', '1073022', '1073027', '1073037', '1073043', '1073045', '1073049', '1073049A', '1073049B', '1073050', '1073052', '1073054', '1073056', '1073058', '1073074', '1073074A', '1073076', '1073077', '1073079', '1073081', '1073082', '1073090', '1073093', '1073095', '1073097', '1073098', '1073099', '1073101', '1073104', '1073105', '1073106', '1073107', '1073112', '1073114', '1073115', '1073118', '1073121', '1073124', '1073124A', '1073125', '1073128', '1073133', '1073135', '1073142', '1073144', '1073146', '1073147', '1073148', '1073149', '1073150', '1073151', '1073153', '1073154', '1073155', '1073156', '1073158', '1073159', '1073163', '1073164', '1073169', '1073173', '1073175', '1073175A', '1073178', '1073179', '1073181', '1073182', '1073183', '1073184', '1073185', '1073187', '1073190', '1073191', '1073192', '1073193', '1073193A', '1073194', '1073195', '1073197', '1073199', '1073200', '1073202', '1073205', '1073208', '1073217', '1073221', '1073223', '1073224', '1073225', '1073227', '1073228', '1073230', '1073233', '1073235', '1073236', '1073237', '1073239', '1073240', '1073242', '1073242A', '1073244', '1073245', '1073246', '1073247', '1073248', '1073249', '1073250', '1073251', '1073252', '1073253', '1073256', '1073258', '1073263', '1073269', '1073272', '1073278', '1073279', '1073280', '1073283', '1073286', '1073287', '1073288', '1073289', '1073291', '1073293', '1073295', '1073296', '1073297', '1073298', '1073300', '1073302', '1073309', '1073310', '1073311', '1073312', '1073313', '1073315', '1073318', '1073319', '1073321', '1073322', '1073323', '1073324', '1073331', '1073332', '1073336', '1073340', '1073343', '1073351', '1073352', '1073371', '1073373', '1073374', '1073384', '1073393', '1073399', '1073401', '1073402', '1073404', '1073406', '1073409', '1073411', '1073412', '1073418', '1073419', '1073421', '1073423', '1073425', '1073428', '1073432', '1073433', '1073434', '1073440', '1073442', '1073443', '1073448', '1073452', '1073455', '1073457', '1073458', '1073459', '1073460', '1073461', '1073462', '1073467', '1073469', '1073475', '1073476', '1073479', '1073480', '1073488', '1073490', '1073492', '1073493', '1073494', '1073495', '1073497', '1073507', '1073518', '1073521', '1073523', '1073525', '1073529', '1073531', '1073532', '1073533', '1073542', '1073543', '1073548', '1073553', '1073555', '1073557', '1073559', '1073561', '1073565', '1073566', '1073568', '1073568A', '1073577', '1073580', '1073582', '1073584', '1073586', '1073588', '1073589', '1073591', '1073593', '1073594', '1073598', '1073598A', '1073598B', '1073605', '1073613', '1073621', '1073621A', '1073622', '1073622A', '1073629', '1073631', '1073631A', '1073631B', '1073632', '1073670', '1073672', '1073672A', '1073673', '1073679', '1073679A', '1073679B', '1073680', '1073682', '1073683', '1073684', '1073685', '1073710', '1073712', '1073713', '1073715', '1073718', '1073723', '1073725', '1073727', '1073728', '1073730', '1073731', '1073733', '1073737', '1073740', '1073742', '1073744', '1073746', '1073747', '1073753', '1073755', '1073757', '1073757A', '1073762', '1073764', '1073765', '1073768', '1073769', '1073771', '1073776', '1073780', '1073781', '1073783', '1073786', '1073787', '1073788', '1073789', '1073789A', '1073790', '1073791', '1073792', '1073793', '1073794', '1073795', '1073798', '1073803', '1073805', '1073806', '1073808', '1073808A', '1073811', '1073813', '1073816', '1073817', '1073818', '1073820', '1073821', '1073824', '1073826', '1073830', '1073831', '1073833', '1073836', '1073837', '1073839', '1073842', '1073843', '1073844', '1073847', '1073858', '1073860', '1073861', '1073863', '1073864', '1073866', '1073868', '1073889', '1073889A', '1073904', '1073906', '1073909', '1073914', '1073918', '1073920', '1073925', '1073927', '1073928', '1073931', '1073932', '1073933', '1073934', '1073935', '1073936', '1073937', '1073938', '1073939', '1073940', '1073941', '1073942', '1073943', '1073944', '1073945', '1073946', '1073947', '1073948', '1073949', '1073950', '1073951', '1073952', '1073953', '1073954', '1073955', '1073961', '1073962', '1073964', '1073966', '1073967', '1073972', '1073973', '1073975', '1073976', '1073977', '1073978', '1073983', '1073985', '1073988', '1073989', '1073992', '1073993', '1073994', '1074002', '1074003', '1074004', '1074005', '1074006', '1074008', '1074010', '1074012', '1074017', '1074018', '1074029', '1074031', '1074032', '1074035', '1074038', '1074039', '1074041', '1074042', '1074045', '1074049', '1074050', '1074054', '1074055', '1074056', '1074057', '1074059', '1074061', '1074063', '1074066', '1074071', '1074076', '1074080', '1074082', '1074082A', '1074083', '1074086', '1074099', '1074101', '1074105', '1074113', '1074115', '1074116', '1074118', '1074120', '1074128', '1074129', '1074131', '1074132', '1074134', '1074135', '1074139', '1074143', '1074145', '1074147', '1074148', '1074149', '1074151', '1074153', '1074154', '1074155', '1074157', '1074158', '1074162', '1074163', '1074165', '1074167', '1074170', '1074172', '1074175', '1074177', '1074178', '1074183', '1074184', '1074185', '1074186', '1074189', '1074195', '1074196', '1074197', '1074199', '1074200', '1074211', '1074212', '1074213', '1074215', '1074218', '1074219', '1074220', '1074221', '1074221A', '1074222', '1074224', '1074224A', '1074225', '1074226', '1074230', '1074246', '1074248', '1074251', '1074252', '1074259', '1074263', '1074269', '1074288', '1074291', '1074313', '1074316', '1074319', '1074321', '1074322', '1074324', '1074326', '1074327', '1074327A', '1074330', '1074333', '1074334', '1074335', '1074339', '1074341', '1074344', '1074345', '1074346', '1074346A', '1074347', '1074347A', '1074358', '1074360', '1074361', '1074364', '1074365', '1074373', '1074377', '1074378', '1074383', '1074384', '1074385', '1074391', '1074398', '1074400', '1074402', '1074403', '1074405', '1074408', '1074409', '1074427', '1074432', '1074434', '1074435', '1074435A', '1074435B', '1074437', '1074440', '1074442', '1074444', '1074447', '1074449', '1074450', '1074451', '1074452', '1074455', '1074457', '1074459', '1074461', '1074465', '1074466', '1074469', '1074471', '1074472', '1074473', '1074474', '1074479', '1074483', '1074485', '1074486', '1074487', '1074490', '1074491', '1074493', '1074495', '1074497', '1074500', '1074502', '1074504', '1074505', '1074506', '1074508', '1074511', '1074514', '1074514A', '1074515', '1074516', '1074520', '1074525', '1074529', '1074529A', '1074533', '1074534', '1074535', '1074539', '1074547', '1074553', '1074554', '1074559', '1074561', '1074568', '1074571', '1074572', '1074580', '1074581', '1074582', '1074585', '1074587', '1074593', '1074594', '1074597', '1074598', '1074636', '1074640', '1074641', '1074643', '1074644', '1074645', '1074647', '1074650', '1074653', '1074656', '1074657', '1074658', '1074663', '1074664', '1074668', '1074670', '1074676', '1074677', '1074678', '1074680', '1074682', '1074682A', '1074684', '1074685', '1074688', '1074692', '1074693', '1074698', '1074708', '1074710', '1074712', '1074713', '1074715', '1074715A', '1074716', '1074717', '1074719', '1074725', '1074726', '1074728', '1074730', '1074732', '1074733', '1074736', '1074738', '1074743', '1074744', '1074746', '1074749', '1074751', '1074756', '1074757', '1074759', '1074765', '1074778', '1074782', '1074785', '1074791', '1074797', '1074803', '1074805', '1074808', '1074811', '1074814', '1074816', '1074818', '1074822', '1074823', '1074827', '1074828', '1074828A', '1074830', '1074833', '1074834', '1074836', '1074837', '1074837A', '1074837B', '1074844', '1074845', '1074848', '1074849', '1074864', '1074867', '1074868', '1074872', '1074873', '1074876', '1074885', '1074898', '1074900', '1074901', '1074903', '1074904', '1074906', '1074909', '1074910', '1074911', '1074914', '1074915', '1074916', '1074921', '1074921A', '1074939', '1074941', '1074958', '1074959', '1074970', '1074971', '1074975', '1074978', '1074979', '1074984', '1074986', '1074988', '1074990', '1074991', '1074996', '1074998', '1075008', '1075014', '1075016', '1075020', '1075023', '1075024', '1075025', '1075026', '1075027', '1075028', '1075029', '1075030', '1075032', '1075033', '1075034', '1075036', '1075039', '1075040', '1075042', '1075044', '1075046', '1075049', '1075051', '1075059', '1075072', '1075073', '1075074', '1075077', '1075079', '1075080', '1075081', '1075088', '1075089', '1075098', '1075100', '1075101', '1075106', '1075107', '1075108', '1075108A', '1075113', '1075114', '1075115', '1075118', '1075119', '1075120', '1075121', '1075123', '1075128', '1075131', '1075133', '1075136', '1075137', '1075143', '1075144', '1075147', '1075152', '1075157', '1075158', '1075159', '1075160', '1075162', '1075163', '1075165', '1075167', '1075168', '1075169', '1075170', '1075171', '1075172', '1075173', '1075174', '1075175', '1075176', '1075177', '1075178', '1075179', '1075180', '1075181', '1075182', '1075184', '1075185', '1075186', '1075187', '1075188', '1075189', '1075190', '1075192', '1075193', '1075194', '1075195', '1075196', '1075197', '1075198', '1075218', '1075219', '1075223', '1075224', '1075225', '1075230', '1075236', '1075259', '1075266', '1075267', '1075271', '1075277', '1075277A', '1075283', '1075284', '1075287', '1075288', '1075299', '1075307', '1075308', '1075310', '1075313', '1075320', '1075322', '1075324', '1075326', '1075331', '1075333', '1075334', '1075340', '1075342', '1075343', '1075345', '1075349', '1075350', '1075351', '1075353', '1075354', '1075362', '1075365', '1075367', '1075369', '1075370', '1075371', '1075374', '1075378', '1075380', '1075382', '1075388', '1075394', '1075398', '1075404', '1075404A', '1075404B', '1075407', '1075413', '1075414', '1075416', '1075418', '1075420', '1075421', '1075422', '1075425', '1075426', '1075429', '1075437', '1075438', '1075439', '1075445', '1075446', '1075447', '1075448', '1075449', '1075453', '1075454', '1075455', '1075456', '1075468', '1075470', '1075473', '1075474', '1075478', '1075481', '1075482', '1075484', '1075485', '1075486', '1075487', '1075488', '1075489', '1075490', '1075491', '1075493', '1075496', '1075498', '1075500', '1075501', '1075502', '1075505', '1075506', '1075508', '1075511', '1075515', '1075518', '1075519', '1075524', '1075525', '1075528', '1075529', '1075529A', '1075533', '1075536', '1075538', '1075539', '1075541', '1075550', '1075552', '1075554', '1075555', '1075556', '1075562', '1075563', '1075565', '1075566', '1075576', '1075578', '1075579', '1075581', '1075583', '1075585', '1075586', '1075587', '1075590', '1075592', '1075595', '1075597', '1075598', '1075599', '1075601', '1075602', '1075603', '1075603A', '1075605', '1075606', '1075611', '1075613', '1075617', '1075618', '1075619', '1075620', '1075621', '1075625', '1075626', '1075628', '1075630', '1075631', '1075632', '1075634', '1075637', '1075637A', '1075637B', '1075652', '1075653', '1075654', '1075658', '1075659', '1075660', '1075662', '1075663', '1075664', '1075664A', '1075666', '1075672', '1075674', '1075683', '1075684', '1075685', '1075694', '1075696', '1075697', '1075698', '1075699', '1075704', '1075705', '1075706', '1075707', '1075708', '1075710', '1075711', '1075714', '1075716', '1075721', '1075723', '1075727', '1075730', '1075732', '1075736', '1075737', '1075738', '1075740', '1075743', '1075745', '1075746', '1075748', '1075750', '1075754', '1075757', '1075762', '1075763', '1075763A', '1075769', '1075770', '1075771', '1075772', '1075776', '1075777', '1075778', '1075780', '1075786', '1075788', '1075790', '1075791', '1075793', '1075795', '1075796', '1075798', '1075800', '1075801', '1075803', '1075804', '1075805', '1075806', '1075807', '1075808', '1075809', '1075810', '1075811', '1075812', '1075813', '1075814', '1075815', '1075816', '1075817', '1075818', '1075819', '1075820', '1075821', '1075822', '1075823', '1075824', '1075825', '1075826', '1075827', '1075828', '1075829', '1075830', '1075831', '1075832', '1075833', '1075834', '1075835', '1075836', '1075839', '1075840', '1075843', '1075845', '1075850', '1075853', '1075859', '1075860', '1075861', '1075863', '1075864', '1075871', '1075875', '1075877', '1075877A', '1075878', '1075880', '1075884', '1075887', '1075890', '1075892', '1075895', '1075897', '1075898', '1075899', '1075900', '1075904', '1075905', '1075906', '1075909', '1075910', '1075913', '1075936', '1075937', '1075938', '1075940', '1075942', '1075943', '1075944', '1075945', '1075951', '1075953', '1075954', '1075959', '1075960', '1075977', '1075978', '1075981', '1075982', '1075986', '1075987', '1075988', '1075996', '1076000', '1076005', '1076011', '1076013', '1076014', '1076016', '1076018', '1076021', '1076024', '1076029', '1076033', '1076035', '1076037', '1076038', '1076042', '1076045', '1076047', '1076049', '1076050', '1076051', '1076052', '1076054', '1076055', '1076056', '1076059', '1076067', '1076070', '1076074', '1076076', '1076081', '1076085', '1076089', '1076092', '1076094', '1076097', '1076099', '1076101', '1076103', '1076106', '1076107', '1076112', '1076114', '1076115', '1076116', '1076120', '1076121', '1076124', '1076126', '1076127', '1076129', '1076132', '1076133', '1076134', '1076136', '1076136A', '1076140', '1076141', '1076143', '1076146', '1076148', '1076149', '1076150', '1076153', '1076156', '1076158', '1076159', '1076160', '1076161', '1076164', '1076170', '1076172', '1076180', '1076188', '1076189', '1076197', '1076198', '1076208', '1076214', '1076215', '1076218', '1076218A', '1076219', '1076219A', '1076223', '1076223A', '1076227', '1076233', '1076236', '1076237', '1076241', '1076245', '1076246', '1076248', '1076253', '1076255', '1076256', '1076257', '1076262', '1076267', '1076269', '1076271', '1076273', '1076278', '1076280', '1076283', '1076285', '1076290', '1076308', '1076309', '1076317', '1076318', '1076320', '1076329', '1076333', '1076333A', '1076335', '1076336', '1076338', '1076341', '1076342', '1076345', '1076346', '1076347', '1076348', '1076350', '1076351', '1076352', '1076355', '1076357', '1076365', '1076367', '1076369', '1076371', '1076374', '1076376', '1076377', '1076378', '1076379', '1076380', '1076382', '1076385', '1076387', '1076389', '1076390', '1076395', '1076400', '1076402', '1076403', '1076408', '1076411', '1076412', '1076419', '1076425', '1076427', '1076428', '1076433', '1076435', '1076437', '1076438', '1076442', '1076444', '1076445', '1076446', '1076447', '1076450', '1076452', '1076452A', '1076457', '1076465', '1076466', '1076471', '1076472', '1076472A', '1076473', '1076474', '1076476', '1076477', '1076478', '1076479', '1076480', '1076481', '1076482', '1076484', '1076485', '1076486', '1076489', '1076496', '1076505', '1076506', '1076508', '1076509', '1076512', '1076515', '1076526', '1076527', '1076528', '1076531', '1076533', '1076534', '1076535', '1076543', '1076544', '1076548', '1076552', '1076553', '1076554', '1076555', '1076556', '1076557', '1076558', '1076559', '1076560', '1076561', '1076563', '1076564', '1076565', '1076567', '1076568', '1076569', '1076570', '1076571', '1076573', '1076576', '1076578', '1076579', '1076582', '1076584', '1076585', '1076586', '1076587', '1076594', '1076601', '1076602', '1076604', '1076605', '1076608', '1076610', '1076613', '1076615', '1076616', '1076618', '1076619', '1076620', '1076621', '1076623', '1076626', '1076627', '1076630', '1076631', '1076633', '1076635', '1076637', '1076638', '1076639', '1076639A', '1076642', '1076645', '1076646', '1076647', '1076648', '1076651', '1076652', '1076653', '1076656', '1076658', '1076660', '1076662', '1076663', '1076665', '1076673', '1076675', '1076676', '1076677', '1076681', '1076683', '1076686', '1076688', '1076689', '1076690', '1076691', '1076693', '1076697', '1076698', '1076700', '1076706', '1076709', '1076711', '1076713', '1076714', '1076715', '1076716', '1076717', '1076721', '1076724', '1076727', '1076732', '1076733', '1076735', '1076737', '1076738', '1076740', '1076741', '1076743', '1076746', '1076747', '1076749', '1076751', '1076754', '1076757', '1076759', '1076770', '1076771', '1076779', '1076780', '1076782', '1076783', '1076784', '1076788', '1076796', '1076799', '1076801', '1076802', '1076804', '1076806', '1076808', '1076811', '1076816', '1076817', '1076819', '1076821', '1076821A', '1076823', '1076827', '1076828', '1076829', '1076833', '1076834', '1076836', '1076839', '1076840', '1076842', '1076845', '1076846', '1076848', '1076854', '1076856', '1076857', '1076859', '1076860', '1076864', '1076870', '1076873', '1076875', '1076877', '1076880', '1076882', '1076888', '1076889', '1076891', '1076905', '1076907', '1076916', '1076917', '1076918', '1076922', '1076922A', '1076933', '1076941', '1076944', '1076952', '1076954', '1076962', '1076965', '1076966', '1076968', '1076969', '1076998', '1077009', '1077022', '1077024', '1077025', '1077030', '1077031', '1077032', '1077034', '1077035', '1077040', '1077042', '1077046', '1077047', '1077050', '1077052', '1077053', '1077055', '1077059', '1077063', '1077065', '1077066', '1077067', '1077077', '1077079', '1077080', '1077082', '1077090', '1077091', '1077093', '1077093A', '1077094', '1077100', '1077101', '1077104', '1077107', '1077108', '1077110', '1077111', '1077112', '1077115', '1077119', '1077121', '1077125', '1077132', '1077133', '1077135', '1077137', '1077145', '1077146', '1077149', '1077152', '1077153', '1077154', '1077155', '1077156', '1077159', '1077163', '1077170', '1077171', '1077175', '1077176', '1077180', '1077181', '1077183', '1077186', '1077187', '1077189', '1077193', '1077194', '1077196', '1077199', '1077208', '1077211', '1077215', '1077216', '1077219', '1077223', '1077228', '1077230', '1077235', '1077236', '1077238', '1077239', '1077242', '1077245', '1077248', '1077249', '1077251', '1077253', '1077256', '1077258', '1077261', '1077263', '1077265', '1077269', '1077271', '1077273', '1077274', '1077276', '1077279', '1077281', '1077282', '1077285', '1077287', '1077292', '1077293', '1077294', '1077298', '1077299', '1077300', '1077302', '1077313', '1077314', '1077317', '1077319', '1077323', '1077324', '1077326', '1077328', '1077329', '1077329A', '1077331', '1077333', '1077336', '1077342', '1077348', '1077350', '1077353', '1077356', '1077359', '1077361', '1077362', '1077363', '1077364', '1077367', '1077369', '1077372', '1077375', '1077377', '1077378', '1077382', '1077388', '1077390', '1077395', '1077396', '1077398', '1077399', '1077402', '1077403', '1077404', '1077405', '1077407', '1077409', '1077411', '1077412', '1077414', '1077417', '1077419', '1077420', '1077421', '1077422', '1077424', '1077425', '1077426', '1077428', '1077429', '1077430', '1077432', '1077433', '1077434', '1077435', '1077436', '1077437', '1077438', '1077439', '1077440', '1077441', '1077452', '1077455', '1077456', '1077458', '1077460', '1077462', '1077463', '1077467', '1077469', '1077470', '1077472', '1077489', '1077491', '1077492', '1077494', '1077495', '1077497', '1077498', '1077500', '1077503', '1077504', '1077506', '1077508', '1077508A', '1077511', '1077513', '1077526', '1077531', '1077537', '1077544', '1077546', '1077554', '1077572', '1077575', '1077578', '1077583', '1077596', '1077597', '1077598', '1077604', '1077606', '1077608', '1077609', '1077610', '1077613', '1077616', '1077618', '1077620', '1077622', '1077624', '1077625', '1077626', '1077628', '1077629', '1077633', '1077634', '1077636', '1077638', '1077643', '1077645', '1077648', '1077650', '1077652', '1077653', '1077654', '1077656', '1077659', '1077660', '1077661', '1077662', '1077663', '1077666', '1077668', '1077669', '1077670', '1077671', '1077673', '1077676', '1077678', '1077682', '1077684', '1077685', '1077688', '1077689', '1077693', '1077694', '1077696', '1077697', '1077698', '1077699', '1077700', '1077701', '1077703', '1077704', '1077705', '1077706', '1077708', '1077709', '1077711', '1077713', '1077715', '1077717', '1077718', '1077719', '1077720', '1077722', '1077723', '1077724', '1077726', '1077728', '1077730', '1077734', '1077736', '1077738', '1077741', '1077742', '1077752', '1077755', '1077756', '1077760', '1077761', '1077762', '1077764', '1077765', '1077767', '1077768', '1077771', '1077773', '1077774', '1077775', '1077778', '1077780', '1077780A', '1077784', '1077785', '1077788', '1077789', '1077790', '1077797', '1077798', '1077799', '1077800', '1077804', '1077806', '1077807', '1077809', '1077818', '1077819', '1077820', '1077821', '1077823', '1077825', '1077826', '1077827', '1077828', '1077829', '1077830', '1077831', '1077832', '1077833', '1077834', '1077835', '1077836', '1077838', '1077839', '1077840', '1077843', '1077848', '1077852', '1077854', '1077856', '1077857', '1077858', '1077860', '1077861', '1077863', '1077865', '1077870', '1077870A', '1077885', '1077887', '1077891', '1077893', '1077894', '1077895', '1077898', '1077900', '1077902', '1077903', '1077907', '1077908', '1077909', '1077910', '1077911', '1077911A', '1077936', '1077939', '1077941', '1077950', '1077951', '1077954', '1077959', '1077961', '1077965', '1077966', '1077968', '1077969', '1077971', '1077977', '1077978', '1077980', '1077982', '1077982A', '1077982B', '1077982C', '1077982D', '1077983', '1077984', '1077984A', '1077984B', '1077985', '1077985A', '1077985B', '1077986', '1077987', '1077987A', '1077987B', '1077988', '1077988A', '1077989', '1077989A', '1077990', '1077990A', '1077990B', '1077990C', '1077992', '1077992A', '1077994', '1077995', '1077995A', '1077995B', '1077995C', '1077996', '1077996A', '1077996B', '1077996C', '1077997', '1077997A', '1077998', '1077999', '1077999A', '1077999B', '1077999C', '1078000', '1078000A', '1078000B', '1078001', '1078002', '1078002A', '1078002B', '1078003', '1078003A', '1078004', '1078004A', '1078005', '1078005A', '1078005B', '1078005C', '1078005D', '1078006', '1078007', '1078007A', '1078008', '1078010', '1078010A', '1078011', '1078011A', '1078012', '1078012A', '1078013', '1078013A', '1078014', '1078014A', '1078014B', '1078015', '1078015A', '1078015B', '1078023', '1078024', '1078026', '1078033', '1078039', '1078040', '1078042', '1078045', '1078046', '1078049', '1078050', '1078053', '1078056', '1078058', '1078059', '1078065', '1078067', '1078072', '1078076', '1078077', '1078081', '1078087', '1078088', '1078088A', '1078090', '1078092', '1078106', '1078108', '1078110', '1078116', '1078119', '1078124', '1078126', '1078132', '1078134', '1078135', '1078135A', '1078137', '1078138', '1078140', '1078142', '1078143', '1078144', '1078144A', '1078147', '1078151', '1078154', '1078155', '1078158', '1078158A', '1078160', '1078166', '1078170', '1078171', '1078172', '1078174', '1078177', '1078179', '1078183', '1078185', '1078186', '1078189', '1078194', '1078196', '1078197', '1078198', '1078199', '1078204', '1078209', '1078210', '1078211', '1078215', '1078217', '1078219', '1078219A', '1078242', '1078247', '1078251', '1078257', '1078260', '1078260A', '1078276', '1078282', '1078283', '1078285', '1078288', '1078290', '1078292', '1078293', '1078294', '1078297', '1078300', '1078301', '1078303', '1078311', '1078312', '1078313', '1078319', '1078328', '1078333', '1078338', '1078339', '1078340', '1078341', '1078342', '1078346', '1078349', '1078350', '1078353', '1078355', '1078359', '1078362', '1078364', '1078366', '1078369', '1078372', '1078373', '1078382', '1078382A', '1078384', '1078390', '1078394', '1078398', '1078399', '1078400', '1078401', '1078402', '1078405', '1078407', '1078408', '1078409', '1078410', '1078411', '1078412', '1078413', '1078420', '1078421', '1078427', '1078431', '1078433', '1078442', '1078445', '1078446', '1078448', '1078449', '1078452', '1078456', '1078459', '1078461', '1078465', '1078470', '1078478', '1078482', '1078483', '1078485', '1078490', '1078494', '1078495', '1078499', '1078505', '1078514', '1078520', '1078522', '1078523', '1078537', '1078538', '1078539', '1078557', '1078561', '1078563', '1078565', '1078566', '1078569', '1078575', '1078591', '1078631', '1078652', '1078652A', '1078652B', '1078654', '1078656', '1078659', '1078660', '1078663', '1078684', '1078686', '1078694', '1078704', '1078710', '1078711', '1078712', '1078713', '1078729', '1078731', '1078733', '1078736', '1078740', '1078743', '1078745', '1078746', '1078754', '1078755', '1078757', '1078758', '1078759', '1078760', '1078763', '1078766', '1078772', '1078773', '1078774', '1078775', '1078777', '1078778', '1078779', '1078780', '1078783', '1078785', '1078788', '1078789', '1078791', '1078793', '1078795', '1078797', '1078799', '1078800', '1078801', '1078803', '1078803A', '1078810', '1078813', '1078815', '1078817', '1078820', '1078822', '1078823', '1078825', '1078827', '1078828', '1078829', '1078831', '1078834', '1078835', '1078837', '1078838', '1078839', '1078840', '1078841', '1078842', '1078851', '1078852', '1078853', '1078855', '1078857', '1078858', '1078859', '1078860', '1078862', '1078863', '1078865', '1078869', '1078870', '1078871', '1078872', '1078873', '1078874', '1078875', '1078878', '1078880', '1078881', '1078882', '1078884', '1078890', '1078893', '1078895', '1078896', '1078898', '1078898A', '1078899', '1078900', '1078905', '1078909', '1078910', '1078911', '1078913', '1078915', '1078916', '1078916A', '1078918', '1078919', '1078920', '1078921', '1078922', '1078926', '1078927', '1078929', '1078931', '1078932', '1078934', '1078935', '1078940', '1078941', '1078943', '1078944', '1078945', '1078946', '1078948', '1078952', '1078954', '1078955', '1078958', '1078961', '1078965', '1078967', '1078967A', '1078968', '1078971', '1078982', '1078983', '1078984', '1078989', '1078992', '1078995', '1078997', '1079009', '1079011', '1079014', '1079018', '1079024', '1079037', '1079044', '1079044A', '1079049', '1079051', '1079066', '1079067', '1079074', '1079081', '1079083', '1079084', '1079090', '1079097', '1079103', '1079104', '1079118', '1079121', '1079122', '1079124', '1079125', '1079127', '1079128', '1079130', '1079138', '1079139', '1079139A', '1079140', '1079140A', '1079141', '1079142', '1079142A', '1079143', '1079144', '1079145', '1079146', '1079147', '1079148', '1079149', '1079150', '1079151', '1079152', '1079153', '1079154', '1079155', '1079156', '1079157', '1079158', '1079159', '1079159A', '1079160', '1079161', '1079162', '1079163', '1079164', '1079165', '1079167', '1079168', '1079169', '1079169A', '1079170', '1079171', '1079172', '1079172A', '1079172B', '1079173', '1079176', '1079177', '1079178', '1079180', '1079181', '1079183', '1079184', '1079186', '1079190', '1079191', '1079192', '1079194', '1079195', '1079203', '1079231', '1079232', '1079233', '1079235', '1079253', '1079255', '1079286', '1079291', '1079295', '1079297', '1079298', '1079302', '1079305', '1079307', '1079308', '1079309', '1079311', '1079314', '1079317', '1079318', '1079326', '1079328', '1079329', '1079331', '1079332', '1079333', '1079336', '1079337', '1079338', '1079341', '1079343', '1079346', '1079350', '1079355', '1079359', '1079361', '1079362', '1079363', '1079371', '1079373', '1079396', '1079401', '1079402', '1079404', '1079409', '1079410', '1079424', '1079426', '1079428', '1079429', '1079432', '1079433', '1079434', '1079437', '1079438', '1079439', '1079440', '1079443', '1079444', '1079447', '1079452', '1079453', '1079455', '1079459', '1079468', '1079475', '1079475A', '1079476', '1079476A', '1079476B', '1079480', '1079480A', '1079483', '1079505', '1079507', '1079511', '1079516', '1079518', '1079519', '1079520', '1079528', '1079529', '1079544', '1079545', '1079550', '1079551', '1079552', '1079575', '1079576', '1079579', '1079583', '1079609', '1079610', '1079611', '1079612', '1079616', '1079622', '1079635', '1079635A', '1079642', '1079646', '1079647', '1079648', '1079654', '1079690', '1079691', '1079692', '1079694', '1079702', '1079703', '1079706', '1079714', '1079715', '1079716', '1079740', '1079745', '1079747', '1079748', '1079754', '1079765', '1079770', '1079772', '1079773', '1079775', '1079777', '1079779', '1079786', '1079798', '1079800', '1079804', '1079807', '1079808', '1079814', '1079831', '1079833', '1079835', '1079840', '1079846', '1079849', '1079850', '1079862', '1079896', '1079898', '1079903', '1079904', '1079905', '1079914', '1079941', '1079948', '1079948A', '1079989', '1079995', '1080021', '1080026', '1080033', '1080035', '1080068', '1080068A', '1080068B', '1080076', '1080105', '1080110', '1080116', '1080118', '1080119', '1080125', '1080126', '1080130', '1080149', '1080150', '1080151', '1080153', '1080154', '1080155', '1080156', '1080171', '1080175', '1080190', '1080200', '1080201', '1080202', '1080203', '1080205', '1080227', '1080228', '1080237', '1080242', '1080274', '1080276', '1080281', '1080284', '1080285', '1080287', '1080316', '1080336', '1080364', '1080389', '1080393', '1080410', '1080413', '1080414', '1080460', '1080463', '1080465', '1080466', '1080467', '1080469', '1080471', '1080473', '1080474', '1080498', '1080499', '1080501', '1080503', '1080512', '1080514', '1080540', '1080542', '1080551', '1080567', '1080569', '1080570', '1080578', '1080583', '1080584', '1080609', '1080610', '1080612', '1080614', '1080616', '1080619', '1080622', '1080624', '1080625', '1080627', '1080629', '1080631', '1080633', '1080638', '1080645', '1080646', '1080649', '1080652', '1080653', '1080654', '1080660', '1080660A', '1080675', '1080678', '1080679', '1080680', '1080681', '1080682', '1080684', '1080686', '1080688', '1080690', '1080692', '1080693', '1080695', '1080698', '1080700', '1080702', '1080704', '1080705', '1080706', '1080707', '1080708', '1080711', '1080712', '1080714', '1080715', '1080716', '1080722', '1080723', '1080724', '1080725', '1080726', '1080731', '1080733', '1080735', '1080737', '1080738', '1080739', '1080741', '1080742', '1080744', '1080746', '1080747', '1080750', '1080752', '1080755', '1080757', '1080759', '1080760', '1080762', '1080763', '1080764', '1080765', '1080766', '1080767', '1080768', '1080769', '1080774', '1080777', '1080780', '1080781', '1080782', '1080783', '1080784', '1080786', '1080789', '1080791', '1080791A', '1080792', '1080793', '1080796', '1080799', '1080800', '1080801', '1080802', '1080803', '1080805', '1080807', '1080810', '1080811', '1080815', '1080819', '1080820', '1080822', '1080823', '1080825', '1080826', '1080828', '1080829', '1080830', '1080831', '1080833', '1080836', '1080838', '1080839', '1080841', '1080846', '1080849', '1080852', '1080861', '1080861A', '1080862', '1080864', '1080868', '1080869', '1080872', '1080873', '1080876', '1080878', '1080883', '1080885', '1080890', '1080913', '1080917', '1080919', 'The CCC received a call from the customer stating LOBs from RFF Bliss were inaccurate.']
    #     test_list1.sort() # sort the test array
    #     self.assertEqual(result, test_list1) # the resulting list should contain 6 unique hex codes and an empty string
    #     test_list2 = [] # empty array
    #     self.assertFalse(result == test_list2) # the resulting list should not be empty

if __name__ == '__main__':
    unittest.main()