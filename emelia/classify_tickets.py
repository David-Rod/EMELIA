from __future__ import absolute_import, division, print_function, \
    unicode_literals
from sklearn.model_selection import train_test_split

from learning_model import get_compiled_model


# training model
def classify_data(alarm_data, classification_label_data, filepath):
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

    model = get_compiled_model()

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
