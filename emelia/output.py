import time
from learning_model import prediction
from classify_tickets import (classify_data, validation,
                              report_prediction_results,
                              convert_test_data)
from data_processing import (detection_method, event_cause_vals,
                             fix_classification, restore_method, relevance,
                             subsystem, encode_ticket_hex_codes,
                             get_encoded_label_value,
                             convert_array_to_np_array)


def main():
    # starting timer
    start_time = time.time()

    # converting lists to numpy array, the number specifies the index in the
    # array of associated label values
    encoded_hex_codes = convert_array_to_np_array(encode_ticket_hex_codes())
    event_cause_options = convert_array_to_np_array(
                            get_encoded_label_value(event_cause_vals, 0))
    detection_method_options = convert_array_to_np_array(
                            get_encoded_label_value(detection_method, 1))
    restore_method_options = convert_array_to_np_array(
                                get_encoded_label_value(restore_method, 2))
    fix_classification_options = convert_array_to_np_array(
                                get_encoded_label_value(fix_classification, 3))
    subsystem_options = convert_array_to_np_array(
                            get_encoded_label_value(subsystem, 4))
    relevance_options = convert_array_to_np_array(
                            get_encoded_label_value(relevance, 5))

# ########################## Train on Data ####################################
    # training & saving the model for each of the labels
    classify_data(encoded_hex_codes, event_cause_options,
                  'event_cause.hdf5', 101, 110,
                  0.80, len(event_cause_vals))

    classify_data(encoded_hex_codes, detection_method_options,
                  'detection_method.hdf5', 101, 110,
                  0.80, len(detection_method))

    classify_data(encoded_hex_codes, restore_method_options,
                  'restore_method.hdf5', 101, 110,
                  0.80, len(restore_method))

    classify_data(encoded_hex_codes, fix_classification_options,
                  'fix_classification.hdf5', 101, 110,
                  0.80, len(fix_classification))

    classify_data(encoded_hex_codes, subsystem_options,
                  'subsystem.hdf5', 101, 110,
                  0.80, len(subsystem))

    classify_data(encoded_hex_codes, relevance_options,
                  'relevance.hdf5', 101, 110,
                  0.80, len(relevance))

# ######################## Generate Predictions ###############################
    # 20 percent that needs to be tested for alarm hex and all labels
    predict_input_hex = encoded_hex_codes[2132:]
    predict_event_cause = event_cause_options[2132:]
    predict_detection_method = detection_method_options[2132:]
    predict_restore_method = restore_method_options[2132:]
    predict_fix_classification = fix_classification_options[2132:]
    predict_subsystem = subsystem_options[2132:]
    predict_relevance = relevance_options[2132:]

    # calling prediction from predict.py and returns array of confidence values
    event_cause_prediction = prediction(predict_input_hex, 'event_cause.hdf5')

    detection_method_prediction = prediction(predict_input_hex,
                                             'detection_method.hdf5')

    restore_method_prediction = prediction(predict_input_hex,
                                           'restore_method.hdf5')

    fix_classification_prediction = prediction(predict_input_hex,
                                               'fix_classification.hdf5')

    subsystem_prediction = prediction(predict_input_hex, 'subsystem.hdf5')

    relevance_prediction = prediction(predict_input_hex, 'relevance.hdf5')

# ############################ Validate Predictions ###########################
    # Validation calls for all labels using the prediction function returns
    validation(predict_event_cause,
               event_cause_prediction,
               predict_input_hex,
               'event_cause_predictions.txt')

    validation(predict_detection_method,
               detection_method_prediction,
               predict_input_hex,
               'detection_method_predictions.txt')

    validation(predict_restore_method,
               restore_method_prediction,
               predict_input_hex,
               'restore_method_predictions.txt')

    validation(predict_fix_classification,
               fix_classification_prediction,
               predict_input_hex,
               'fix_classication_predictions.txt')

    validation(predict_subsystem,
               subsystem_prediction,
               predict_input_hex,
               'subsystem_predictions.txt')

    validation(predict_relevance,
               relevance_prediction,
               predict_input_hex,
               'relevance_predictions.txt')


# ######################### TESTS REAL TICKETS ################################

    # Convert the alarm data to encoded np arrays
    result_alarm_np = convert_test_data('TestAlarms10.csv')

    # create prediction arrays using the input data from result_alarm_np
    test_EV = prediction(result_alarm_np, 'event_cause.hdf5')
    test_DM = prediction(result_alarm_np, 'detection_method.hdf5')
    test_RM = prediction(result_alarm_np, 'restore_method.hdf5')
    test_FC = prediction(result_alarm_np, 'fix_classification.hdf5')
    test_SUB = prediction(result_alarm_np, 'subsystem.hdf5')
    test_REL = prediction(result_alarm_np, 'relevance.hdf5')

    # Report the label under each classification and store the result in the
    # corresponding file. The order is the same as the alarm data order
    report_prediction_results(test_EV, event_cause_vals, 'Event Cause',
                              'EC_Predictions.txt')
    report_prediction_results(test_DM, detection_method, 'Detection Method',
                              'DM_Predictions.txt')
    report_prediction_results(test_RM, restore_method, 'Restore Method',
                              'RM_Predictions.txt')
    report_prediction_results(test_FC, fix_classification,
                              'Fix Classification', 'FC_Predictions.txt')
    report_prediction_results(test_SUB, subsystem, 'Subsystem',
                              'SUB_Predictions.txt')
    report_prediction_results(test_REL, relevance, 'Relevance',
                              'REL_Predictions.txt')

    # End timer & total runtime
    end_time = time.time()
    runtime = round(end_time - start_time, 2)

    print("\n" * 2)
    print("############################# METRICS ############################")
    print("Runtime: " + str(runtime) + "s")


if __name__ == "__main__":
    main()
