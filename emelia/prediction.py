import threading
import pandas as pd

from classify_tickets import (convert_test_data, report_prediction_results,
                              report_ticket_id)
from data_processing import DataProcessor as dp
from learning_model import prediction
from progress import run_progress_bar


def generate_predictions(alarm, ticket, test, predictions):
    '''
    Function will perform the following actions:

    1. Create predictions using alarm data and saved state files of the
       learning model
    2. Report predictions results
    3. Store results in a pandas dataframe, which is converted to CSV file

            Parameters:
                alarm: alarm file needed to initialize DataProcessor
                ticket: ticket file needed to intialize DataProcessor
                test: file containing unclassified ticket data
                predictions: name of file needed to convert dataframe to CSV
                             (must be CSV filename)
    '''

    # Convert the alarm data to encoded np arrays
    result_alarm_np = convert_test_data(test, alarm, ticket)

    # Function that stores array of all ticket ID values in the alarm file
    ticket_id = report_ticket_id(test)

    # Create thread to run progress bar
    thread = threading.Thread(target=run_progress_bar, args=(len(ticket_id),))

    # Test Real Ticket Alarm Data
    # Start the thread needed to run the progress bar
    thread.start()

    # create prediction arrays using the input data from result_alarm_np
    test_EV = prediction(result_alarm_np, 'event_cause.hdf5')
    test_DM = prediction(result_alarm_np, 'detection_method.hdf5')
    test_RM = prediction(result_alarm_np, 'restore_method.hdf5')
    test_FC = prediction(result_alarm_np, 'fix_classification.hdf5')
    test_SUB = prediction(result_alarm_np, 'subsystem.hdf5')
    test_REL = prediction(result_alarm_np, 'relevance.hdf5')

    # Report the label under each classification and store the result in the
    # corresponding file. The order is the same as the alarm data order
    ev = report_prediction_results(test_EV, dp.event_cause_vals)
    dm = report_prediction_results(test_DM, dp.detection_method)
    rm = report_prediction_results(test_RM, dp.restore_method)
    fc = report_prediction_results(test_FC, dp.fix_classification)
    sub = report_prediction_results(test_SUB, dp.subsystem)
    rel = report_prediction_results(test_REL, dp.relevance)

    # Converts all of the arrays to a pandas dataframe to be written to single
    # output file
    df = pd.DataFrame({'TICKET ID': ticket_id, 'EVENT CAUSE': ev,
                       'DETECTION METHOD': dm, 'RESTORE METHOD': rm,
                       'FIX CLASSIFICATION': fc, 'SUBSYSTEM': sub,
                       'RELEVANCE': rel})

    # Convert dataframe to csv file
    df.to_csv(predictions, index=False)

    # Join thread
    thread.join()
