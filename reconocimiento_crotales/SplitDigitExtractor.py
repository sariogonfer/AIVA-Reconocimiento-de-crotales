import cv2
import imutils
import os
import math
import numpy as np

from skimage.morphology import convex_hull_image

from reconocimiento_crotales.BaseDigitExtractor import BaseDigitExtractor

class SplitDigitExtractor(BaseDigitExtractor):
    def _filter_contours(self, contours):
        contours = [c for c in contours if c[3] > 20 and c[3] > c[2]]
        b = max(contours, key=lambda c: c[1])
        contours = [c for c in contours if c[1] < b[1] + b[3] and c[1] > b[1] - b[3] and c[1] + c[3] > b[1]]
        
        return contours
    
    def _smooth_image(self, img):
        thresh = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)[1]
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 5))
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        
        return thresh
        
    def _remove_noise(self, img):
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8, 8))
        aux = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
        
        return aux
    
    def _contours_left_to_rigth(self, contours):
        return sorted(contours, key=lambda c: c[0])
        
    def extract_digits(self, image):
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        img = self._smooth_image(img)
        chull = convex_hull_image(img)
        img = chull + img
        img = self._remove_noise(img)
        img = img * 255
        _, contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = [cv2.boundingRect(c) for c in contours]
        contours = self._filter_contours(contours)
        contours = self._contours_left_to_rigth(contours)
        
        return image, [((x, y), (x+w, y+h))for x, y, w, h in contours]