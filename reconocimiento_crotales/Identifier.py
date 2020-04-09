import base64
import cv2
import numpy as np

from reconocimiento_crotales.ExceptionIntCastFailure import ExceptionIntCastFailure

# Clase que alberga el valor extraido y lanza la excepción ExceptionIntCastFailure si hay algún problema
class Identifier:
    def __init__(self, id, image=None, rois=None):
        try:
            self.__id=id.replace(' ', '')
            self.__image = image
            self.__rois = rois
        except:
            raise ExceptionIntCastFailure(
                f'The {id} value is not a valid Identifier'
            )

    def get_value(self):
        return self.__id

    def get_image(self):
        return selg.__image

    def get_image_base64(self):
        _, im_arr = cv2.imencode('.jpg', self.__image)
        im_bytes = im_arr.tobytes()
        im_b64 = base64.b64encode(im_bytes)

        return im_b64.decode('ascii')

    def get_detected_image_base64(self):
        aux = self.__image.copy()
        for r in self.__rois:
            aux = cv2.rectangle(aux, *r, (255, 0, 0), 4)
        _, im_arr = cv2.imencode('.jpg', aux)
        im_bytes = im_arr.tobytes()
        im_b64 = base64.b64encode(im_bytes)

        return im_b64.decode('ascii')

