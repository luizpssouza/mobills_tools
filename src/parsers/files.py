from dynaconf import settings
import glob
import os
import sys

import parsers.bank as parser_bank

IGNORE_LINES_CONTAINS_IN_FILE = [
    "saldo em"
]

PATH_EXECUTION = settings.PATH_CONTAINS_BANK_STATEMENT_FILES


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
    bank = parser_bank.get_bank(file_name_as_bank)

    print("#################")
    print(bank.__name__)
    print("#################")

    with open(file, "r") as file:
        lines_of_file = file.readlines()
        bank.process(lines_of_file, file_name_as_bank)


def list_files():
    files = glob.glob(f"{PATH_EXECUTION}/*.txt")
    for file in files:
        read_file(file)