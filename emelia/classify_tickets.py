from __future__ import absolute_import, division, print_function, \
    unicode_literals
import csv
import numpy as np

from sklearn.model_selection import train_test_split
from learning_model import get_compiled_model


# training model
def classify_data(alarm_data, classification_label_data, filepath,
                  input_dimension, input_num, dropout, output):
    """
        x_data is what is fed into the NN. This will be the encoded alarm
        values for each ticket.

        y_data are the encoded label values that correspond to each ticket.
    """
    x_data = alarm_data[:2132]
    y_data = classification_label_data[:2132]

    x_train, x_test, y_train, y_test = train_test_split(x_data,
                                                        y_data,
                                                        test_size=0.20,
                                                        random_state=0)

    model = get_compiled_model(input_dimension, input_num, dropout, output)

    # Epochs pass the data n times through the system
    history = model.fit(x_train,
                        y_train,
                        epochs=20,
                        batch_size=20,
                        validation_data=(x_test, y_test),
                        verbose=2)

    # saves the model in the filepath listed
    model.save('./models/' + filepath)

    # Eval accuracy of model on test data using the test labels in the file
    test_results = model.evaluate(x_test, y_test)
    train_results = model.evaluate(x_train, y_train)

    print(history.model)
    print("Test Evaluation: " + str(test_results))
    print("Train Evaluation: " + str(train_results))


'''
    TODO: Convert this to doc string
    result.csv contains corresp. hex code,
    the correct classification (Actual),
    predicition (result) and if the
    prediction was correct (Correctly Classified)
'''


def validation(prediction_list, result_array, input_hex, filename):
    with open(filename, mode='w') as csv_file:
        fieldnames = ['Hex Code', 'Actual',
                      'Result', 'Correctly Classified']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        # Converting np arrays to lists
        # predict_actual = np.array(predict_actual).tolist()
        predict_actual = np.array(prediction_list).tolist()
        result_array = np.array(result_array).tolist()

        length_of_array = len(input_hex)
        num_of_vals = len(predict_actual[0])
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

            writer.writerow({'Hex Code': input_hex[rows],
                             'Actual': predict_actual[rows],
                             'Result': result_array[rows],
                             'Correctly Classified': boolean})
        csv_file.close()

    return true_counter / length_of_array
