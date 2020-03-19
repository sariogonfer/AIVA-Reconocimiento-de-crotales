from reconocimiento_crotales.BaseReader import BaseReader
from reconocimiento_crotales.BaseDigitExtractor import BaseDigitExtractor
from reconocimiento_crotales.SplitDigitExtractor import SplitDigitExtractor
from reconocimiento_crotales.Identifier import Identifier

class PretrainedReader(BaseReader):
    def read_image(self, path):
        return super().read_image(path)

    def digits_extractor(self, image, extractor):
        return extractor.detect_boundaries(image)

    def digits_recognition(self, image, rois, recognition):
        return Identifier(recognition.predict(image, rois))

