import cv2
import numpy as np
import pytesseract
from reconocimiento_crotales.ExceptionNotDigitRecognized import ExceptionNotDigitRecognized
import platform

class BaseDigitRecognition():
    def predict(self, image, bb_start, bb_end):
        pass
