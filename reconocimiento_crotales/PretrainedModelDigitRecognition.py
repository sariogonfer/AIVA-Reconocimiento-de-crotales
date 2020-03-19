from reconocimiento_crotales.BaseDigitRecognition import BaseDigitRecognition


class PretrainedModelDigitRecognition(BaseDigitRecognition):
    def predict(self, image, rois):
        text=""
        for r in rois:
            text=text+super().predict(image, r[0], r[1])
        return text

    def model(self):
        #TO DO: Implementar conexión con rrnn MNIST para mejorar resultados
        return None
