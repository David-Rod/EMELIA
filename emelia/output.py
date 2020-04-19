import time
import csv
import numpy as np
from learning_model import prediction
from classify_tickets import classify_data
from data_processing import (encode_ticket_hex_codes,
                             get_event_cause_val,
                             convert_array_to_np_array)


def main():
    # starting timer
    start_time = time.time()

    # converting lists to numpy array
    encoded_hex_codes = convert_array_to_np_array(encode_ticket_hex_codes())
    event_cause_options = convert_array_to_np_array(get_event_cause_val())

    # training & saving the model
    classify_data(encoded_hex_codes,
                  event_cause_options,
                  'event_cause_weights.hdf5')

    # 20 percent that needs to be tested
    predict_input_hex = encoded_hex_codes[2132:]
    predict_actual = event_cause_options[2132:]

    # calling prediction from predict.py and returns array of confidence values
    result_array = prediction(predict_input_hex)

    '''result.csv contains corresp. hex code,
    the correct classification (Actual),
    predicition (result) and if the
    prediction was correct (Correctly Classified)
    '''
    with open('result.csv', mode='w') as csv_file:
        fieldnames = ['Hex Code', 'Actual', 'Result', 'Correctly Classified']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        # Converting np arrays to lists
        predict_actual = np.array(predict_actual).tolist()
        result_array = np.array(result_array).tolist()

        length_of_array = len(predict_input_hex)  # 533 values from 2132-2665
        num_of_vals = len(predict_actual[0])  # 9 values for the assoc label
        true_counter = 0
        # loops through rows
        for rows in range(length_of_array):
            greatest_percent = max(result_array[rows])
            boolean = False
            position = 0

            # gets the index of largest confidence value
            for index in range(num_of_vals):
                if result_array[rows][index] == greatest_percent:
                    position = index

            # if the index of largest confidence value equals the index of
            # actual classification
            for index in range(num_of_vals):
                if predict_actual[rows][index] == 1 and index == position:
                    boolean = True
                    true_counter += 1

            writer.writerow({'Hex Code': predict_input_hex[rows],
                             'Actual': predict_actual[rows],
                             'Result': result_array[rows],
                             'Correctly Classified': boolean})
        csv_file.close()

    # end timer
    end_time = time.time()

    # run time
    runtime = round(end_time - start_time, 2)
    avg_time_per_ticket = round(runtime / 2665, 5)

    print("\n" * 2)
    print("############################# METRICS ############################")
    print("Runtime: " + str(runtime) + "s")
    print("Average Time per Ticket: " + str(avg_time_per_ticket) + "s")
    print("Accuracy of system for test tickets - event cause label:  "
          + str(true_counter / length_of_array))


if __name__ == "__main__":
    main()
