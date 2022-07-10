import os
import csv
from typing import Generator

from .types import ScandirIterator


DIRECTION = "emails"


class FileParser:
    def __init__(self, direction=DIRECTION):
        self.direction = direction

    def email_generator(self) -> Generator:
        files = os.scandir(self.direction)
        return self._parse_files(files)

    def _parse_files(self, files: ScandirIterator) -> Generator:
        for file in files:
            if file.name.endswith(".txt"):
                generator = self._read_txt_file(file.path)

            elif file.name.endswith(".csv"):
                generator = self._read_csv_file(file.path)

            else:
                continue

            for line in generator:
                yield line

    def _read_txt_file(self, file_path: str) -> Generator:
        with open(file_path, "r") as file:
            for line in file:
                yield line.strip()

    def _read_csv_file(self, file_path: str) -> Generator:
        with open(file_path, "r") as file:
            reader = csv.reader(file, delimiter=";")
            first_row = True

            for line in reader:
                if first_row:
                    first_row = False
                    continue
                yield line[1].strip()
