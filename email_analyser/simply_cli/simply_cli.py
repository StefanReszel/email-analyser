from sys import argv

from .components import (
    Messages,
    TooManyArgumentsError,
    NotEnoughArgumentsError,
    Commands,
    CommandRegistry,
    CommandRegister,
)


register_command = CommandRegister().register_command


class SimplyCLI:
    def __init__(self):
        self.commands = Commands()
        self.tasks = CommandRegistry.registered_tasks

    def run(self):
        task_id = self.commands.get_command_id(argv[1]) if len(argv) > 1 else 0
        task_name = self.tasks.get(task_id, "_command_does_not_exist")

        task = getattr(self, task_name)
        arguments = argv[2:]

        try:
            task(*arguments)
        except (TooManyArgumentsError, NotEnoughArgumentsError) as error:
            if error.required_args == 0:
                print(Messages.TAKES_NO_ARGUMENTS_ERROR)
            else:
                print(error)

    @register_command(("--help", "-h"), "Show help.")
    def _help(self):
        print(Messages.HELP)
        for index in range(len(self.commands.commands)):

            commands = ", ".join(self.commands.commands[index])
            arguments = " ".join(self.commands.arguments[index])
            description = self.commands.descriptions[index]
            space = " " * (50 - len(commands) - len(arguments))

            print(
                Messages.COMMAND_ROW.format(
                    commands=commands,
                    arguments=arguments,
                    space=space,
                    description=description,
                )
            )

    def _command_does_not_exist(self, *args):
        print(Messages.COMMAND_DOES_NOT_EXIST_ERROR)
