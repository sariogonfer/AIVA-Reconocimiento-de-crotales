from reconocimiento_crotales.ExceptionInvalidFile import ExceptionInvalidFile
import cv2

# Clase que se dedicará a la lectura de imágenes
class BaseReader():
    # Método que se encarga de la lectura de imágenes que en caso de ser erronea, lanzará la excepcion ExceptionInvalidFile
    # params
    # path: ruta de la imagen
    #
    # return
    # image: imagen ya leida
    def _read_image(self, path):
        #print(path)
        image=cv2.imread(path)
        if image is  None:
            raise ExceptionInvalidFile()
        else:
            return image
