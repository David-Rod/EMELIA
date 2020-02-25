from __future__ import absolute_import, division, print_function, \
    unicode_literals


model_path = 'models/event_cause_weights.hdf5'

# from keras.models import model_from_json

from learning_model import get_compiled_model


# training model 
def classify_data(alarm_input_data, classification_label_data, filepath):
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
     
    
    # x_train = encode_ticket_hex_codes()[:1266]
    # y_train = get_event_cause_val()[:1266]
    # x_train = alarm_input_data[:1266]
    # y_train = classification_label_data[:1266]
    x_train = alarm_input_data[:1012]
    y_train = classification_label_data[:1012]
    

    # x_test = encode_ticket_hex_codes()[1266:]
    # y_test = get_event_cause_val()[1266:]
    # x_test = alarm_input_data[1266:]
    # y_test = classification_label_data[1266:]
    x_test = alarm_input_data[1012:1266]
    y_test = classification_label_data[1012:1266]
    

    model = get_compiled_model()

    # Epochs pass the data n times through the system
    history = model.fit(x_train,
                        y_train,
                        epochs=50,
                        batch_size=75,
                        validation_data=(x_test, y_test),
                        verbose=1)
    
    # saves the model in the filepath listed
    model.save('./models/' + filepath)
    
    
    # model_json_string = model.to_json()
    # model = model_from_json(model_json_string)
    # model.save_weights(filepath=filepath)
    results = model.evaluate(x_test, y_test)
    # Eval accuracy of model on test data using the test labels in the file
    # results = model.evaluate(test_data, test_labels)
    print(history)
    print("Results: " + str(results))
