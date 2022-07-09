from types import FunctionType


class CommandRegistry:
    registered_tasks = {}
    registered_commands = {}
    registered_arguments = {}
    registered_descriptions = {}

    def __init__(
        self, task: FunctionType, commands: tuple, arguments: list, description: str
    ):
        self.index = len(self.registered_tasks)

        self.task = task.__name__
        self.commands = commands
        self.arguments = arguments
        self.description = description

    def register(self):
        self.registered_tasks[self.index] = self.task
        self.registered_commands[self.index] = self.commands
        self.registered_arguments[self.index] = self.arguments
        self.registered_descriptions[self.index] = self.description
