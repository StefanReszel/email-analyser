import pytest

from email_analyser.email_analyser.validators import EmailValidator


class TestEmailValidator:
    @pytest.fixture
    def validator(self):
        return EmailValidator()

    @pytest.mark.parametrize(
        "invalid_email",
        (
            "@",
            "email",
            "email.com",
            "email@.com",
            "@email.com",
            "email@test.",
            "email@test.commm",
            "email.test@.com.pl",
            "email@test@domain.com",
            "email.test@domain.commm.pl",
            "email.test@domain.com.pllll",
        ),
    )
    def test_validate_should_return_false_when_invalid_emails_provided(
        self, validator, invalid_email
    ):
        assert not validator.validate(invalid_email)

    @pytest.mark.parametrize(
        "invalid_email", ("test@email.com", "test.user@email.com.pl")
    )
    def test_validate_should_return_true_when_valid_emails_provided(
        self, validator, invalid_email
    ):
        assert validator.validate(invalid_email)
