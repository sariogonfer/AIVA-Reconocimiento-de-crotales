from reconocimiento_crotales.ExceptionInvalidFile import ExceptionInvalidFile
import cv2


class BaseReader():
    def read_image(self, path):
        image=cv2.imread(path)
        if image is  None:
            raise ExceptionInvalidFile()
        else:
            return image
