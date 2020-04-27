import tensorflow as tf
from keras.layers import Dense, Dropout
from keras.models import Sequential


def get_compiled_model(input_dimension, input_num, dropout, output):
    # ##################### LAYERS ####################### #
    model = Sequential()
    # ##################### INPUT  ####################### #
    model.add(Dense(input_num,
                    input_dim=input_dimension,
                    activation='relu',
                    kernel_initializer='normal'))

    # ##################### HIDDEN ####################### #
    model.add(Dropout(dropout))

    # ##################### OUTPUT ####################### #
    model.add(Dense(output, activation='softmax', kernel_initializer='normal'))

    # #################### SUMMARY ###################### #
    model.summary()

    model.compile(optimizer='rmsprop',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    return model


# Store the state of the learning model in the following hdf5 file
def prediction(test_input, filename):
    modelpath = './models/' + filename
    model = tf.keras.models.load_model(modelpath)
    return model.predict(test_input)
