from reconocimiento_crotales.BaseReader import BaseReader
from reconocimiento_crotales.SplitDigitExtractor import SplitDigitExtractor
from reconocimiento_crotales.Identifier import Identifier
from reconocimiento_crotales.PretrainedModelDigitRecognition import PretrainedModelDigitRecognition

class PretrainedReader(BaseReader):
    def __init__(self):
        self.digits_extractor = SplitDigitExtractor()
        self.digits_recognition = PretrainedModelDigitRecognition()

    def process_image(self, path):
        image = self._read_image(path)
        digits = self.digits_extractor.extract_digits(image)
        value = self.digits_recognition(*digits).get_value()

        return value
