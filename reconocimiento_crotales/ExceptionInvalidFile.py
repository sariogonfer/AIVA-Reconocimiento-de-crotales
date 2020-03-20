# Excepción creada que se lanzará cuando haya un fallo en la lectura de una imagen
class ExceptionInvalidFile(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    def __str__(self):
        if self.message:
            return 'The image can not be read, {0} '.format(self.message)
        else:
            return 'The image can not be read'

