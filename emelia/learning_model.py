import tensorflow as tf
from tensorflow import keras

# import EMELIA.data_processing as dp
# from EMELIA.data_processing import encode_ticket_hex_codes, get_event_cause_val


def get_compiled_model():
    model = keras.Sequential()
    ###################### LAYERS ########################

    ###################### INPUT  ########################
    # Add layers
    # Embedding layer, looks up embedding vector for each word
    # TODO: uncomment line below if needed
    # model.add(keras.layers.Embedding(vocab_size, 16))

    ###################### HIDDEN ########################
    # Hidden layers are these next two consecutive add functions
    # model.add(keras.layers.GlobalAveragePooling1D())
    model.add(keras.layers.Dense(9, input_shape=(74,)))

    # 16 hidden units in the hidden layer using activation function
    model.add(keras.layers.Dense(9, activation=tf.nn.softmax))
    model.add(keras.layers.Dense(9, activation=tf.nn.softmax))
    model.add(keras.layers.Dense(9, activation=tf.nn.softmax))

    # To add more hidden layers, simply copy add line without the embedding func
    # model.add(keras.layers.Dense(16, activation=tf.nn.relu))
    # model.add(keras.layers.Dense(16, activation=tf.nn.relu))
    # model.add(keras.layers.Dense(16, activation=tf.nn.relu))

    ###################### OUTPUT ########################
    # Creates S curve graph (sigmoid) that contain output of 0 or 1
    # The activation function provides the confidence value (floating point)
    # The 2 in the Dense() is the number of hidden layers that are made above
    # model.add(keras.layers.Dense(3, activation=tf.nn.sigmoid))


    ##################### SUMMARY #######################
    # Provides summary table of the neural network for hidden layers and param data
    model.summary()

    # Add optimizer and loss function to determine the confidence based on the 1
    # or 0, measure distance of probability distributions.
        # binary_crossentropy selected based on the 0 or 1 values
        # accuracy is provided to the metric param to train the model
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    return model






