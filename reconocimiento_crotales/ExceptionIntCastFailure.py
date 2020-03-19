class ExceptionIntCastFailure(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    def __str__(self):
        if self.message:
            return 'The value can not cast to int, {0} '.format(self.message)
        else:
            return 'The value can not cast to int'

