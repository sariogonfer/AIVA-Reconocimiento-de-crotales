from reconocimiento_crotales.BaseReader import BaseReader
from reconocimiento_crotales.SplitDigitExtractor import SplitDigitExtractor
from reconocimiento_crotales.Identifier import Identifier
from reconocimiento_crotales.TesseractDigitRecognition import TesseractDigitRecognition

# Clase que hereda de BaseReader y se conectará con un extractor de dígitos y un reconocedor de dígitos
class PretrainedReader(BaseReader):
    def __init__(self):
        self.digits_extractor = SplitDigitExtractor()
        self.digits_recognition = TesseractDigitRecognition()

    # Método que sirve para conectar todos los procesos que debe realizarse en la imagen para obtener el Identifier
    # params
    # path: ruta de la imagen
    #
    # return
    # Identifier: Objeto con el valor a identificar

    def process_image(self, path):
        image = self.__read_image(path)
        i, rois = self.digits_extractor.extract_digits(image)
        text = ''
        for r in rois:
            text += self.digits_recognition.predict(image, r)

        return Identifier(text)
