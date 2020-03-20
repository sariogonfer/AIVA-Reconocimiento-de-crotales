# Clase abstracta de la que heredarán las clases que se dediquen a la extracción de dígitos
class BaseDigitExtractor:
    # Método abstracto encargado de la extracción de dígitos
    # params
    # image: imagen de la que se extraerán los dígitos
    def extract_digits(self, image):
        raise NotImplementedError
