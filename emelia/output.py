import time
import csv
import numpy as np

from classify_tickets import classify_data
from data_processing import (encode_ticket_hex_codes,
                             get_event_cause_val,
                             convert_array_to_np_array)
from predict import prediction


def main():
    start_time = time.time()
    # TODO: Call the trained models with data here
    encoded_hex_codes = convert_array_to_np_array(encode_ticket_hex_codes())
    event_cause_options = convert_array_to_np_array(get_event_cause_val())
   
    # event_cause_classification = classify_data(encoded_hex_codes,
    #                                           event_cause_options,
    #                                          'event_cause_weights.hdf5')
    
    
    # 20 percent that needs to be tested
    predict_input_hex = encoded_hex_codes[1266:]
    predict_actual = event_cause_options[1266:]
    
    
    result_array = prediction( predict_input_hex )
    
    
    # print statement to check array lengths: all 317
    # print("predict_input_hex length: " + str(len(predict_input_hex)) )
    # print("predict_actual length: " + str(len(predict_actual)) )
    # print("predict_result length: " + str(len(result_array)) )
    
    with open('result.csv', mode='w') as csv_file:
           fieldnames = ['Hex Code', 'Actual', 'Result', 'Correctly Classified']
           writer = csv.DictWriter(csv_file, fieldnames = fieldnames)

           writer.writeheader()
           
           #list(predict_actual)
           #list(result_array)
           predict_actual = np.array(predict_actual).tolist()
           result_array = np.array(result_array).tolist()
           #np.asarray(predict_actual)
           #np.asarray(result_array)
           
           length_of_array = len(predict_input_hex) #317
           
           num_of_vals = len(predict_actual[0]) #9
           
           
           # loops through rows
           for rows in range(length_of_array):
                  greatest_percent = max(result_array[rows])
                  boolean = False
                  position = 0
                  
                  for index in range(num_of_vals):
                         if result_array[rows][index] == greatest_percent:
                                position = index
                                
                  for working_index in range(num_of_vals):
                         if predict_actual[rows][working_index] == 1 and working_index == position:
                                boolean = True
                                
                  
                  #position_of_actual = predict_actual.index(max(predict_actual))
                  #position_of_actual = predict_actual[np.array([(max(predict_actual))])]
                  #position_of_actual = np.where(predict_actual == max(predict_actual))
                  
                  #position_of_result = result_array.index(max(result_array))
                  #position_of_result = result_array[np.array([(max(result_array))])]
                  #position_of_result = np.where(result_array == max(result_array))
       
                  writer.writerow({'Hex Code': predict_input_hex[rows], 
                                   'Actual': predict_actual[rows], 
                                   'Result': result_array[rows],
                                   'Correctly Classified': boolean})
           csv_file.close()
           
                              

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
