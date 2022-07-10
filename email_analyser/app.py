import re
from typing import Generator

from .simply_cli import SimplyCLI, register_command

from .email_analyser import (
    Messages,
    Descriptions,
    FileParser,
    EmailValidator,
)


class EmailAnalyser(SimplyCLI):
    def __init__(self):
        self.parser = FileParser()
        self.email_validator = EmailValidator()

        super().__init__()

    @register_command(("-ic", "--incorrect-emails"), Descriptions.INCORRECT_EMAILS)
    def incorrect_emails(self):
        incorrect_emails = self._get_incorrect_emails()

        if isinstance(incorrect_emails, list):
            print(
                Messages.INCORRECT_EMAILS.format(number_of_emails=len(incorrect_emails))
            )
            for email in incorrect_emails:
                print(Messages.EMAIL_ROW.format(email=email))
        else:
            print(incorrect_emails)

    @register_command(("-s", "--search"), Descriptions.SEARCH, ["phrase"])
    def search(self, phrase: str):
        found_emails = self._search_emails(phrase)

        if isinstance(found_emails, set):
            print(
                Messages.FOUND_EMAILS.format(
                    phrase=phrase, number_of_emails=len(found_emails)
                )
            )
            for email in found_emails:
                print(Messages.EMAIL_ROW.format(email=email))
        else:
            print(found_emails)

    @register_command(("-gbd", "--group-by-domain"), Descriptions.GROUP_BY_DOMAIN)
    def group_by_domain(self):
        grouped_emails = self._get_grouped_emails()

        if isinstance(grouped_emails, dict):
            print()
            for domain in sorted(grouped_emails.keys()):
                emails = grouped_emails[domain]
                print(
                    Messages.DOMAIN_GROUP.format(
                        domain=domain, number_of_emails=len(emails)
                    )
                )
                for email in sorted(emails):
                    print(Messages.EMAIL_ROW.format(email=email))
        else:
            print(grouped_emails)

    @register_command(
        ("-feil", "--find-emails-not-in-logs"),
        Descriptions.FIND_EMAILS_NOT_IN_LOGS,
        ["path_to_log"],
    )
    def find_emails_not_in_logs(self, path_to_log: str):
        not_sent_emails = self._get_not_sent_emails(path_to_log)

        if isinstance(not_sent_emails, set):
            print(
                Messages.NOT_SENT_EMAILS.format(number_of_emails=len(not_sent_emails))
            )
            for email in sorted(not_sent_emails):
                print(Messages.EMAIL_ROW.format(email=email))
        else:
            print(not_sent_emails)

    def _get_email_generator(self) -> Generator | None:
        try:
            return self.parser.email_generator()
        except FileNotFoundError:
            return

    def _get_incorrect_emails(self) -> list | str:
        email_generator = self._get_email_generator()

        if email_generator:
            incorrect_emails = []

            for email in email_generator:
                if not self.email_validator.validate(email):
                    incorrect_emails.append(email)

            return incorrect_emails
        return Messages.DIRECTION_ERROR.format(directory=self.parser.direction)

    def _search_emails(self, phrase: str) -> set | str:
        email_generator = self._get_email_generator()

        if email_generator:
            found_emails = set()

            for email in email_generator:
                if self.email_validator.validate(email) and phrase in email:
                    found_emails.add(email)

            return found_emails
        return Messages.DIRECTION_ERROR.format(directory=self.parser.direction)

    def _get_grouped_emails(self) -> dict[str, set]:
        email_generator = self._get_email_generator()

        if email_generator:
            grouped_emails = {}

            for email in email_generator:
                if self.email_validator.validate(email):
                    domain = email.split("@")[1]

                    if domain in grouped_emails:
                        grouped_emails[domain].add(email)
                    else:
                        grouped_emails[domain] = {email}

            return grouped_emails
        return Messages.DIRECTION_ERROR.format(directory=self.parser.direction)

    def _get_not_sent_emails(self, path: str) -> set:
        email_generator = self._get_email_generator()

        if email_generator:
            not_sent_emails = set()

            try:
                log = open(path, "r")
            except FileNotFoundError:
                return Messages.FILE_DOES_NOT_EXISTS_ERROR.format(file=path)

            sent_emails = log.read()

            for email in email_generator:
                is_valid = self.email_validator.validate(email)

                if is_valid:
                    sent = re.search(email, sent_emails)

                    if not sent:
                        not_sent_emails.add(email)

            log.close()

            return not_sent_emails
        return Messages.DIRECTION_ERROR.format(directory=self.parser.direction)
