from .registry import CommandRegistry


class Commands:
    def __init__(self):
        self.commands = CommandRegistry.registered_commands
        self.arguments = CommandRegistry.registered_arguments
        self.descriptions = CommandRegistry.registered_descriptions

    def get_command_id(self, command: str) -> int:
        for index in self.commands:
            if command in self.commands[index]:
                return index
        return -1
