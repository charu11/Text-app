import tensorflow
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pandas as pd

import time
import urllib
import urllib.request
import re

label_list = ['User Interface', 'Debug', 'Document and Text', 'Integration', 'Core']

text_dir = ''
model_dir = '../models/text_model.h5'
max_length = 100


text = ['']


def text_classification(text):
    model = tensorflow.keras.models.load_model(model_dir)
    # df = pd.read_csv(text_dir)

    token = Tokenizer()
    token.fit_on_texts(text)
    seq = token.texts_to_sequences(text)
    pad_seq = pad_sequences(seq, maxlen=max_length, padding='post')

    # predict the model
    pred = model.predict(pad_seq)
    print(pred)
    classes = np.argmax(pred, axis=1)
    #classes = classes.tolist()
    print(classes[0])

    return None


text_classification(text)
