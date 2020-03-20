from reconocimiento_crotales.BaseReader import BaseReader
from reconocimiento_crotales.SplitDigitExtractor import SplitDigitExtractor
from reconocimiento_crotales.Identifier import Identifier
from reconocimiento_crotales.TesseractDigitRecognition import TesseractDigitRecognition

class PretrainedReader(BaseReader):
    def __init__(self):
        self.digits_extractor = SplitDigitExtractor()
        self.digits_recognition = TesseractDigitRecognition()

    def process_image(self, path):
        image = self._read_image(path)
        i, rois = self.digits_extractor.extract_digits(image)
        text = ''
        for r in rois:
            text += self.digits_recognition.predict(image, r)

        return Identifier(text)
