import tensorflow as tf
from keras.layers import Dense, Dropout
from keras.models import Sequential


def get_compiled_model():
    # ##################### LAYERS ####################### #
    model = Sequential()
    # ##################### INPUT  ####################### #

    model.add(Dense(110,
                    input_dim=101,
                    activation='relu',
                    kernel_initializer='normal'))

    # ##################### HIDDEN ####################### #
    model.add(Dropout(0.8))

    # ##################### OUTPUT ####################### #
    model.add(Dense(9, activation='softmax', kernel_initializer='normal'))

    # #################### SUMMARY ###################### #
    model.summary()

    model.compile(optimizer='rmsprop',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    return model


# Store the state of the learning model in the following hdf5 file
def prediction(test_input):
    modelpath = "./models/event_cause_weights.hdf5"
    model = tf.keras.models.load_model(modelpath)
    return model.predict(test_input)
