from __future__ import absolute_import, division, print_function, \
    unicode_literals
from sklearn.model_selection import train_test_split

from learning_model import get_compiled_model


# training model
def classify_data(alarm_input_data, classification_label_data, filepath):

    x_ticket_data = classification_label_data[:2132]
    y_alarm_data = alarm_input_data[:2132]

    x_train, x_test, y_train, y_test = train_test_split(x_ticket_data,
                                                        y_alarm_data,
                                                        test_size=0.20,
                                                        random_state=0)

    # x_train = alarm_input_data[:1012]
    # x_train = alarm_input_data[316:1050]   USED LAST
    # y_train = classification_label_data[:1012]
    #y_train = classification_label_data[316:1050]   USED LAST

    # x_test = alarm_input_data[1012:1266]
    #x_test = alarm_input_data[1050:]   USED LAST
    # y_test = classification_label_data[1012:1266]
    #y_test = classification_label_data[1050:]   USED LAST

    model = get_compiled_model()

    # Epochs pass the data n times through the system
    history = model.fit(x_train,
                        y_train,
                        epochs=30,
                        batch_size=50,
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
