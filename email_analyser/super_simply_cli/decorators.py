from .errors import TooManyArgumentsError, NotEnoughArgumentsError
from .messages import Messages
from .register import CommandRegister
from .utilities import check_arguments, check_commands


def register_command(
    commands: tuple[str] | list[str],
    description: str,
    arguments: list[str] | tuple[str] = (),
    count_arguments: bool = True,
):
    arguments = check_arguments(arguments, count_arguments)
    commands = check_commands(commands)

    def register(method):
        index = len(CommandRegister.registered_tasks)

        CommandRegister.registered_tasks[index] = method.__name__
        CommandRegister.registered_commands[index] = commands
        CommandRegister.registered_arguments[index] = arguments
        CommandRegister.registered_descriptions[index] = description

        def validate_args(*args):
            if count_arguments:
                required_args = len(arguments)
                provided_args = len(args) - 1

                if provided_args > required_args:
                    raise TooManyArgumentsError(
                        required_args, Messages.TOO_MANY_ARGUMENTS_ERROR
                    )

                if provided_args < required_args:
                    raise NotEnoughArgumentsError(
                        required_args, Messages.NOT_ENOUGH_ARGUMENTS_ERROR
                    )

            method(*args)

        return validate_args

    return register
