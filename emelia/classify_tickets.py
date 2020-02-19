from __future__ import absolute_import, division, print_function, \
    unicode_literals

import time

from data_processing import (encode_ticket_hex_codes,
                             get_event_cause_val)
from testNN import get_compiled_model


def main():
    start_time = time.time()
    '''
    def get_compiled_model():

        model = tf.keras.Sequential([
            tf.keras.layers.Dense(10, activation='softmax'),
            tf.keras.layers.Dense(10, activation='softmax'),
            tf.keras.layers.Dense(10, activation='softmax'),
            tf.keras.layers.Dense(10, activation='softmax'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])

        model.compile(optimizer='adam',
                      loss='binary_crossentropy',
                      metrics=['accuracy'])
        return model
    '''

    x_train = encode_ticket_hex_codes()[:1266]
    y_train = get_event_cause_val()[:1266]

    x_test = encode_ticket_hex_codes()[1266:]
    y_test = get_event_cause_val()[1266:]

    model = get_compiled_model()

    # Epochs pass the data n times through the system
    history = model.fit(x_train,
                        y_train,
                        epochs=50,
                        batch_size=75,
                        validation_data=(x_test, y_test),
                        verbose=1)

    # results = model.evaluate(x_test, y_test)
    # Eval accuracy of model on test data using the test labels in the file
    # results = model.evaluate(test_data, test_labels)
    print(history)

    end_time = time.time()
    runtime = round(end_time - start_time, 2)
    avg_time_per_ticket = round(runtime / 1583, 5)

    print("\n" * 2)
    print("############################ METRICS ############################")
    print("Runtime: " + str(runtime) + "s")
    print("AVG Time per Ticket: " + str(avg_time_per_ticket) + "s")


if __name__ == "__main__":
    main()
