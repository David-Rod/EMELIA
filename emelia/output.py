import time
from learning_model import prediction
from classify_tickets import classify_data, validation
from data_processing import (detection_method, event_cause_vals,
                             fix_classification, restore_method, relevance,
                             subsystem, encode_ticket_hex_codes,
                             get_encoded_label_value,
                             convert_array_to_np_array)


def main():
    # starting timer
    start_time = time.time()

    # converting lists to numpy array
    encoded_hex_codes = convert_array_to_np_array(encode_ticket_hex_codes())
    event_cause_options = convert_array_to_np_array(
                            get_encoded_label_value(event_cause_vals, 0))
    detection_method_options = convert_array_to_np_array(
                            get_encoded_label_value(detection_method, 1))
    fix_classification_options = convert_array_to_np_array(
                                get_encoded_label_value(fix_classification, 2))
    restore_method_options = convert_array_to_np_array(
                                get_encoded_label_value(restore_method, 3))
    relevance_options = convert_array_to_np_array(
                            get_encoded_label_value(relevance, 4))
    subsystem_options = convert_array_to_np_array(
                            get_encoded_label_value(subsystem, 5))

    # training & saving the model for each of the labels
    classify_data(encoded_hex_codes, event_cause_options,
                  'event_cause.hdf5', 101, 110,
                  0.80, len(event_cause_vals))

    classify_data(encoded_hex_codes, detection_method_options,
                  'detection_method.hdf5', 101, 110,
                  0.80, len(detection_method))
    classify_data(encoded_hex_codes, fix_classification_options,
                  'fix_classification.hdf5', 101, 110,
                  0.80, len(fix_classification))
    classify_data(encoded_hex_codes, restore_method_options,
                  'restore_method.hdf5', 101, 110,
                  0.80, len(restore_method))
    classify_data(encoded_hex_codes, relevance_options,
                  'relevance.hdf5', 101, 110,
                  0.80, len(relevance))
    classify_data(encoded_hex_codes, subsystem_options,
                  'subsystem.hdf5', 101, 110,
                  0.80, len(subsystem))

    # 20 percent that needs to be tested
    predict_input_hex = encoded_hex_codes[2132:]
    # predict_actual = event_cause_options[2132:]

    predict_event_cause = event_cause_options[2132:]
    predict_detection_method = detection_method_options[2132:]
    predict_fix_classification = fix_classification_options[2132:]
    predict_restore_method = restore_method_options[2132:]
    predict_relevance = relevance_options[2132:]
    predict_subsystem = subsystem_options[2132:]

    # calling prediction from predict.py and returns array of confidence values
    event_cause_prediction = prediction(predict_input_hex, 'event_cause.hdf5')
    detection_method_prediction = prediction(predict_input_hex,
                                             'detection_method.hdf5')
    fix_classification_prediction = prediction(predict_input_hex,
                                               'fix_classification.hdf5')
    restore_method_prediction = prediction(predict_input_hex,
                                           'restore_method.hdf5')
    relevance_prediction = prediction(predict_input_hex, 'relevance.hdf5')
    subsystem_prediction = prediction(predict_input_hex, 'subsystem.hdf5')

    # Validation calls for all labels using the prediction function returns
    event_cause_validation = validation(predict_event_cause,
                                        event_cause_prediction,
                                        predict_input_hex,
                                        'event_cause_predictions.txt')
    event_cause_validation = validation(predict_detection_method,
                                        detection_method_prediction,
                                        predict_input_hex,
                                        'detection_method_predictions.txt')
    event_cause_validation = validation(predict_restore_method,
                                        fix_classification_prediction,
                                        predict_input_hex,
                                        'restore_method_predictions.txt')
    event_cause_validation = validation(predict_fix_classification,
                                        restore_method_prediction,
                                        predict_input_hex,
                                        'fix_classification_predictions.txt')
    event_cause_validation = validation(predict_relevance,
                                        relevance_prediction,
                                        predict_input_hex,
                                        'relevance_predictions.txt')
    event_cause_validation = validation(predict_subsystem,
                                        subsystem_prediction,
                                        predict_input_hex,
                                        'subsystem_predictions.txt')

    # End timer & total runtime
    end_time = time.time()
    runtime = round(end_time - start_time, 2)

    # Time taken per ticket
    avg_time_per_ticket = round(runtime / len(predict_input_hex), 2)

    print("\n" * 2)
    print("############################# METRICS ############################")
    print("Runtime: " + str(runtime) + "s")
    print("Average Time per Ticket: " + str(avg_time_per_ticket) + "s")
    print("Accuracy of system for test tickets - event cause label:  "
          + str(round(event_cause_validation, 4)))


if __name__ == "__main__":
    main()
