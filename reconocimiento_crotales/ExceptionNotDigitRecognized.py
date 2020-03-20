# Excepción creada que se lanzará cuando ningún dígito sea reconocido en el Bbox pertinente
class ExceptionNotDigitRecognized(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    def __str__(self):
        if self.message:
            return 'The digit was not recognized, {0} '.format(self.message)
        else:
            return 'The digit was not recognized'

