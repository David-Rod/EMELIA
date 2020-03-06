from __future__ import absolute_import, division, print_function, \
    unicode_literals

from learning_model import get_compiled_model


# training model 
def classify_data(alarm_input_data, classification_label_data, filepath):
    
    x_train = alarm_input_data[:1012]
    y_train = classification_label_data[:1012]

    x_test = alarm_input_data[1012:1266]
    y_test = classification_label_data[1012:1266]
    
    model = get_compiled_model()

    # Epochs pass the data n times through the system
    history = model.fit(x_train,
                        y_train,
                        epochs=15,
                        batch_size=5,
                        validation_data=(x_test, y_test),
                        verbose=2)
    
    # saves the model in the filepath listed
    model.save('./models/' + filepath)
    
    # Eval accuracy of model on test data using the test labels in the file
    results = model.evaluate(x_test, y_test)

    print(history)
    print("Results: " + str(results))
