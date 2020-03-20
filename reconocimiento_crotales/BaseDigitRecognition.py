# Clase abstracta de la que heredarán las clases que se dediquen al reconocimiento de dígitos
class BaseDigitRecognition():
    # Método abstracto encargado de la predicción de dígitos
    # params
    # image: imagen de la que se predecirán los dígitos
    # bb_star: posiciones (x,y) del inicio del Bbox
    # bb_end: posiciones (x,y) del fin del Bbox
    def predict(self, image, bb_start, bb_end):
        pass
