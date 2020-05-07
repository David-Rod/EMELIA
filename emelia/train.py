import threading

from learning_model import prediction
from classify_tickets import classify_data, validation
'''
from data_processing import (detection_method, event_cause_vals,
                             fix_classification, restore_method, relevance,
                             subsystem, convert_array_to_np_array,
                             encode_ticket_hex_codes, get_encoded_label_value)
'''
from data_processing import DataProcessor
from progress import run_progress_bar


def train_and_validate(alarm_file, ticket_file):

    dp = DataProcessor(alarm_file, ticket_file)
    # Create thread to run progress bar
    thread = threading.Thread(target=run_progress_bar, args=(670,))

    # Start thread to run progress bar
    thread.start()

    '''
    Converting lists to numpy array, the number specifies the index in the
    array of associated label values
    '''
    encoded_hex_codes = dp.convert_array_to_np_array(
        dp.encode_ticket_hex_codes())
    event_cause_options = dp.convert_array_to_np_array(
        dp.get_encoded_label_value(dp.event_cause_vals,
                                              0))
    detection_method_options = dp.convert_array_to_np_array(
                            dp.get_encoded_label_value(
                                dp.detection_method, 1))
    restore_method_options = dp.convert_array_to_np_array(
                                dp.get_encoded_label_value(
                                    dp.restore_method, 2))
    fix_classification_options = dp.convert_array_to_np_array(
                                dp.get_encoded_label_value(
                                    dp.fix_classification, 3))
    subsystem_options = dp.convert_array_to_np_array(
                            dp.get_encoded_label_value(
                                dp.subsystem, 4))
    relevance_options = dp.convert_array_to_np_array(
                            dp.get_encoded_label_value(
                                dp.relevance, 5))

    '''
    Train on Data

    training & saving the model for each of the labels
    '''

    classify_data(encoded_hex_codes, event_cause_options,
                  'event_cause.hdf5', 101, 110,
                  0.80, len(dp.event_cause_vals))

    classify_data(encoded_hex_codes, detection_method_options,
                  'detection_method.hdf5', 101, 110,
                  0.80, len(dp.detection_method))

    classify_data(encoded_hex_codes, restore_method_options,
                  'restore_method.hdf5', 101, 110,
                  0.80, len(dp.restore_method))

    classify_data(encoded_hex_codes, fix_classification_options,
                  'fix_classification.hdf5', 101, 110,
                  0.80, len(dp.fix_classification))

    classify_data(encoded_hex_codes, subsystem_options,
                  'subsystem.hdf5', 101, 110,
                  0.80, len(dp.subsystem))

    classify_data(encoded_hex_codes, relevance_options,
                  'relevance.hdf5', 101, 110,
                  0.80, len(dp.relevance))

    '''
    Generate Training Data Predictions

    20 percent that needs to be tested for alarm hex and all labels
    Calculate the starting place by multiplying length of encoded_hex_codes
    which is the input for the model
    '''

    start_index = int(len(encoded_hex_codes)*0.8)

    predict_input_hex = encoded_hex_codes[start_index:]
    predict_event_cause = event_cause_options[start_index:]
    predict_detection_method = detection_method_options[start_index:]
    predict_restore_method = restore_method_options[start_index:]
    predict_fix_classification = fix_classification_options[start_index:]
    predict_subsystem = subsystem_options[start_index:]
    predict_relevance = relevance_options[start_index:]

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

    '''
    Validate Training Data Predictions

    Validation calls for all labels using the prediction function returns
    '''

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

    # Join thread back to main process
    thread.join()
