import time

from classify_tickets import classify_data
from data_processing import (encode_ticket_hex_codes,
                             get_event_cause_val,
                             convert_array_to_np_array)


def main():
    start_time = time.time()
    # TODO: Call the trained models with data here
    encoded_hex_codes = convert_array_to_np_array(encode_ticket_hex_codes())
    event_cause_options = convert_array_to_np_array(get_event_cause_val())
    event_cause_classification = classify_data(encoded_hex_codes,
                                               event_cause_options,
                                               'event_cause_weights.hdf5')

    with open('output.txt', 'w') as result_file:
        result_file.write("%s\n" % event_cause_classification)

    # write_to_file(event_cause_classification, 'output.txt')
    # print(event_cause_classification)

    end_time = time.time()
    runtime = round(end_time - start_time, 2)
    avg_time_per_ticket = round(runtime / 1583, 5)

    print("\n" * 2)
    print("############################ METRICS ############################")
    print("Runtime: " + str(runtime) + "s")
    print("AVG Time per Ticket: " + str(avg_time_per_ticket) + "s")


if __name__ == "__main__":
    main()
