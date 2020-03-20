from reconocimiento_crotales.PretrainedReader import PretrainedReader
from reconocimiento_crotales.SplitDigitExtractor import SplitDigitExtractor
from reconocimiento_crotales.BaseDigitRecognition import BaseDigitRecognition
from reconocimiento_crotales.PretrainedModelDigitRecognition import PretrainedModelDigitRecognition
from reconocimiento_crotales.BaseDigitExtractor import BaseDigitExtractor
import cv2
import fire


class App:
    def process_image(self, path):
        reader = PretrainedReader()
        return reader.process_image(path)


if __name__ == '__main__':
    fire.Fire(App)
