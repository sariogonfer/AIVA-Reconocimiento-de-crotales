from reconocimiento_crotales.ExceptionIntCastFailure import ExceptionIntCastFailure


class Identifier:
    def __init__(self, id):
        try:
            self.__id=int(id)
        except:
            raise ExceptionIntCastFailure()

    def get_value(self):
        return self.__id