from unittest.mock import Mock
import pytest

from email_analyser.app import EmailAnalyser


class TestEmailAnalyser:
    @pytest.fixture
    def app(self):
        return EmailAnalyser()

    @pytest.fixture
    def file(self, mocker):
        file_mock = Mock()
        file_mock.read = Mock(return_value="sent@email.com")

        file = mocker.patch("email_analyser.app.open", return_value=file_mock)
        return file

    @pytest.fixture
    def email_generator(self, mocker):
        return_value = [
            "email@test.com",
            "test@email.com",
            "tester@email.com",
            "invalid.com",
            "incorrect@.com",
        ]
        mocker.patch(
            "email_analyser.app.EmailAnalyser._get_email_generator",
            return_value=return_value,
        )

    @pytest.fixture
    def none_email_gen(self, mocker):
        mocker.patch(
            "email_analyser.app.EmailAnalyser._get_email_generator", return_value=None
        )

    def test_get_incorrect_emails_should_return_list_of_invalid_emails(
        self, email_generator, app
    ):
        expected = ["invalid.com", "incorrect@.com"]

        result = app._get_incorrect_emails()

        assert expected == result

    def test_get_incorrect_emails_should_return_string_when_generator_is_none(
        self, app, none_email_gen
    ):
        result = app._get_incorrect_emails()

        assert isinstance(result, str)

    @pytest.mark.parametrize(
        ("expected", "phrase"), (({"tester@email.com"}, "er"), (set(), "nonexisted"))
    )
    def test_search_emails_should_return_set_of_emails_which_contain_phrase(
        self, email_generator, app, expected, phrase
    ):
        result = app._search_emails(phrase)

        assert expected == result

    def test_search_emails_should_return_string_when_generator_is_none(
        self, app, none_email_gen
    ):
        result = app._search_emails("test@email.com")

        assert isinstance(result, str)

    def test_get_grouped_emails_should_return_dict_where_key_is_domain_str_and_value_is_set(
        self, email_generator, app
    ):
        expected = {
            "email.com": {"test@email.com", "tester@email.com"},
            "test.com": {"email@test.com"},
        }
        result = app._get_grouped_emails()

        assert expected == result

    def test_grouped_sent_emails_should_return_string_when_generator_is_none(
        self, app, none_email_gen
    ):
        result = app._get_grouped_emails()

        assert isinstance(result, str)

    def test_get_not_sent_emails_should_return_string_when_file_does_not_exist(
        self, app
    ):
        result = app._get_not_sent_emails("path/to/nonexisted/file")

        assert isinstance(result, str)

    def test_get_not_sent_emails_should_return_set_which_not_contains_emails_in_file(
        self, mocker, app, file
    ):
        mocker.patch(
            "email_analyser.app.EmailAnalyser._get_email_generator",
            return_value=["not.sent@email.com"],
        )

        result = app._get_not_sent_emails("path/to/file")

        assert result == set(["not.sent@email.com"])

    def test_get_not_sent_emails_should_return_string_when_generator_is_none(
        self, app, none_email_gen
    ):
        result = app._get_not_sent_emails("path/to/file")

        assert isinstance(result, str)
