import os
import tensorflow as tf
from keras.layers import Dense, Dropout
from keras.models import Sequential

# Ignore warnings regarding supported CPU instructions
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Set tensorflow logging to ignore warnings and report errors only
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)


def get_compiled_model(input_dimension, input_num, dropout, output):
    '''
    Function accepts parameters need to construct and compile TensorFlow
    learning model. Returns compiled model.

    Parameters:

    input_dimension: dimesion of input array provided to the model

    input_num: number of neurons within input layer

    dropout: dropout rate for hidden layer (float value)

    output: number of neurons in output layer
    '''

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
    # model.summary()

    model.compile(optimizer='rmsprop',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    return model


def prediction(test_input, filename):
    '''
    Function will utilize directory of saved state files, load the file
    containing learning model state, and create predictions using predict
    method.

    Parameters:

    test_input: alarm hex values used as input

    filename: name of the .hdf5 state file
    '''
    modelpath = './models/' + filename
    model = tf.keras.models.load_model(modelpath)
    return model.predict(test_input)
