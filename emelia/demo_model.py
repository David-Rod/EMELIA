
from __future__ import absolute_import, division, print_function, unicode_literals

import os

# import matplotlib.pyplot as plt
import tensorflow as tf

from data_processing import (encode_ticket_hex_codes, get_event_cause_val, get_labels)


train_dataset = encode_ticket_hex_codes()[:1266]
class_names = get_labels() #data labels ex. system fault
label_name = 'Error Type'


# print("Local copy of the dataset file: {}".format(class_names))

batch_size = 32

train_dataset = tf.data.experimental.make_csv_dataset(
    train_dataset,
    batch_size,
    column_names = class_names,
    label_name = label_name,
    num_epochs = 1)

features, labels = next(iter(train_dataset))

print(features)