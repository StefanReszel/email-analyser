import pytest

from email_analyser.simply_cli.components.registry import CommandRegistry


class RegistryFixtures:
    @pytest.fixture
    def example_task(self):
        def example_task():
            pass

        return example_task

    @pytest.fixture
    def task_data(self, example_task):
        return {
            "task": example_task,
            "commands": ("--example-task", "-et"),
            "arguments": ("argument"),
            "description": "This is example task used in tests.",
        }

    @pytest.fixture
    def registry(self, task_data):
        return CommandRegistry(**task_data)

    @pytest.fixture
    def registered_task_id(self, registry):
        return registry.index

    @pytest.fixture
    def register(self, registry):
        registry.register()
        yield
        del CommandRegistry.registered_tasks[registry.index]
        del CommandRegistry.registered_commands[registry.index]
        del CommandRegistry.registered_descriptions[registry.index]
        del CommandRegistry.registered_arguments[registry.index]


class TestCommandRegistry(RegistryFixtures):
    def test_registered_tasks_class_attribute_should_containts_index_of_task_in_keys_when_register_method_invoked(
        self, register, registered_task_id
    ):
        assert registered_task_id in CommandRegistry.registered_tasks.keys()

    def test_registered_commands_class_attribute_should_containts_index_of_task_in_keys_when_register_method_invoked(
        self, register, registered_task_id
    ):
        assert registered_task_id in CommandRegistry.registered_commands.keys()

    def test_registered_arguments_class_attribute_should_containts_index_of_task_in_keys_when_register_method_invoked(
        self, register, registered_task_id
    ):
        assert registered_task_id in CommandRegistry.registered_arguments.keys()

    def test_registered_descriptions_class_attribute_should_containts_index_of_task_in_keys_when_register_method_invoked(
        self, register, registered_task_id
    ):
        assert registered_task_id in CommandRegistry.registered_descriptions.keys()

    def test_registered_tasks_class_attribute_should_containts_name_of_task_on_registered_task_id_when_register_method_invoked(
        self, register, registered_task_id, task_data
    ):
        task_name = task_data["task"].__name__

        assert CommandRegistry.registered_tasks[registered_task_id] == task_name

    def test_registered_commands_class_attribute_should_containts_commands_on_registered_task_id_when_register_method_invoked(
        self, register, registered_task_id, task_data
    ):
        commands = task_data["commands"]

        assert CommandRegistry.registered_commands[registered_task_id] == commands

    def test_registered_arguments_class_attribute_should_containts_arguments_on_registered_task_id_when_register_method_invoked(
        self, register, registered_task_id, task_data
    ):
        arguments = task_data["arguments"]

        assert CommandRegistry.registered_arguments[registered_task_id] == arguments

    def test_registered_descriptions_class_attribute_should_containts_description_on_registered_task_id_when_register_method_invoked(
        self, register, registered_task_id, task_data
    ):
        description = task_data["description"]

        assert (
            CommandRegistry.registered_descriptions[registered_task_id] == description
        )
