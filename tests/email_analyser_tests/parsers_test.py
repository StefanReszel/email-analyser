from types import GeneratorType
from unittest.mock import Mock
import pytest

from email_analyser.email_analyser.parsers import FileParser


class TestFileParser:
    @pytest.fixture
    def parser(self):
        return FileParser()

    @pytest.fixture
    def file_content(self):
        return ["line1", "line2"]

    @pytest.fixture
    def txt_file(self):
        return "path/to/file.txt"

    @pytest.fixture
    def csv_file(self):
        return "path/to/file.csv"

    def test_read_txt_file_should_return_generator(
        self, parser, file_content, txt_file
    ):
        result = parser._read_txt_file(txt_file)

        assert isinstance(result, GeneratorType)

    def test_read_csv_file_should_return_generator(
        self, parser, file_content, csv_file
    ):
        result = parser._read_csv_file(csv_file)

        assert isinstance(result, GeneratorType)

    def test_parse_files_should_invoke_read_txt_file_when_file_ends_with_dot_txt(
        self, parser, mocker, txt_file, file_content
    ):
        mocker.patch("email_analyser.email_analyser.parsers.FileParser._read_txt_file")
        files = mocker.patch(
            "email_analyser.email_analyser.parsers.os.scandir", new=[Mock()]
        )
        files[0].name = txt_file

        parser._read_txt_file = Mock(return_value=file_content)

        generator = parser._parse_files(files)
        next(generator)

        assert parser._read_txt_file.called

    def test_parse_files_should_invoke_read_csv_file_when_file_ends_with_dot_csv(
        self, parser, mocker, csv_file, file_content
    ):
        mocker.patch("email_analyser.email_analyser.parsers.FileParser._read_csv_file")
        files = mocker.patch(
            "email_analyser.email_analyser.parsers.os.scandir", new=[Mock()]
        )
        files[0].name = csv_file

        parser._read_csv_file = Mock(return_value=file_content)

        generator = parser._parse_files(files)
        next(generator)

        assert parser._read_csv_file.called
