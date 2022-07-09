from .errors import TooManyArgumentsError, NotEnoughArgumentsError
from .messages import Messages
from .registry import CommandRegistry


class CommandRegister:
    def register_command(
        self,
        commands: list[str] | tuple[str],
        description: str,
        arguments: list[str] | tuple[str] = (),
        count_arguments: bool = True,
    ):
        arguments = self._prepare_arguments(arguments, count_arguments)
        commands = self._prepare_commands(commands)

        def decorator(func):
            command = CommandRegistry(func, commands, arguments, description)

            command.register()

            def wraper(*args):
                if count_arguments:
                    self._count_arguments(arguments, args)

                func(*args)

            return wraper
        return decorator

    def _count_arguments(self, required_args: list, provided_args: list):
        required_args = len(required_args)
        provided_args = (
            len(provided_args) - 1
            if isinstance(provided_args[0], object)
            else len(provided_args)
        )

        if provided_args > required_args:
            raise TooManyArgumentsError(
                required_args, Messages.TOO_MANY_ARGUMENTS_ERROR
            )

        if provided_args < required_args:
            raise NotEnoughArgumentsError(
                required_args, Messages.NOT_ENOUGH_ARGUMENTS_ERROR
            )

    def _prepare_commands(self, commands) -> tuple:
        self._validate_commands(commands)

        if len(commands) == 1:
            return commands

        return (
            commands
            if len(commands[0]) < len(commands[1])
            else (commands[1], commands[0])
        )

    def _validate_commands(self, commands):
        if not isinstance(commands, tuple) and not isinstance(commands, list):
            raise TypeError(Messages.TYPE_ERROR.format(name_of_arg="commands"))

        if not 0 < len(commands) < 3:
            raise TypeError(Messages.BAD_QUANTITY_OF_COMMANDS_ERROR)

    def _prepare_arguments(self, arguments, count_arguments: bool) -> list:
        if not count_arguments:
            return [Messages.MULTIPLE_ARGS]

        self._validate_arguments(arguments)

        return [f"<{argument}>" for argument in arguments]

    def _validate_arguments(self, arguments):
        if not isinstance(arguments, tuple) and not isinstance(arguments, list):
            raise TypeError(Messages.TYPE_ERROR.format(name_of_arg="arguments"))
