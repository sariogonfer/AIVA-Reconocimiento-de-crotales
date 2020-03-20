from reconocimiento_crotales.PretrainedReader import PretrainedReader
import fire

# Clase que sirve de interfaz al usuario para manejar la aplicacion
class App:
    # Conecta la interfaz con la clase PretrainedReader para acabar devolviendo el valor del Identifier
    # params
    # path: ruta de la imagen
    #
    # return
    # id: valor del identificador
    def process_image(self, path):
        reader = PretrainedReader()
        identifier = reader.process_image(path)
        return identifier.get_value()


if __name__ == '__main__':
    fire.Fire(App)
