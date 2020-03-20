import cv2
import numpy as np
import pytesseract
import platform
from reconocimiento_crotales.BaseDigitRecognition import BaseDigitRecognition
from reconocimiento_crotales.ExceptionNotDigitRecognized import ExceptionNotDigitRecognized


class TesseractDigitRecognition(BaseDigitRecognition):
    def predict(self, image, r):
        (startX, startY) = r[0]
        (endX, endY) = r[1]

        if platform.system()=="Windows":
            # Need to specify the path only in widows systems
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        roi = image[startY:endY, startX:endX]
        config = ("-l eng --oem 1 --psm 7 -c tessedit_char_whitelist=0123456789")
        return pytesseract.image_to_string(roi, config=config)

    def model(self):
        #TO DO: Implementar conexión con rrnn MNIST para mejorar resultados
        return None
