import tensorflow as tf
from tensorflow import keras


def get_compiled_model():
    # ##################### LAYERS ####################### #
    model = keras.Sequential()
    # ##################### INPUT  ####################### #

    model.add(keras.layers.Dense(125, input_dim=101, activation=tf.nn.relu))

    # ##################### HIDDEN ####################### #
    model.add(keras.layers.Dense(120, activation=tf.nn.relu))
    model.add(keras.layers.Dense(110, activation=tf.nn.relu))
    model.add(keras.layers.Dropout(0.3))

    # ##################### OUTPUT ####################### #
    model.add(keras.layers.Dense(101, activation=tf.nn.softmax))

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
