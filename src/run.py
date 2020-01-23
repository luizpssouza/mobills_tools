import glob
import os
import sys

from dynaconf import settings

from parsers.default import format_line
from parsers.category import find as find_category
from parsers.words import replace as replace_word

PATH_EXECUTION = settings.PATH_CONTAINS_BANK_STATEMENT_FILES

IGNORE_LINES_CONTAINS_IN_FILE = [
    "saldo em"
]


def is_ignored(line: str) -> bool:
    for contains_with in IGNORE_LINES_CONTAINS_IN_FILE:
        if contains_with in line.lower():
            return True

    return False


def remove_lines_contains(lines):
    for line in lines:
        if not is_ignored(line):
            yield line


def read_file(file: str):
    file_name_as_bank, extension = os.path.splitext(os.path.basename(file))
    print("#################")
    print(file_name_as_bank)
    print("#################")
    with open(file, "r") as file:
        lines_of_file = file.readlines()

        for line in remove_lines_contains(lines_of_file):
            line = format_line(line)
            line += f',{file_name_as_bank}'
            line = find_category(line)
            line = replace_word(line)
            print(line)


def list_files():
    files = glob.glob(f"{PATH_EXECUTION}/*.txt")
    for file in files:
        read_file(file)


if __name__ == '__main__':
    list_files()
