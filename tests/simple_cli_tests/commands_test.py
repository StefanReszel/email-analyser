import pytest

from email_analyser.simply_cli.components.commands import Commands
from tests.simple_cli_tests.registry_test import RegistryFixtures


class TestCommands(RegistryFixtures):
    @pytest.fixture
    def commands(self, register):
        return Commands()

    @pytest.fixture
    def example_task_command(self, request, task_data):
        commands = task_data["commands"]

        return commands[request.param]

    @pytest.mark.parametrize("help_command", ("-h", "--help"))
    def test_when_help_task_obtained_get_command_id_should_return_0(
        self, commands, help_command
    ):
        result = commands.get_command_id(help_command)

        assert result == 0

    @pytest.mark.parametrize("example_task_command", (0, 1), indirect=True)
    def test_when_example_task_obtained_get_command_id_should_return_id_of_task(
        self, commands, example_task_command, registered_task_id
    ):
        result = commands.get_command_id(example_task_command)

        assert result == registered_task_id

    @pytest.mark.parametrize("nonexisted_command", ("--nonexisted", "-ne"))
    def test_get_command_id_should_return_minus_1_when_nonexisted_task_obtained(
        self, commands, nonexisted_command
    ):
        result = commands.get_command_id(nonexisted_command)

        assert result == -1
