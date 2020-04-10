import os

import cv2
import numpy as np
from tensorflow import keras
from tensorflow.keras.models import model_from_json

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

    def _smooth_image(self, img):
        thresh = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)[1]
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 10))
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_ERODE, kernel)
        
        return thresh
        
        
    def predict(self, image, r):
        (startX, startY) = r[0]
        (endX, endY) = r[1]

        img = image[startY:endY, startX:endX]
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = ~img
        img = self._smooth_image(img)
        img = cv2.resize(img, (24, 24)) 
        zeros = np.zeros((28, 28))
        zeros[2:26, 2:26] = img
        img = zeros
        img = img / 255.
        img = img.reshape((28, 28, 1))
        r = str(self.model.predict_classes(np.array([img]))[0])
        
        return r
