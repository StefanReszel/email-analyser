import pytest
from unittest.mock import Mock

from email_analyser.simply_cli.components.decorators import CommandRegister
from email_analyser.simply_cli.components.errors import (
    NotEnoughArgumentsError,
    TooManyArgumentsError,
)


class TestCommandRegister:
    @pytest.fixture
    def command_register(self):
        return CommandRegister()

    @pytest.fixture
    def arguments(self):
        return ["arg1", "arg2"]

    @pytest.fixture
    def expected_order_of_commands(self):
        return ("short-first", "longer-second")

    @pytest.mark.parametrize("invalid_value", ("invalid_value", 123, dict(), set()))
    def test_validate_arguments_should_raise_error_when_provided_value_is_not_list_or_tuple(
        self, command_register, invalid_value
    ):
        with pytest.raises(TypeError):
            command_register._validate_arguments(invalid_value)

    def test_prepare_arguments_should_return_list_of_arguments_in_angle_brackets_when_count_arguments_is_true(
        self, command_register, arguments
    ):
        expected = ["<arg1>", "<arg2>"]

        result = command_register._prepare_arguments(
            arguments=arguments, count_arguments=True
        )

        assert result == expected

    def test_prepare_arguments_should_return_list_with_ellipsis_in_square_brackets_when_count_arguments_is_false(
        self, command_register, arguments
    ):
        expected = ["[...]"]

        result = command_register._prepare_arguments(
            arguments=arguments, count_arguments=False
        )

        assert result == expected

    @pytest.mark.parametrize("invalid_value", ("invalid_value", 123, dict(), set()))
    def test_validate_commands_should_raise_error_when_provided_value_is_not_list_or_tuple(
        self, command_register, invalid_value
    ):
        with pytest.raises(TypeError):
            command_register._validate_commands(invalid_value)

    @pytest.mark.parametrize(
        "invalid_value",
        ((), ("arg1", "arg2", "arg3"), ("arg1", "arg2", "arg3", "arg4")),
    )
    def test_validate_commands_should_raise_error_when_lenght_of_provided_value_is_not_1_or_2(
        self, command_register, invalid_value
    ):
        with pytest.raises(TypeError):
            command_register._validate_commands(invalid_value)

    def test_prepare_commands_should_change_order_of_commands_when_is_not_provided_as_expected(
        self, command_register, expected_order_of_commands
    ):
        commands = ("longer-second", "short-first")

        result = command_register._prepare_commands(commands)

        assert result == expected_order_of_commands

    def test_prepare_commands_should_return_commands_as_provided_if_provided_as_expected(
        self, command_register, expected_order_of_commands
    ):
        commands = ("short-first", "longer-second")

        result = command_register._prepare_commands(commands)

        assert result == expected_order_of_commands

    def test_prepare_commands_should_return_commands_as_provided_if_lenght_of_their_equals_1(
        self, command_register
    ):
        commands = ("single-command",)

        result = command_register._prepare_commands(commands)

        assert result == commands

    def test_count_arguments_should_return_none_when_provided_proper_amount_of_arguments_and_function_is_decorated(
        self, command_register, arguments
    ):
        result = command_register._count_arguments(
            required_args=arguments, provided_args=arguments
        )

        assert result is None

    def test_count_arguments_should_return_none_when_provided_proper_amount_of_arguments_and_method_is_decorated(
        self, command_register, arguments
    ):
        self = Mock()
        provided_args = [self, "arg1", "arg2"]

        result = command_register._count_arguments(
            required_args=arguments, provided_args=provided_args
        )

        assert result is None

    def test_count_arguments_should_raise_error_when_len_of_provided_args_is_less_than_required_args(
        self, command_register, arguments
    ):
        provided_args = arguments[:-1]

        with pytest.raises(NotEnoughArgumentsError):
            command_register._count_arguments(
                required_args=arguments, provided_args=provided_args
            )

    def test_count_arguments_should_raise_error_when_len_of_provided_args_is_greater_than_required_args(
        self, command_register, arguments
    ):
        required_args = arguments[:-1]

        with pytest.raises(TooManyArgumentsError):
            command_register._count_arguments(
                required_args=required_args, provided_args=arguments
            )
