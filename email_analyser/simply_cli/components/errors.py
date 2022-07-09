class AmountOfArgumentsError(Exception):
    def __init__(self, required_args, *args):
        self.required_args = required_args
        super().__init__(*args)


class TooManyArgumentsError(AmountOfArgumentsError):
    pass


class NotEnoughArgumentsError(AmountOfArgumentsError):
    pass
