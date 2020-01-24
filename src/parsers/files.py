import glob
import os
import sys


from dynaconf import settings


import parsers.bank as parser_bank


def list_files():
    files_path = glob.glob(
        f"{settings.PATH_CONTAINS_BANK_STATEMENT_FILES}/*.txt"
    )
    for file_path in files_path:
        read_file(file_path)


def read_file(file: str):
    file_name_as_bank, extension = os.path.splitext(os.path.basename(file))
    bank = parser_bank.get_bank(file_name_as_bank)

    print("#################")
    print(bank.__name__)
    print("#################")

    with open(file, "r") as file:
        lines_of_file = file.readlines()
        bank.process(lines_of_file, file_name_as_bank)
