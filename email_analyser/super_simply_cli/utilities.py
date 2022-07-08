from typing import Any

from .messages import Messages


def check_commands(commands: Any) -> tuple:
    if not isinstance(commands, tuple) and not isinstance(commands, list):
        raise TypeError(Messages.TYPE_ERROR.format(name_of_arg="commands"))

    quantity_of_commands = len(commands)

    if not 0 < quantity_of_commands < 3:
        raise TypeError(Messages.BAD_QUANTITY_OF_COMMANDS_ERROR)

    if quantity_of_commands == 1:
        return commands

    return (
        commands if len(commands[0]) < len(commands[1]) else (commands[1], commands[0])
    )


def check_arguments(arguments: Any, check_arguments: bool) -> list:
    if not check_arguments:
        return [Messages.MULTIPLE_ARGS]

    if not isinstance(arguments, tuple) and not isinstance(arguments, list):
        raise TypeError(Messages.TYPE_ERROR.format(name_of_arg="arguments"))

    return [f"<{argument}>" for argument in arguments]
