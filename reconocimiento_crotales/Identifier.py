from reconocimiento_crotales.ExceptionIntCastFailure import ExceptionIntCastFailure

# Clase que alberga el valor extraido y lanza la excepción ExceptionIntCastFailure si hay algún problema
class Identifier:
    def __init__(self, id):
        try:
            self.__id=id.replace(' ', '')
        except:
            raise ExceptionIntCastFailure(
                f'The {id} value is not a valid Identifier'
            )

    def get_value(self):
        return self.__id
