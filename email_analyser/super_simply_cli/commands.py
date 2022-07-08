from .register import CommandRegister


class Commands:
    def __init__(self):
        self.commands = CommandRegister.registered_commands
        self.arguments = CommandRegister.registered_arguments
        self.descriptions = CommandRegister.registered_descriptions

    def get_command_id(self, command: str) -> int:
        for index in self.commands:
            if command in self.commands[index]:
                return index
        return -1
