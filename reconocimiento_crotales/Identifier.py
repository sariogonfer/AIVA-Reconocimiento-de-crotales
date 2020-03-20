from reconocimiento_crotales.ExceptionIntCastFailure import ExceptionIntCastFailure


class Identifier:
    def __init__(self, id):
        try:
            self.__id=int(id.replace(' ', ''))
        except:
            raise ExceptionIntCastFailure(
                f'The {id} value is not a valid Identifier'
            )

    def get_value(self):
        return self.__id
