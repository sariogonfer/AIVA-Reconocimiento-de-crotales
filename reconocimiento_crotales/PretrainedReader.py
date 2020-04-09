from reconocimiento_crotales.BaseReader import BaseReader
from reconocimiento_crotales.SplitDigitExtractor import SplitDigitExtractor
from reconocimiento_crotales.Identifier import Identifier
from reconocimiento_crotales.TesseractDigitRecognition import TesseractDigitRecognition
from reconocimiento_crotales.PretrainedModelDigitRecognition import PretrainedModelDigitRecognition

# Clase que hereda de BaseReader y se conectará con un extractor de dígitos y un reconocedor de dígitos
class PretrainedReader(BaseReader):
    def __init__(self):
        self.digits_extractor = SplitDigitExtractor()
        # self.digits_recognition = TesseractDigitRecognition()
        self.digits_recognition = PretrainedModelDigitRecognition()

    # Método que sirve para conectar todos los procesos que debe realizarse en la imagen para obtener el Identifier
    # params
    # path: ruta de la imagen
    #
    # return
    # Identifier: Objeto con el valor a identificar

    def process_image(self, path):
        image = self._read_image(path)
        i, rois = self.digits_extractor.extract_digits(image)
        text = ''
        for r in rois:
            print(r)
            text += self.digits_recognition.predict(i, r)
        return Identifier(text,  image, rois)
