from reconocimiento_crotales.PretrainedReader import PretrainedReader
from reconocimiento_crotales.SplitDigitExtractor import SplitDigitExtractor
from reconocimiento_crotales.BaseDigitRecognition import BaseDigitRecognition
from reconocimiento_crotales.PretrainedModelDigitRecognition import PretrainedModelDigitRecognition
from reconocimiento_crotales.BaseDigitExtractor import BaseDigitExtractor
import cv2

"""
r=PretrainedReader()
image=r.read_image("images/TestSamples/0004.TIF")
b=SplitDigitExtractor()
rois=b.detect_boundaries(image)
print(rois)
j=PretrainedModelDigitRecognition()
print(j.predict(image, rois))
"""


reader=PretrainedReader()
image=reader.read_image("images/TestSamples/0004.TIF")
digit_extractor=SplitDigitExtractor()
image, rois=reader.digits_extractor(image,digit_extractor)
digit_recognition=PretrainedModelDigitRecognition()
print(reader.digits_recognition(image, rois, digit_recognition).get_value())
