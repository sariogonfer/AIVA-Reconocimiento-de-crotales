import os

import cv2
import keras
import numpy as np
from keras.models import model_from_json

from reconocimiento_crotales.BaseDigitRecognition import BaseDigitRecognition

# Clase que reconocerá los digitos a partir de una Red Neuronal (futura entrega)
class PretrainedModelDigitRecognition(BaseDigitRecognition):

    def __init__(self):

        foo = os.path.join(
            os.path.dirname(__file__), 'models/model.json'
        )
        bar = os.path.join(
            os.path.dirname(__file__), 'models/model.h5'
        )


        with open(foo, 'r') as json_file:
            json_savedModel= json_file.read()
        self.model = model_from_json(json_savedModel)
        self.model.load_weights(bar)

        self.model.compile(loss=keras.losses.categorical_crossentropy,
                      optimizer=keras.optimizers.Adadelta(),
                      metrics=['accuracy'])


    def predict(self, image, r):
        (startX, startY) = r[0]
        (endX, endY) = r[1]

        img = image[startY:endY, startX:endX]
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, (28, 28))
        _, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        img = cv2.bitwise_not(img)
        img = img / 255.
        img = img.reshape((28, 28, 1))
        r = str(self.model.predict_classes(np.array([img]))[0])
        # print(r)
        return r
