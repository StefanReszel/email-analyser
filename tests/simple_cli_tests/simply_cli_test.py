import pytest

from email_analyser.simply_cli.simply_cli import SimplyCLI
from email_analyser.simply_cli.components import Messages


class TestSimplyCLI:
    @pytest.fixture
    def app(self):
        return SimplyCLI()

    @pytest.fixture
    def set_argv(self, mocker):
        mocker.patch(
            "email_analyser.simply_cli.simply_cli.argv", new=["main.py", "arg1", "arg2"]
        )

    def test_run_should_invoke_command_does_not_exist_method_when_get_command_id_returns_minus_1(
        self, app, mocker, set_argv
    ):
        mocker.patch(
            "email_analyser.simply_cli.simply_cli.SimplyCLI._command_does_not_exist"
        )
        mocker.patch(
            "email_analyser.simply_cli.simply_cli.Commands.get_command_id",
            return_value=-1,
        )

        app.run()

        assert app._command_does_not_exist.called

    def test_run_should_print_concrete_message_when_to_task_which_takes_no_args_they_have_been_provided(
        self, app, mocker, set_argv
    ):
        mocker.patch(
            "email_analyser.simply_cli.simply_cli.Commands.get_command_id",
            return_value=0,
        )

        print_mock = mocker.patch("email_analyser.simply_cli.simply_cli.print")

        app.run()

        print_mock.assert_called_with(Messages.TAKES_NO_ARGUMENTS_ERROR)
