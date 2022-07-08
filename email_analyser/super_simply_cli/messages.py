from sys import orig_argv


class Messages:
    help_exclude = -1 if "-h" in orig_argv or "--help" in orig_argv else None
    _APP_NAME = " ".join(orig_argv[:help_exclude])

    MULTIPLE_ARGS = '[...]'
    HELP = "\nUsage:\n" f"    {_APP_NAME} <command> {MULTIPLE_ARGS}\n\n" "Commands:"
    COMMAND_ROW = "    {commands} {arguments}{space}{description}"

    COMMAND_DOES_NOT_EXIST_ERROR = "[ERROR] Command does not exist."
    TAKES_NO_ARGUMENTS_ERROR = "[ERROR] This command does not take arguments."
    TOO_MANY_ARGUMENTS_ERROR = "[ERROR] Too many arguments provided."
    NOT_ENOUGH_ARGUMENTS_ERROR = "[ERROR] Not enough arguments provided."
    TYPE_ERROR = "[ERROR] To '{name_of_arg}' you can pass only list or tuple."
    BAD_QUANTITY_OF_COMMANDS_ERROR = (
        "[ERROR] You can provide either one or two 'commands'."
    )
