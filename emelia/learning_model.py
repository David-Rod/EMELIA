import tensorflow as tf
# from tensorflow import keras
from keras.layers import Dense, Dropout, Input
from keras.models import Sequential, Model
# from keras.metrics import categorical_accuracy

# from keras.models import load_model

# import EMELIA.data_processing as dp
# from EMELIA.data_processing import encode_ticket_hex_codes, get_event_cause_val


def get_compiled_model():
    # model = keras.Sequential()
    model = Sequential()
    ###################### LAYERS ########################
    # Add layers
    ###################### INPUT  ########################

    # Embedding layer, looks up embedding vector for each word
    #inputs = model.add(keras.layers.Dense(125,
    #                                      input_shape=(101,),
    #                                      kernel_initializer='normal'))
    model.add(Dense(125,
                    input_shape=(101,),
                    kernel_initializer='normal'))
    # inputs = Input(shape=(101,))
    #model.add(Dense(125, activation=tf.nn.relu, kernel_initializer='normal')) #125, inp,activation=tf.nn.relu))
    model.add(Dropout(0.5))
    # model.add(keras.layers.Dense(125, activation=tf.nn.relu))
    '''
    model.add(keras.layers.Dropout(32,
                                 activation=tf.nn.softmax,
                                 kernel_constraint=unit_norm(1)))
    '''
    ###################### HIDDEN ########################

    # 16 hidden units in the hidden layer using activation function
    # model.add(keras.layers.Dense(125, activation=tf.nn.relu))
    model.add(Dense(125, activation=tf.nn.relu))
    # model.add(Dropout(0.5))

    ###################### OUTPUT ########################
    # predictions = model.add(keras.layers.Dense(9, activation=tf.nn.softmax))
    model.add(Dense(101, activation=tf.nn.softmax))
    # model = Model(input=inputs, output=predictions)

    ##################### SUMMARY #######################
    # Provides summary table of the neural network for hidden layers and param data
    # model.summary()

    # model = Model(input=inputs, output=predictions)
    # Add optimizer and loss function to determine the confidence based on the 1
    # or 0, measure distance of probability distributions.
        # binary_crossentropy selected based on the 0 or 1 values
        # accuracy is provided to the metric param to train the model
    model.compile(optimizer='rmsprop',
                  loss='categorical_crossentropy',
                  metrics=['acc'])

    return model


# pass in file that contains only 20 percent of hex values that need to be predicted
def prediction(test_input):
    modelpath = "./models/event_cause_weights.hdf5"
    model = tf.keras.models.load_model(modelpath)
    return model.predict(test_input)
