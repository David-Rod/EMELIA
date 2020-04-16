import time
import csv
import numpy as np
from learning_model import prediction
from classify_tickets import classify_data
from data_processing import (encode_ticket_hex_codes,
                             get_event_cause_val,
                             convert_array_to_np_array,
                             zerolistmaker)


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
    # predict_input_hex = encoded_hex_codes[1266:]
    predict_input_hex = encoded_hex_codes[2132:]
    # predict_actual = event_cause_options[1266:]
    predict_actual = event_cause_options[2132:]

    # calling prediction from predict.py and returns array of confidence values
    result_array = prediction(np.array(predict_input_hex))

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

        length_of_array = len(predict_input_hex)  # 317

        num_of_vals = len(predict_actual[0])  # 9

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
            for working_index in range(num_of_vals):
                if predict_actual[rows][working_index] == 1 \
                    and working_index == position:
                    boolean = True

            writer.writerow({'Hex Code': predict_input_hex[rows],
                             'Actual': predict_actual[rows],
                             'Result': result_array[rows],
                             'Correctly Classified': boolean})
        csv_file.close()

    # end timer
    end_time = time.time()

    # run time
    runtime = round(end_time - start_time, 2)
    avg_time_per_ticket = round(runtime / 1583, 5)

    print("\n" * 2)
    print("############################ METRICS ############################")
    print("Runtime: " + str(runtime) + "s")
    print("AVG Time per Ticket: " + str(avg_time_per_ticket) + "s")


if __name__ == "__main__":
    main()
