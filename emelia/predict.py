import numpy as np
#import keras
from keras.models import load_model

import tensorflow as tf 

modelpath = './models/event_cause_weights.hdf5'

#whatever the test path is
testpath = ""

#model = load_model( modelpath )
model = tf.keras.models.load_model(modelpath)

# pass in file that contains only 20 percent of hex values that need to be predicted
def prediction(test_input):
       # array = model.predict(x)
       # result = array[0]
       # answer = np.argmax(result)
       
       return model.predict(test_input)
      
       #return model.predict_classes(test_input[:3])
       
       
       
       

