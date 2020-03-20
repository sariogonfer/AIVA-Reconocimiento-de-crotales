# Excepción creada que se lanzará cuando ningún dígito sea detectado en un Bbox
class ExceptionNotDigitDetected(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    def __str__(self):
        if self.message:
            return 'The digit was not detected, {0} '.format(self.message)
        else:
            return 'The digit was not detected'

